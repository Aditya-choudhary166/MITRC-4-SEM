import mysql.connector
conn=mysql.connector.connect(host='localhost',password='9079285970',user='root')
                             
if conn.is_connected():
         print("connection established")                    
