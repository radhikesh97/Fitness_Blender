#!C:\Users\Mahe\AppData\Local\Programs\Python\Python36-32\python.exe
import sqlite3

conn = sqlite3.connect("login.db")
#conn.execute("DELETE FROM LOGIN")
cursor = conn.execute("SELECT * FROM LOGIN")
for row in cursor:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print(row[5])
    print()
#conn.commit()
conn.close()
