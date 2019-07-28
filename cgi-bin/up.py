#!C:\Users\Mahe\AppData\Local\Programs\Python\Python36-32\python.exe
import sqlite3
import cgi,cgitb
import json
form = cgi.FieldStorage()
email = form.getvalue('fname')
sques = form.getvalue('sel')
sans = form.getvalue('ans')
pas = form.getvalue('lname')
cpas = form.getvalue('bname')


conn = sqlite3.connect('login.db')
#cursor =  conn.execute("SELECT * FROM LOGIN WHERE EMAIL = 'kaushal@gmail.com'")
cursor =  conn.execute("SELECT * FROM LOGIN WHERE EMAIL = ?",(email,))
c = 0
'''for i in cursor:
    c = c + 1
#print(cursor.rowcount)'''
row = cursor.fetchone()
#print(row)
if (row == None):
    redirectURL = "http://localhost/forgot.html"
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >') 
    print('</head>')
    print('</html>')


else:
    #row = cursor.fetchone()
    co = 0


    ans="{\"First\" "+": \""+row[0]+"\","+" \"Last\""+": \""+row[1]+"\"}" 
    #ans = {"First":str(row[2]),"Last":str(row[3])}
    ans = json.loads(ans)
    #json_string = json.dumps(ans)
    with open('C:/Apache24/htdocs/JSONData.json', 'w') as f:
        json.dump(ans, f)

    if(row[4] == sques and row[5] == sans):
        conn.execute("UPDATE LOGIN SET PASSWORD = ? WHERE EMAIL = ?",(pas,email,))
        conn.commit()
        redirectURL = "http://localhost/mainworkpage.html"
        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >') 
        print('</head>')
        print('</html>')
    #if((row[4] != sques and row[5] != sans) or (row[4] == sques and row[5] != sans) or (row[4] != sques and row[5] == sans)):
    else:
        redirectURL = "http://localhost/forgot.html"
        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >') 
        print('</head>')
        print('</html>')
conn.close()


"""if (row == None):
    redirectURL = "http://localhost/login.html"
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >') 
    print('</head>')
    print('</html>')
    
elif (row[1] != password):
    redirectURL = "http://localhost/login.html"
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >') 
    print('</head>')
    print('</html>')
else:
    print("Content-type:text/html\r\n\r\n")
    '''print("<html>")
    print("<head>")
    print("<title>Hello</title>")
    print("</head>")
    print("<body>")
    print("<h1>Hello %s </h1>"%(name))
    print("</body>")
    print("</html>")'''
    
    result = {"fn":str(row[2]),"ln":str(row[3])}
    data = json.dumps(result)
    redirectURL = "http://localhost/mainpage.html"
    print('<html>')
    print('<head>')
    print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >') 
    print('</head>')
    print('</html>')
conn.close()"""
