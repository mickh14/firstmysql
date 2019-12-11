import os
import pymysql

#Get username from Workspace
# (should be modified if running from another machine)
username = os.getenv('C9_USER')

#connect to DB
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close connection
    connection.close()
                                         
