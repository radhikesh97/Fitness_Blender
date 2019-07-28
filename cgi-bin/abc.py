#!C:\Users\Mahe\Anaconda3\python.exe
import cgi,cgitb
import sqlite3
import json
form = cgi.FieldStorage()
conn = sqlite3.connect("login.db")
name = form.getvalue('uname')
password = form.getvalue('upass')

#cursor = conn.execute("SELECT EMAIL,PASSWORD,FNAME,LNAME FROM LOGIN WHERE EMAIL = 'radhikesh1997@gmail.com'")
cursor = conn.execute("SELECT EMAIL,PASSWORD,FNAME,LNAME FROM LOGIN WHERE EMAIL = ?",(name,))
'''c = 0
for i in cursor:
    c = c + 1
print(c)'''
row = cursor.fetchone()
#print(row)
if(row == None):
    redirectURL = "http://localhost/login.html"
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >') 
    print('</head>')
    print('</html>')
else:
    #row = cursor.fetchone()

    ans="{\"First\" "+": \""+row[2]+"\","+" \"Last\""+": \""+row[3]+"\"}" 
    #ans = {"First":str(row[2]),"Last":str(row[3])}
    ans = json.loads(ans)
    #json_string = json.dumps(ans)
    with open('C:/Apache24/htdocs/JSONData.json', 'w') as f:
        json.dump(ans, f)


    if (row[1] != password):
        redirectURL = "http://localhost/login.html"
        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >') 
        print('</head>')
        print('</html>')
    else:
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
    print("<h1>Hello %s </h1>"%(name))
    print("</body>")
    print("</html>")"""
    
    """result = {"fn":str(row[2]),"ln":str(row[3])}
    data = json.dumps(result)
    redirectURL = "http://localhost/mainpage.html"
    print('<html>')
    print('<head>')
    print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >') 
    print('</head>')
    print('</html>')"""
conn.close()
