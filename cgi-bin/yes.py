#!C:\Users\Mahe\Anaconda3\python.exe
import cgi,cgitb

form = cgi.FieldStorage()
name = form.getvalue("abc")
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>"+name+"</h1>")
print("</body>")
print("</html>")