import shutil, os, re 

datePattern = re.compile(r'''
	^(.*?) # text before the date
	((0|1)?\d)- # one or two digits for the month
	((0|1|2|3)?\d)- # one or two digits for the day
	((19|20)\d\d) # four digits for the year
	(.*?)$ # all text after the date
	''', re.VERBOSE)

for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilenames)

	if mo == None:
		continue

	before_part = mo.group(1)
	month_part = mo.group(4)
	day_part = mo.group(2)
	year_part = mo.group(6)
	after_part = mo.group(8)

	euroFilename = before_part + day_part + '-' + month_part + '-' + 'year_part' + after_part
	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFilename = os.path.join(absWorkingDir, euroFilename)

	print('Renaming the %s to %s ...' % (amerFilename, euroFilename))
	# shutil.move(amerFilename, euroFilename)
