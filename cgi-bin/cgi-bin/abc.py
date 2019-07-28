#!C:\Anaconda\python.exe

import cgi,cgitb

form = cgi.FieldStorage()
name = form.getvalue('ab')
print ("Content-type:text/html\r\n\r\n")


print("Hello" + str(name))