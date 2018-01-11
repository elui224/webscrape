# webscrape
The script, entirewebscrape.py, scrapes multiple public school websites for staff information.
These information are saved in multiple .csv files -- one .csv file per school.

An additional script, csvtosql.py, inserts the information in the .csv files into a MySQL database.

# Steps
1. A list of tuples is created. Each item of the list represents a school and its website URL. The file is directory.py.
2. The process scrapes one website URL, which is contained in webscrape.py, to get name and email information.
3. The file entirewebscrape.py puts these steps together.
