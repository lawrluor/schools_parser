from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Selenium + Chrome webdriver set up
# CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = './chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                           chrome_options=chrome_options
                          )  

def processEmailBox():
	with open('master.txt', encoding = "ISO-8859-1") as input_file:
		with open('processed.txt', 'w') as output_file:
			for line in input_file:
				values = line.split('\t')
				school_id = values[3]

				if school_id != "school_not_found":
					url = "http://profiles.doe.mass.edu/general/general.aspx?topNavID=1&leftNavId=100&orgcode=" + str(school_id) + "&orgtypecode=6"
					email = parseEmailBox(url)
					new_line = school_id + '\t' + email + '\n'

					print(new_line)
					output_file.write(new_line)
				else:
					output_file.write("no_school_id")
					return

def parseEmailBox(url):
	# Extracting and parsing by HTML section: https://stackoverflow.com/questions/46730306/parsing-text-from-certain-html-elements-using-selenium
	browser.get(url)
	found_item = browser.find_element_by_id('whiteboxRight')
	email_results = browser.find_elements_by_partial_link_text('@')

	# Catch missing email
	if not email_results or len(email_results) == 0:
		print("email not found")
		return "not_found"
	else:
		email = email_results[0].text.strip()
		return email

processEmailBox()
