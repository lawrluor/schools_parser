import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Code to make Chrome browser run silently ('headless')
# Adapted from https://stackoverflow.com/questions/16180428/can-selenium-webdriver-open-browser-windows-silently-in-background

# CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = './chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                           chrome_options=chrome_options
                          )  

def searchBySchool():
	# with open('non_private_manual.txt', encoding = "ISO-8859-1") as input_file:
	with open('outliers2.txt', encoding = "ISO-8859-1") as input_file:
		with open('processed.txt', "w") as output_file:
			counter = 0
			for line in input_file:
				counter += 1
				values = line.split('\t')
				school_name = values[2].strip()

				browser.get('http://profiles.doe.mass.edu/search/search_new.aspx?leftNavId=11241') # search page
				search = browser.find_element_by_id("ctl00_ContentPlaceHolder1_quickSearchText")

				search.send_keys(school_name)
				search.send_keys(Keys.RETURN) # hit return after search text entered
				time.sleep(2)

				# Search result string: Center For Technical Education Innovation ( 01530605 )  -  Public School
				results_table = browser.find_element_by_tag_name('table')
				search_results = results_table.find_elements_by_css_selector('td.newblubg')
				if len(search_results) > 0:
					school_result = search_results[0]

					# Extract ID from school_result string, between parentheses with space
					school_result = school_result.text
					re_result = re.search('\( (.*) \)', school_result)
					school_id = re_result.group(1)

					# Consolidate data into new tab separated line and write to output file
					new_line = school_name + '\t' + school_id + '\n'
					print(counter, new_line)
					output_file.write(new_line)
				else:
					# write school name with ID empty for tracking purposes
					new_line = school_name + '\t' + "school_not_found" + '\n'
					print(counter, new_line)
					output_file.write(new_line)

searchBySchool()