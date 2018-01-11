
'''
The script combines functions from webscrape.py and
directory.py to scrape information in all the links 
in the school directory. This is the main file to run the scrape.
'''

filedir = 'school_files' #name of folder to save files

if __name__ == '__main__': #prevents script from executing if this file is imported elsewhere. Only runs on direct execution.
	import time
	from directory import getSchools
	from webscrape import (
		get_soup_object,
		make_directory,
		logic_school,
		)
	full_school_directory = 'http://www.montgomeryschoolsmd.org/directory/schools.aspx' #url holds school staff directory. 
	all_schools = getSchools(full_school_directory) #This function parses the school directory to return a list of tuples of schools and URL.
	# tot_schools = all_schools[0:2] #change this based on how many items in list to iterate through.
	tot_schools = all_schools
	start_time = time.time()

	print("Printing: " + str(len(tot_schools)) + " schools...")
	for x, y in tot_schools: #x, y unpacks the tuple in the list all_schools.
		school_name = ''
		teachers = ''
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
			f.write("\n" + school.replace(',',' ') + "," + teacher_name.replace(',',' ') + "," + title.replace(',',' ') + "," + email.replace(',',' ') + "," + time.strftime("%m/%d/%Y") + "," + concat_name)

		f.close()

	time.sleep(2) #Waits for 2 seconds before starting next iteration to prevent bottleneck.

	print("Done!")
	print("--- %s seconds ---" % round(time.time() - start_time, 2) )

