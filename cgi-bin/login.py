import sqlite3

conn = sqlite3.connect("login.db")
conn.execute("CREATE TABLE LOGIN(FNAME TEXT,LNAME TEXT,EMAIL TEXT,PASSWORD TEXT,SECURITYQ TEXT,SECURITYA TEXT)")
conn.close()

