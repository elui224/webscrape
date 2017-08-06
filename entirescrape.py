import time
from directory import getSchools
from webscrape import (
	get_soup_object,
	make_directory,
	logic_school,
	)

'''
The script combines functions from webscrape.py and
directory.py to scrape information in all the links 
in the school directory.
'''

full_school_directory = 'http://www.montgomeryschoolsmd.org/directory/schools.aspx' #url holds list of schools.
element = "ul" 
element_name = "box-one-light" #class name that holds teacher's information (name, title, email)
filedir = 'school_files' #name of folder to save files
school_name = ''
teachers = ''

all_schools = getSchools(full_school_directory) #This function parses the school directory to return a list of tuples of schools and URL.

start_time = time.time()

for x, y in all_schools[0:2]:
	school_name = x
	teachers = get_soup_object(y) #get html object for each individual school. Contains, name, title, email.
	print("Currently printing " + school_name)
	
	#creates and prepares csv file.
	f = open(make_directory(filedir, school_name), "w")
	headers = "school, teacher_name, title, email, upd_dt, concat_name"
	f.write(headers)

	#populates csv file with data.
	for teacher in teachers:
		school, teacher_name, title, email, concat_name = logic_school(school_name, teacher)
		f.write("\n" + school + "," + teacher_name + "," + title.replace(',',' ') + "," + email + "," + time.strftime("%m/%d/%Y") + "," + concat_name)

	f.close()

time.sleep(2) #Waits for 2 seconds before starting next iteration to prevent bottleneck.

print("--- %s seconds ---" % round(time.time() - start_time, 2) )

