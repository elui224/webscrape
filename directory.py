
import bs4
from urllib.request import urlopen as urlreq
from bs4 import BeautifulSoup as soup

'''
The function returns a list of tuples contained in all_schools.
For example, each tuple is (school name, url)
'''

root_url = 'http://www.montgomeryschoolsmd.org/directory/' #root link that all school links begin with. Used to concatenate.
all_schools = [] #Will be a list of tuples (school name, school's URL)

def getSchools(url):
	try:
		urlclient = urlreq(url)
		page_html = urlclient.read()
		urlclient.close()
	except Exception as e: 
		print(e.message)
		return #If url does not exist, it skips and continues with the program.

	try:
		page_soup = soup(page_html, "html.parser")
		obj1 = page_soup.find_all("div", "column") #gets elementary schools obj1[0]:obj1[24]. Need to chop off [25]:[30]
		obj2 = page_soup.find_all("div", "columnbig") #gets middle schools, high schools, and special
	except AttributeError:
		print("Error creating soup object")

	#appends text and href to create the list of tuples called all_schools
	for li in obj1[:-5] + obj2: #Exclude last five elements in obj1 because they aren't schools.
		li_obj = li.find_all('li')
		for item in li_obj:
			a_obj = item.find_all('a')
			for sch in a_obj:
				all_schools.append( (sch.text.strip(), root_url+sch.get('href')) )
				# print(all_schools)
	return all_schools
	