import mysql.connector as db
a=db.connect (host="localhost",user="root",password="root",database="don")
if a.is_connected():
    print('ok')
