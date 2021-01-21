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
        list_of_names = ['Jim', 'Fred']
        format_strings = ",".join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({0});".format(format_strings), list_of_names)
        connection.commit()
#Close the connection
finally:
    connection.close()
