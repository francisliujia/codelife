#  CSV: common seperate values
import csv


with open('names.csv', 'r') as csv_file:
	csv_file = csv.reader(csv_file)

	with open('new_names.csv', 'w') as new_file:
		# csv_writer = csv.writer(new_file, delimiter = '-')
		csv_writer = csv.writer(new_file, delimiter = '\t')

		for line in csv_reader:
			csv_writer.writerow(line)


	# next(csv_reader)

	# for line in csv_file:
	# 	print(line[2])


	with open('names.csv', 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)

		# for line in csv_reader:
		# 	print(line)
		# 	print(line['email'])

		with open('new_names.csv', 'w') as new_file:
		# csv_writer = csv.writer(new_file, delimiter = '-')
		fieldnames = ['first_name', 'last_name', 'email']

			csv_writer = csv.DictWriter(new_file, filenames=fieldnames delimiter = '\t')

			csv_writer.writeheader()

			for line in csv_reader:
				del line['email']
				csv_writer.writerow(line)
















