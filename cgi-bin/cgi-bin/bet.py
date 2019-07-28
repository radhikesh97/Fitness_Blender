#!C:\Users\Mahe\Anaconda3\python.exe
from datetime import datetime
from dateutil.parser import parse
import pandas as pd
import pickle
import cgi,cgitb
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np
import json

form = cgi.FieldStorage()
lat = form.getvalue('Latitude')
lon = form.getvalue('Longitude')
da = form.getvalue('Date')
#da='05-23-1999'
redirectURL = "http://localhost/htdocs/home.html"

y = datetime.strptime(da, '%Y-%m-%d')
month=y.month
day = y.day
year = y.year
filename = 'knn_final.sav'
knn = KNeighborsClassifier(n_neighbors = 2)
loaded_model = pickle.load(open(filename, 'rb'))
X_test = pickle.load(open("xtest.sav", 'rb'))
Y_test = pickle.load(open("ytest.sav", 'rb'))
user = [[lat,lon,month,year,day]]
y_ans = loaded_model.predict(user)
accuracy = loaded_model.score(X_test,Y_test)

ans = {"Magni":str(y_ans),"Accuracy":str(accuracy)}
json_string = json.dumps(ans)


print ("Content-type:text/html\r\n\r\n")
print('<html>')





print('<head>')
#print('''<meta charset="UTF-8"> <title>Vertical Layout with Navigation</title> <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css"><link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet"> <meta name="viewport" content="width=device-width"> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css"> <link rel="stylesheet" href="css/style.css">''')
print('<meta http-equiv="Refresh" content="0;url='+str(redirectURL)+'" >') 
print('</head>')
print('<body>')
"""print('''
  <nav class="nav">
  <div class="burger">
    <div class="burger__patty"></div>
  </div>

  <ul class="nav__list">
    <li class="nav__item">
      <a href="#1" class="nav__link c-blue"><i class="fa fa-camera-retro"></i></a>
    </li>
    <li class="nav__item">
      <a href="#2" class="nav__link c-yellow scrolly"><i class="fa fa-bolt"></i></a>
    </li>
  </ul>
</nav>

<section class="panel b-blue" id="1">
  <article class="panel__wrapper">
    <div class="panel__content">
      <h1 class="panel__headline"><i class="fa fa-camera-retro"></i>&nbsp;THE RESULTS</h1>
      <div class="panel__block"></div>
      <span> Magnitude: </span>''' + str(y_ans))
      
print(''' <br>    <span> Accuracy: </span> +'''+ str(accuracy))
print(''' <br>   </div>
  </article>
</section>
<section class="panel b-yellow" id="2">
  <article class="panel__wrapper">
    <div class="panel__content">
      <h1 class="panel__headline"><i class="fa fa-bolt"></i>&nbsp;WHAT DO YOU DO?</h1>
      <div class="panel__block"></div>

      <ul >
        <li>
          Drop down,take cover under a desk or table and hold on
        </li>
        <li>
          Stay indoors until the shaking stops and you're sure it's safe to exit.
        </li>
      </ul>

    </div>
  </article>
<a href="http://ettrics.com/code/vertical-layout-navigation/" class="logo" target="_blank">
 <img class="logo" src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/45226/ettrics-logo.svg" alt="" />
</a>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>



    <script  src="js/index.js"></script>
 ''')"""
with open('JSONData.json', 'w') as f:
     json.dump(json_string, f)
print(json_string)
print('</body>')
print('</html>')
#lat = 5
#lon = 6
