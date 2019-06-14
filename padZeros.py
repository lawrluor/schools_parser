def padZeros():
	with open('full_names_and_ids.txt', encoding = "ISO-8859-1") as input_file:
		with open('processed.txt', "w") as output_file:
			for line in input_file:
				values = line.split('\t')
				school_id = values[1].strip()

				if school_id != "school_not_found":
					if len(school_id) < 8:
						num_zeros = 8 - len(school_id)
						padded_zeros = num_zeros * '0'
						padded_school_id = padded_zeros + school_id
						output_file.write(values[0] + '\t' + padded_school_id + '\n')
					else:
						print("8 digit id found")
						output_file.write(values[0] + '\t' + school_id + '\n')
				else:
					output_file.write(values[0] + '\t' + school_id + '\n')

padZeros()
