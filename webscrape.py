import bs4
from urllib.request import urlopen as urlreq
from bs4 import BeautifulSoup as soup
import os


'''
ReadMe:
Define URL, file directory, and school name here.
The script should be run once for each school.
'''
# my_url = 'http://www.montgomeryschoolsmd.org/directory/directory_Boxschool.aspx?processlevel=04757'
filedir = 'school_files' #name of folder to save files
element = "ul" 
element_name = "box-one-light"
# root_url = 'http://www.montgomeryschoolsmd.org/directory/directory_Boxschool.aspx?processlevel='
# school_url = 'http://www.montgomeryschoolsmd.org/directory/schools.aspx'

def get_soup_object(my_url):
	'''
	Returns a beautifulsoup object, HTML-parsed.
	Need to figure out a way to iterate 
	through multiple url patterns.
	'''
	#or uClient = urllib.request.urlopen(my_url)
	urlclient = urlreq(my_url)
	page_html = urlclient.read()
	urlclient.close()

	#stores page HTML into variable. HTML parse.
	page_soup = soup(page_html, "html.parser").find_all(element, element_name) #This line likely needs to change based on website HTML.
	return page_soup


def make_directory(filedir, school_name):
	if not os.path.exists(filedir):
		os.makedirs(filedir)

	filename = str(school_name.replace('.', '').replace(',', '').replace('-', '').replace(' ', '_'))+ "_Teachers.csv" #name of file
	complete_name = os.path.join(filedir, filename) #save location.
	return complete_name


def logic_school(school_name, teacher):
	'''
	Each school will need different logic.
	'''	
	school = school_name.replace('_', ' ')

	teacher_name = teacher.li.h3.string.replace(u'\xa0', u' ').split(',') #puts name in comma separated list.
	teacher_name.reverse() #reverses order of the list. [jones, mike] --> [mike, jones]
	teacher_name = ' '.join(teacher_name).rsplit('.', 1)[-1].strip() #converts list to Mike Jones. Trims white space.

	title = teacher.find_all('p')[0].getText()
	email = teacher.find_all('p')[1].getText()
	concat_name = email.replace('_', '').replace('.org', '').split('@', 1)[0].upper()
	return school, teacher_name, title, email, concat_name


# def scrape():
# 	f = open(make_directory(), "w")
# 	headers = "school, teacher_name, title, email, upd_dt, concat_name"
# 	f.write(headers)
	
# 	teachers = get_soup_object() #Finds section with teacher information on the page. stores in variable.

# 	for teacher in teachers:
		
# 		school, teacher_name, title, email, concat_name = logic_school(teacher) #Need to change the function

# 		f.write("\n" + school + "," + teacher_name + "," + title.replace(',',' ') + "," + email + "," + time.strftime("%m/%d/%Y") + "," + concat_name)

# 	f.close()

# scrape()

