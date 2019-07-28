#!C:\Users\Mahe\Anaconda3\python.exe
import cgi,cgitb
import sqlite3
conn = sqlite3.connect("login.db")
cursor = conn.execute("SELECT FNAME,LNAME FROM LOGIN")

ur = "C:/Apache24/htdocs/forest.jpg"
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('</head>')
print("<body background="+ur+">")
for row in cursor:
    print("<h1 style="+"color:yellow;"+"> %s %s</h1>"%(row[0],row[1]))
print("</body>")
print("</html>")
print('</html>')
conn.close()