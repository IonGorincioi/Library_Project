import mysql.connector
mydb = mysql.connector.connect(host ="localhost",
                               user = "root",
                               passwd = "Gsandanat.1")

#   create a cursor
my_cursor = mydb.cursor()

#   create the database
my_cursor.execute("CREATE DATABASE books")

#   show the database to make sure it was created
my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)