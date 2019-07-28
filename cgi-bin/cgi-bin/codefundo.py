# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:35:14 2018

@author: Radhikesh
"""
import datetime
import pickle
from sklearn.cross_validation import train_test_split
#from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\Mahe\Downloads\database.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['dat'], df['year'], df['month'] = df['Date'].dt.day, df['Date'].dt.year, df['Date'].dt.month
df
#datee = datetime.datetime.strptime('Date', "%d/%m/%Y")
#ans = datee.year()
#print(ans)
#print(df.head())
feature_cols = ['Latitude','Longitude','month','year','dat']
x = df[feature_cols]
a = x.head(23412)
t = df.Magnitude[1]
"""print(a.shape)"""
i = 0

#df['abc'] = int(df['Magnitude'])
for item in df.Magnitude:
    df.loc[i, 'c1'] = int(item)
    
    i = i+1
y = df['c1']
b = y.head(23412)

"""print(b.shape)"""
#x = data[]
X_train, X_test, y_train, y_test = train_test_split(a,b,test_size = 0.2,random_state = 7)
knn = KNeighborsClassifier(n_neighbors = 2)
knn.fit(X_train,y_train)
y_ans = knn.predict(X_test)
#print(metrics.accuracy_score(y_test,y_ans))

filename = 'knn_final.sav'
pickle.dump(knn, open(filename, 'wb'))
 
# some time later...
 
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)

#print(df.head())
"""linreg = LinearRegression()

linreg.fit(X_train,y_train)

y_pred = linreg(X_test)

print(np.sqrt(metrics.mean_squared_error(y_test,y_pred)))"""
