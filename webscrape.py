import bs4
from urllib.request import urlopen as urlreq
from bs4 import BeautifulSoup as soup
import os


'''
The functions contain the logic that needs
to be run once for each school.
'''

def get_soup_object(my_url):
	'''
	Returns a beautifulsoup object, HTML-parsed.
	Need to figure out a way to iterate 
	through multiple url patterns.
	'''
	element = "ul" 
	element_name = "box-one-light" #class name that holds teacher's information (name, title, email)
	try:
		#or uClient = urllib.request.urlopen(my_url)
		urlclient = urlreq(my_url)
		page_html = urlclient.read()
		urlclient.close()
	except Exception as e: 
		print(e.message)
		return #If url does not exist, it skips and continues with the program.	

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



