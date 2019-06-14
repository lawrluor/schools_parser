from html_parser import parseHTML

with open('wiki_searchable.txt', encoding = "ISO-8859-1") as input_file:
	with open('processed.txt', "w") as output_file:
		for line in input_file:
			line = line.replace('"', '') # remove quote chars
			values = line.split('\t')
			school_type = parseHTML(values[1])

			new_line = school_type + '\t' + values[0] + '\t' + values[1]
			print(new_line)

			if school_type != "private":
				output_file.write(new_line)

