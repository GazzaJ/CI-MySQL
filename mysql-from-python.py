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
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (25, 'Fred')]                
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
        rows)
        connection.commit()
#Close the connection
finally:
    connection.close()
