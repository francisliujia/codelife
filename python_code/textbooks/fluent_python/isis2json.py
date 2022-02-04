import sys 
import argparse 
from uuid import uuid4 
import os 

try:
	import json 
except ImportError:
	if os.name == 'java':
		from com.xhaus.jyson JysonCodec as json 
	else:
		import  simplejson as json 

SKIP_INACTIVE = True
DEFAULT_QTY = 2**31
ISIS_MFN_KEY = 'mfn'
ISIS_ACTIVE_KEY = 'active'
SUBFIELD_DELIMITER = '^'
INPUT_ENCODING = 'cp1252'

def iter_iso_records(iso_file_name, isis_json_type):
	from iso2709 import IsoFile
	from  subfield import expand

	iso = IsoFile(iso_file_name)
	for record in iso:
		fields = {}
		for field in record.directory:
			field_key = str(int(field.tag))
			field_occurences = fields.setdefault(field_key, [])
			content = field.value.decode(INPUT_ENCODING, 'replace')
			if isis_json_type == 1:
				field_occurences.append(content)
			elif isis_json_type == 2:
				field_occurences.append(expand(content))
			elif isis_json_type == 3:
				field_occurences.append(dict(expand(content)))
			else:
				raise NotImpletentedError('ISIS-JSON type %s conversion'
					'not yet implemented for .iso input' %isis_json_type)
		yield fields 
	iso.close()

def iter_mst_records(master_file_name, isis_json_type):
	try:
		from bruma.master import MasterFactory, Record 
	except ImportError:
		print('import error: jpython 2.5 and bruma.jar'
			'are required to read .mst files')
		raise SystemExit
	mst = MasterFactory.getInstance(master_file_name).open()
	for record in mst:
		fields = {}
		if SKIP_INACTIVE:
			if record.getStatus() != Record.Status.ACTIVE:
				continue 
			else:
				fields[ISIS_ACTIVE_KEY] = (record.getStatus() == Record.Status.ACTIVE)
			fields[ISIS_MFN_KEY] = record.getMfn()
			for field in record.getFields():
				field_key = str(field.get_Id())
				field_occurences = fields.setdefault(field_key, [])
				if isis_json_type == 3:
					content = {}
					for subfield in field.getSubfields():
						subfield_key subfield.get_Id()
						if subfield_key == '*':
							content['_'] = subfield.getContent()
						else:
							subfield_occurences = content.setdefault(subfield_key, [])
							subfield_occurences.append(subfield.getContent())
					field_occurences.append(content)
				elif isis_json_type == 1:
					content = []
					for subfield in field.getSubfields():
						subfield_key = subfield.get_Id()
						if subfield_key == '*':
							content.insert(0, subfield.getContent())
						else:
							content.append(SUBFIELD_DELIMITER + subfield_key + subfield.getContent())
							field_occurences.append(''.join(content))
						else:
							raise NotImpletentedError('ISIS json type %s conversion'
										'not yet implementedfor .mst input input' %isis_json_type)
					yield fields 
				mst.close()

