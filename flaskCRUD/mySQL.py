import mysql.connector
#  mysql -h localhost -u root
dbconn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="facerecognition"

)

mycursor = dbconn.cursor()
if (dbconn):
    print("DB successfull")
else:
    print("DB not successfull")
