import pymysql
import csv
import os
import time
from entirewebscrape import filedir

start_time = time.time()
print("Inserting records into database.")
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='thel123', db='teachers') #mySQL DB conneciton object.
cursor = conn.cursor() 

basedir = os.path.join(os.path.abspath('.'), filedir) #/Users/ericlui/Documents/webscrape/school_files
list_sch_files = os.listdir(os.path.join(os.path.abspath('.'), filedir)) #puts all files of directory in a list.

for csvfile in list_sch_files:
	if csvfile.endswith('.csv'):
		complete_name = os.path.join(basedir, csvfile)
		print(complete_name)
		with open(complete_name, 'r') as csviterate:
			reader = csv.reader(csviterate, delimiter=',')
			next(reader) #skips header.
			for row in reader:
				cursor.execute("INSERT INTO teachers(school, teacher_name, title, email, upd_dt, concat_name) VALUES(%s, %s, %s, %s, %s, %s)", row)
 

# close the connection to the database.
conn.commit()
cursor.close()

print("Done!")
print("--- %s seconds ---" % round(time.time() - start_time, 2) )