#!C:\Users\Mahe\AppData\Local\Programs\Python\Python36-32\python.exe

import cgi,cgitb

import json
form = cgi.FieldStorage()
age = int(form.getvalue('age1'))
gender = form.getvalue('ip')
height = float(form.getvalue('uheight'))
weight = float(form.getvalue('uweight'))
op = form.getvalue('sel')

if(gender == 'male'):
    ree = 10*weight + 6.25*height-5*age+5
    if(op == 'sed'):
        tdee = ree*1.2
    elif(op == 'light'):
        tdee = ree*1.375
    elif(op == 'mod'):
        tdee = ree*1.55
    elif(op == 'ext'):
        tdee = ree*1.725
else:
    ree = 10*weight + 6.25*height-5*age-161
    if(op == 'sed'):
        tdee = ree*1.2
    elif(op == 'light'):
        tdee = ree*1.375
    elif(op == 'mod'):
        tdee = ree*1.55
    elif(op == 'ext'):
        tdee = ree*1.725
w = weight
w = w * 2.20462
prog = w*0.825
proc = prog*4
fatc = tdee*0.25
fatg = fatc/9
carc = tdee - proc -fatc
carg = carc/4
ur = "C:/Apache24/htdocs/forest.jpg"
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello</title>")
print("</head>")
print("<body background="+ur+">")
print("<h1 style="+"color:yellow;"+">REE: %s </h1>"%(ree))
print("<h1 style="+"color:yellow;"+">TDEE: %s </h1>"%(tdee))
print("<h1 style="+"color:yellow;"+">Protein: %s gm</h1>"%(prog))
print("<h1 style="+"color:yellow;"+">Fat: %s gm</h1>"%(fatg))
print("<h1 style="+"color:yellow;"+">Carbohydrate: %s gm</h1>"%(carg))
print("<h1 style="+"color:yellow;"+">Protein: %s cal</h1>"%(proc))
print("<h1 style="+"color:yellow;"+">Fat: %s cal</h1>"%(fatc))
print("<h1 style="+"color:yellow;"+">Carbohydrate: %s cal</h1>"%(carc))
print("</body>")
print("</html>")

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
