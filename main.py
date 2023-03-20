import sqlite3

db = sqlite3.connect('city.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS streets(
    id integer,
    name text
)""")

sql.execute("INSERT INTO streets VALUES('1','Mira')")
sql.execute("INSERT INTO streets VALUES('2','Sovetska')")
sql.execute("INSERT INTO streets VALUES('3','Truda')")
sql.execute("INSERT INTO streets VALUES('4','Proizvodstvenna')")
sql.execute("INSERT INTO streets VALUES('5','3 Stroitelei')")


db.commit()

db.close()