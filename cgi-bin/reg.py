#!C:\Users\Mahe\Anaconda3\python.exe
import cgi,cgitb
import sqlite3
import json
form = cgi.FieldStorage()

fname = form.getvalue('fname')
lname = form.getvalue('lname')
email = form.getvalue('uname2')
password = form.getvalue('upass')
secq = form.getvalue('sel')
seca = form.getvalue('ans')

conn = sqlite3.connect("login.db")
conn.execute("INSERT INTO LOGIN VALUES(?,?,?,?,?,?)",(fname,lname,email,password,secq,seca))
conn.commit()
conn.close()
ans="{\"First\" "+": \""+fname+"\","+" \"Last\""+": \""+lname+"\"}" 
#ans = {"First":str(row[2]),"Last":str(row[3])}
ans = json.loads(ans)
#json_string = json.dumps(ans)
with open('C:/Apache24/htdocs/JSONData.json', 'w') as f:
     json.dump(ans, f)

redirectURL = "http://localhost/mainworkpage.html"
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >') 
print('</head>')
print('</html>')
"""print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello</title>")
print("</head>")
print("<body>")
print("<h1>Hello %s </h1>"%(fname))
print("</body>")
print("</html>")"""
