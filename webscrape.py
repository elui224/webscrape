import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.montgomeryschoolsmd.org/directory/directory_Boxschool.aspx?processlevel=04757'

#Open connection, download page.
uClient = uReq(my_url)

#puts content into a variable.
page_html = uClient.read()

#close connection.
uClient.close()

#stores page HTML into variable. HTML parse.
page_soup = soup(page_html, "html.parser")

#gets HTML elements h3 on url.
#page_soup.h3

#Finds section with teacher information on the page. stores in variable.
teachers = page_soup.findAll("div", {"id": "ctl00_ContentPlaceHolder1_pnlStructure"})

#Finds teacher name and phone number.
name = teachers.findAll("ul", {"class": "box-one-light"})

# filename = "teachers.csv"
# f = open(filename, "w")
# headers = "h1, h2, h3"

# f.write(headers)

for teacher in teachers:
	name = name.


	# f.write() #writes headers.

# f.close()