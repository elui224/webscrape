import pymysql
import csv
import os
from entirewebscrape import filedir

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='thel123', db='teachers')
cursor = conn.cursor() 

basedir = os.path.join(os.path.abspath('.'), filedir) #/Users/ericlui/Documents/webscrape/school_files
list_sch_files = os.listdir(os.path.join(os.path.abspath('.'), filedir)) #puts all files of directory in a list.

for csvfile in list_sch_files:
	if csvfile.endswith('.csv'):
		complete_name = os.path.join(basedir, csvfile)
		with open(complete_name, 'r') as csviterate:
			reader = csv.reader(csviterate, delimiter=',')
			next(reader) #skips header.
			for row in reader:
				cursor.execute("INSERT INTO teachers(school, teacher_name, title, email, upd_dt, concat_name) VALUES(%s, %s, %s, %s, %s, %s)", row)
 

# close the connection to the database.
conn.commit()
cursor.close()

