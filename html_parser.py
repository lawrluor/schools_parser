import urllib.request
from bs4 import BeautifulSoup

def parseHTML(url):
	page = urllib.request.urlopen(url).read()

	soup = BeautifulSoup(page, "lxml")
	infobox = soup.find("table", class_="infobox")

	if infobox:
		data = infobox.get_text()
		# data = infobox.find('td')
	else:
		return "not_found"

	if 'Private' in data:
		return "private"
	elif 'Public' in data:
		return "public"
	else:
		return "unknown"