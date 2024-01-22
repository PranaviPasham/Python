import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Bhavik2911", database="python")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchall()

r1 = mycursor.fetchone()

print(r1)

for i in result:
    print(i)