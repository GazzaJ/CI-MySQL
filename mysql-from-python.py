import os
import datetime
import pymysql

#Gets Usernamer from the workspace
username = os.getenv('C9_USER')

#Connect to the Database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

#Run a query
try:
    with connection.cursor() as cursor:
        rows = [("Bob", 30, "1990-02-06 23:05:00"), 
              ("Jim", 49, "1971-03-01 15:30:25"),
              ("Fred", 40, "1980-09-04 07:30:00")]        
        cursor.executemany("INSERT INTO Friends VALUES(%s, %s, %s);", rows)
        connection.commit()
#Close the connection
finally:
    connection.close()
