import sqlite3

db = sqlite3.connect('test.db')

#db.execute('''CREATE TABLE edienkarte
#    (id     INT     PRIMARY KEY     NOT NULL,
#   nosaukums   TEXT    NOT NULL,
#  cena    REAL    NOT NULL,
# alergeni CHAR(50),
#    );
#    ''')

#db.execute("""INSERT INTO edienkarte
#            (id, nosaukums, cena, alergeni)
#            VALUES (4, 'kartupeli',0.5,'')
#""")

#db.commit()

dati = db.execute("SELECT * FROM edienkarte WHERE cena > 0.5")
rezultats = dati.fetchall()

print(rezultats)

db.close()