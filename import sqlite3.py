import sqlite3
import datetime
from tracemalloc import start

db = sqlite3.connect("titanicDB.db")

tabulu_nosaukumi = db.execute("SELECT name FROM sqlite_schema WHERE type = 'table';")

rezultats = tabulu_nosaukumi.fetchall()
print(rezultats)

kolonnu_nosaukumi = db.execute("""SELECT name FROM pragma_table_info('titanic')
""")

rezultats = kolonnu_nosaukumi.fetchall()
[print(rinda[0]) for rinda in rezultats]
for rinda in rezultats:
    print(rinda[0])


