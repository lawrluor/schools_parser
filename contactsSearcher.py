import urllib
import http
from urllib.request import urlopen
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def processContactInfo():
	with open('master.txt', encoding = "ISO-8859-1") as input_file:
		with open('processed.txt', "w") as output_file:
			for line in input_file:
				school_id = line.split('\t')[3]
				if school_id != "school_not_found":
					url = "http://profiles.doe.mass.edu/profiles/general.aspx?topNavId=1&orgcode=" + str(school_id) + "&orgtypecode=6&leftNavId=122&"
					results = parseContactsBox(url)

					info_line = results['Title'] + '\t' + results['Name'] + '\t' + results['Phone'] + '\t' + results['Fax'] + '\n'
					output_file.write(info_line)
				else:
					info_line = "not_found" + '\t' + "not_found" + '\t' + "not_found" + '\t' + "not_found" + '\n'
					output_file.write(info_line)

# CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = './chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                           chrome_options=chrome_options
                          )  

def parseContactsBox(url):
	results = {'Title': '', 'Name': '', 'Phone': '', 'Fax': ''}

	# Parse with urllib and BS4
	# page = urllib.request.urlopen(url)
	# soup = BeautifulSoup(page, "lxml")
	# info_table = soup.find("table", class_="t_detail")

	# Parse with Selenium
	browser.get(url) # search page
	found_items = browser.find_elements_by_css_selector('table.t_detail')

	if len(found_items) > 0:
		# Correct format found

		# Parse Principal Information
		# td_data = info_table.find('td')
		# Grab next td using BS4 or Selenium
		# .next.next.next
		# td_data = td_data.find_element_by_xpath("//td/following-sibling::td")

		info_table = found_items[0]
		td_data = info_table.find_elements_by_tag_name('td')
		results['Title'] = td_data[0].text.strip()
		results['Name'] = td_data[1].text.strip()
		results['Phone'] = td_data[2].text.strip()
		results['Fax'] = td_data[3].text.strip()

	# else:
	# 	# try alternate parsing method

	print(results)
	return results

# parseContactsBox("http://profiles.doe.mass.edu/profiles/general.aspx?topNavId=1&orgcode=08720605&orgtypecode=6&leftNavId=122&")
processContactInfo()

# Principal Info
# <table border="1" class="t_detail">
# <tbody><tr>
# <th width="200">Function</th>
# <th width="150">Contact Name</th>
# <th width="100">Phone</th>
# <th width="100">Fax</th>
# </tr>
# <tr>
# <td>Principal</td>
# <td>Margaret A McDevitt</td>
# <td>--</td>
# <td>978-459-0456</td>
# </tr>
# <tr class="altrow">
# <td>Nutrition Coordinator</td>
# <td>Margaret A McDevitt</td>
# <td>--</td>
# <td>978-459-0456</td>
# </tr>
# </tbody></table>