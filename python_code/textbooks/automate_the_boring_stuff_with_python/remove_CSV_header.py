import csv, os 

os.makedirs('headerRemoved', exist_ok = True)

for csv_file_name in os.listdir('.'):
	if not csv_file_name.endswith('.csv'):
		continue
	print('Removing header from ' + csv_file_name + '...')

	csv_rows = []
	csv_file_obj= open(csv_file_name)
	reader_obj = csv.reader(csv_file_obj)
	for row in reader_obj:
		if reader_obj.line_num == 1:
			continue
		csv_rows.append(row)
	csv_file_obj.close()

for csv_file_obj in os.listdir('.'):
	if not csv_file_name.endswith('.csv'):
		continue
	csv_file_obj = open(os.path.join('headerRemoved', csv_file_name), 'w', newline='')
	csv_writer = csv.writer(csv_file_obj)
	for row in csv_rows:
		csv_writer.writerow(row)
	csv_file_obj.close()