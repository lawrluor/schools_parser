with open('outliers3.txt', encoding = "ISO-8859-1") as input_file:
	with open('processed.txt', "w") as output_file:
		for line in input_file:
			line = line.strip()
			line = line.replace('"', '') # remove quote chars

			# Delete 'School' in school name
			line = line.replace('School', '')
			line = line.replace('school', '')
			new_line = line + '\n'

			print(new_line)
			output_file.write(new_line)
