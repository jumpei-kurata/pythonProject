import sqlite3

import conda_build.post

# conn = sqlite3.connect('test_sqlite.db')
conn = sqlite3.connect(':memory:')

curs = conn.cursor()

curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("Mike")'
)
conn.commit()

curs.execute('SELECT * FROM persons')
print(curs.fetchall())

curs.execute(
    'INSERT INTO persons(name) values("Nancy")')
curs.execute(
     'INSERT INTO persons(name) values("Jun")')
conn.commit()

curs.execute('UPDATE persons set name= "MICHEL" WHERE name = "Mike"')
conn.commit()

curs.execute('DELETE FROM persons WHERE name = "MICHEL"')
conn.commit()

curs.execute('SELECT * FROM persons')
print(curs.fetchall())
conn.close()