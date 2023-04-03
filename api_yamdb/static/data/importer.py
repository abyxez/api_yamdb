import csv
import sqlite3

con = sqlite3.connect("db.sqlite3")  # change to 'sqlite:///your_filename.db'
cur = con.cursor()

with open('titles.csv', 'r') as fin:  # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin)  # comma is default delimiter
    to_db = [(i['id'], i['name'], i['year'], i['category']) for i in dr]

cur.executemany("INSERT INTO reviews_title (id, name, year, category_id) "
                "VALUES (?, ?, ?,?);", to_db)
con.commit()
con.close()
