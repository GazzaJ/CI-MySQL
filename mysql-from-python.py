import os
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
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
#Close the connection
finally:
    connection.close()
