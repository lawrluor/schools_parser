with open('outliers2.txt', encoding = "ISO-8859-1") as input_file:
	with open('processed.txt', "w") as output_file:
		for line in input_file:
			line = line.replace('"', '') # remove quote chars

			values = line.split('\t')
			school_city = values[0].split(',') # grab first column
			school = school_city[0].strip()
			city = school_city[1].strip()

			new_line = city + '\t' + school + '\n'
			print(new_line)

			output_file.write(new_line)
