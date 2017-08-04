import pymysql
from webscrape import make_directory
import csv

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='thel123', db='teachers')

csvfile = make_directory()

cursor = conn.cursor() 

with open(csvfile, 'r') as csviterate:
	reader = csv.reader(csviterate, delimiter=',')
	next(reader)
	for row in reader:
		cursor.execute("INSERT INTO teachers(school, teacher_name, title, email, upd_dt) VALUES(%s, %s, %s, %s, %s)", row)
 
#close the connection to the database.
conn.commit()
cursor.close()
