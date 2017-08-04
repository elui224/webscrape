import bs4
from urllib.request import urlopen as urlreq
from bs4 import BeautifulSoup as soup
import os

my_url = 'http://www.montgomeryschoolsmd.org/directory/directory_Boxschool.aspx?processlevel=04757'
school_name = 'Montgomery_Blair'


#Open connection, download page.
#or uClient = urllib.request.urlopen(my_url)
urlclient = urlreq(my_url)

#puts content into a variable.
page_html = urlclient.read()

#close connection.
urlclient.close()

#stores page HTML into variable. HTML parse.
page_soup = soup(page_html, "html.parser")

# container = page_soup.find(id="ctl00_ContentPlaceHolder1_pnlStructure")

#Finds section with teacher information on the page. stores in variable.
teachers = page_soup.find_all("ul", "box-one-light")

filedir = 'school_files' #name of folder

if not os.path.exists(filedir):
	os.makedirs(filedir)

filename = str(school_name)+ "_Teachers.csv" #name of file
complete_name = os.path.join(filedir, filename) #save location.

f = open(complete_name, "w")


headers = "school, teacher_name, title, email"

f.write(headers)

for teacher in teachers:
	school = school_name.replace('_', ' ')

	teacher_name = teacher.li.h3.string.replace(u'\xa0', u' ').split(',') #puts name in comma separated list.
	teacher_name.reverse() #reverses order of the list. [jones, mike] --> [mike, jones]
	teacher_name = ' '.join(teacher_name).rsplit('.', 1)[-1].strip() #converts list to Mike Jones. Trims white space.

	title = teacher.find_all('p')[0].getText()
	email = teacher.find_all('p')[1].getText()

	# print(school)
	# print(teacher_name)
	# print(title)
	# print(email)

	f.write("\n" + school + "," + teacher_name + "," + title.replace(',',' ') + "," + email)


f.close()
