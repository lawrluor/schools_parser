with open('mass_high_schools_txt.txt', encoding = "ISO-8859-1") as input_file:
	with open('processed.txt', "w") as output_file:
		for line in input_file:
			line = line.replace('"', '') # remove quote chars
			if '/w/' not in line:
				output_file.write(line)