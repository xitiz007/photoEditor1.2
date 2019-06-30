import mysql.connector
connect = mysql.connector.connect(host="localhost",user="root",passwd="aezakmi",database="students")
cursor = connect.cursor()
cursor.execute("select * from studentsinfo")
for i in cursor:
    print(i)