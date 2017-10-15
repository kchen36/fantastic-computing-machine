import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)" )
c.execute("CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)" )

sfile = csv.DictReader(open("peeps.csv"))
cfile = csv.DictReader(open("courses.csv"))

for row in cfile:
    code = row['code']
    mark = row['mark']
    ids = row['id']
    c.execute('INSERT INTO courses VALUES (?,?,?)', (code,mark,ids) )

for row in sfile:
    name = row['name']
    age = row['age']
    ids = row['id']
    c.execute('INSERT INTO peeps VALUES (?,?,?)', (name,age,ids) )

db.commit() #save changes
db.close()  #close database
