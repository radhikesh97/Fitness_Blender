#!C:\Users\Mahe\Anaconda3\python.exe
import os
import cgi,cgitb

#print(os.environ)
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>OS</title>")
print("</head>")
print("<body>")
print("<h1>%s</h1>"%(os.environ['SERVER_NAME']))
print("<h1>%s</h1>"%(os.system('ls')))

print("</body>")
print("</html>")
