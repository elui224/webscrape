import bs4
from urllib.request import urlopen as urlreq
from bs4 import BeautifulSoup as soup
import os
import time
# import pymysql
# import pandas

# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='thel123', db='teachers')

'''
ReadMe:
Define URL, file directory, and school name here.
The script should be run once for each school.
'''
my_url = 'http://www.montgomeryschoolsmd.org/directory/directory_Boxschool.aspx?processlevel=04757'
filedir = 'school_files' #name of folder to save files
school_name = 'Montgomery_Blair'
element = "ul" 
element_name = "box-one-light"

def get_soup_object():
	'''
	Returns a beautifulsoup objected, HTML-parsed.
	Need to figure out a way to iterate 
	through multiple url patterns.
	'''
	#or uClient = urllib.request.urlopen(my_url)
	urlclient = urlreq(my_url)
	page_html = urlclient.read()
	urlclient.close()

	#stores page HTML into variable. HTML parse.
	page_soup = soup(page_html, "html.parser").find_all(element, element_name)
	return page_soup


def make_directory():
	if not os.path.exists(filedir):
		os.makedirs(filedir)

	filename = str(school_name)+ "_Teachers.csv" #name of file
	complete_name = os.path.join(filedir, filename) #save location.
	return complete_name


def logic_montgomery_blair(teacher):
	'''
	Each school will need different logic.
	'''	
	school = school_name.replace('_', ' ')

	teacher_name = teacher.li.h3.string.replace(u'\xa0', u' ').split(',') #puts name in comma separated list.
	teacher_name.reverse() #reverses order of the list. [jones, mike] --> [mike, jones]
	teacher_name = ' '.join(teacher_name).rsplit('.', 1)[-1].strip() #converts list to Mike Jones. Trims white space.

	title = teacher.find_all('p')[0].getText()
	email = teacher.find_all('p')[1].getText()
	return school, teacher_name, title, email


def scrape():
	f = open(make_directory(), "w")
	headers = "school, teacher_name, title, email, upd_dt"
	f.write(headers)
	
	teachers = get_soup_object() #Finds section with teacher information on the page. stores in variable.

	for teacher in teachers:
		
		school, teacher_name, title, email = logic_montgomery_blair(teacher) #Need to change the function

		f.write("\n" + school + "," + teacher_name + "," + title.replace(',',' ') + "," + email + "," + time.strftime("%m/%d/%Y"))

	f.close()

scrape()
