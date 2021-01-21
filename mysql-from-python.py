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
        rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Bob')
        connection.commit()
#Close the connection
finally:
    connection.close()