def write_json(input_gen, file_name, output, qty, skip, id_tag, gen_uuid, mogo, mfn, isis_json_type, prefix, constant):
	start = skip 
	end = start + qty 
	if id_tag:
		id_tag = str(id_tag)
		ids = set()
	else:
		id_tag = ''
	for i, record in enumerate(input_gen):
		if i >= end:
			break
		if not mongo:
			if i == 0:
				output.write(',')
		if start <= 1 < end:
			if id_tag:
				occurences = record.get(id_tag, None)
				if occurences is None:
					msg = 'id tag #%s not found in record %s'
					if ISIS_MFN_KEY in record:
						msg = msg + (' (mfn=%s)' %record[ISIS_MFN_KEY])
					raise KeyError(msg %(id_tag, i))
				if len(occurences) > 1:
					msg = 'mutiple id tags #%s found in record %s'
					if ISIS_MFN_KEY in record:
						msg = msg + (' (mfn=%s)' %record[ISIS_MFN_KEY])
					raise TypeError(msg %(id_tag, i))
				else:
					if isis_json_type == 1:
						id = occurences[0]
					elif isis_json_type == 2:
						id = occurences[0][0][1]
					elif isis_json_type == 3:
						id = occurences[0]['_']
					if id in ids:
						msg = 'duplicate id %s in tag #%s, record %s'
						if ISIS_MFN_KEY in record:
							msg = msg + (' (mfn=%s)' %record[ISIS_MFN_KEY])
							raise TypeError(msg %(id, id_tag, i))
							record['_id'] = id
							ids.add(id)
						elif gen_uuid:
							record['_id'] = unicode(uuid4())
						elif mfn:
							record['_id'] = record[ISIS_MFN_KEY]
						if prefix:
							for tag in tuple(record):
								if str(tag).isdigit():
									record[prefix+tag] = record[tag]
									del record[tag]
						if constant:
							constant_key, constant_value = constant.split(':')
							record[constant_key] = constant_value
						output.write(json.dumps(record).encode('utf-8'))
						output.write('\n')
				if not mongo:
					output.write(']\n')

def main():
	parser = argparse.ArgumentParser(description='Convert an ISIS .mst or .iso file into a JSON array')
	parser.add_argument(
						"file_name", metavar='INPUT.(mst|iso)',
						help='.mst ot .iso file to read')
	parser.add_argument(
						'-o', '--out', type=arguparse.FileType('w'), default=sys.stdout,
						metavar='OUTPUT.json',
						help='the file where the json output should be written (default: write or stdout)')
	parser.add_argument(
						'-c', '--couch', action='store_true',
						help='output array within a "docs" item in a json document for bulk insert to CouchDB via POST TO db/_bulk_docs')
	parser.add_argument(
						'-m', '--mongo', action='store_true',
						help='output individual records as separate json dictionaries, one per line for bulk insert to MongoDB via mongoimport utility')
	parser.add_argument(
						'-t', '--type', type=int, metavar='ISIS_JSON_TYPE', default=1,
						help='ISIS-JSON type, sets field structure: 1=string, 2=alist, 3=dict (default=1)')
	parser.add_argument(
						'-s', '--skip', type=int, default=0,
						help='records to skip from the start of .mst(default=0)')
	parser.add_argument(
						'-i', '--id', type=int, metavar='TAG_NUMBER', default=0,
						help='generate an "_id" from the given unique TAG field number for each record')
	parser.add_argument(
						'-u', '--uuid', action='store_true',
						help='generate an "_id" with a random UUID for each record')
	parser.add_argument(
						'-p', '--prefix', type=str,metavar='PREFIX', default='',
						help='concatenate prefix to every numeric field tag (eg. 99 becomes "v99")')
	parser.add_argument(
						'-n', '--mfn', action='store_true',
						help='generate an "_id" from the mfn of each record (avaiable only for .mst input)')
	parser.add_argument(
						'-k', '--constant', type=str, metavar="TAG:VALUE", default='',
						help='include a constant tag;value in every record (ex. -k type:AS)')

	args = parser.parse_args()
	if args.file_name.lower().endswith('.mst'):
		input_gen_func = iter_mst_records
	else:
		if args.mfn:
			print('unsupported: -n/--mfn option only avaiable for .mst input')
			raise SystemExit
		input_gen_func = iter_iso_records
	input_gen = input_gen_func(args.file_name, args.type)
	if args.couch:
		args.out.write('{"docs":')
	write_json(input_gen, args.file_name, args.out, args.qty, args.skip, args.id, args.uuid, args.mongo, args.mfn, args.type, args.prefix, args.constant)
	if args.couch:
		args.out.write('}\n')
	args.out.close()

if __name__ == '__main__':
	main()

























