import csv, sqlite3

con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER, username TEXT, email TEXT, role TEXT, bio TEXT, first_name TEXT, last_name TEXT);") # use your column names here

with open('users.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['username'], i['email'], i['role'],i['bio'], i['first_name'], i['last_name']) for i in dr]

cur.executemany("INSERT INTO Users (id, username, email, role, bio, first_name, last_name) VALUES (?, ?, ?,?,?,?,?);", to_db)
con.commit()
con.close()