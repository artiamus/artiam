import random
import sqlite3

while True:
    variants = ['1', '2', '3']
    a = input("izvelies varianu 1(papirs), 2(skeres), 3(akmens): ")
    randoms = random.choice(variants)
    if a == '1' and randoms == '1':
        print("vienads")
        b = input("spelet velreiz[ja] [ne]")
        if b == "ja":
            pass
        else:
            break
    elif a == '1' and randoms == '2':
        print("zaudeji")
        b = input("spelet velreiz[ja] [ne]")
        if b == "ja":
            pass
        else:
            break
    elif a == '1' and randoms == '3':
        print("uzvara")
        b = input("spelet velreiz[ja] [ne]")
        if b == "ja":
            pass
        else:
            break        
    elif a == '2' and randoms == '1':
        print("uzvara")
        b = input("spelet velreiz[ja] [ne]")
        if b == "ja":
            pass
        else:
            break
    elif a == '2' and randoms == '2':
        print("vienads")
        b = input("spelet velreiz[ja] [ne]")
        if b == "ja":
            pass
        else:
            break
    elif a == '2' and randoms == '3':
        print("vienads")
        b = input("spelet velreiz[ja] [ne]")
        if b == "ja":
            pass
        else:
            break
    elif a == '3' and randoms == '1':
        print("zaudeji")
        b = input("spelet velreiz[ja] [ne]")
        if b == "ja":
            pass
        else:
            break
    elif a == '3' and randoms == '2':
        print("uzvara")
        b = input("spelet velreiz[ja] [ne]")
        if b == "ja":
            pass
        else:
            break
    elif a == '3' and randoms == '3':
        print("vienads")
        b = input("spelet velreiz[ja] [ne]")
        if b == "ja":
            pass
        else:
            break
    else:
        print("kluda")
while True:

    vecums = input("Ievadi savu vecumu:")
    if vecums.isdigit() == True:
        break
    else:
        continue

print(vecums)


while True:
    vards = input("Ievadi savu vārdu:")

    if vards.strip() == "":
        print(vards)
        continue
    else:
        break

print(vards)

db = sqlite3.connect("test.db")

db.execute("""CREATE TABLE IF NOT EXISTS test
    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    vards TEXT NOT NULL,
    vecums INT NOT NULL
)""")

db.execute("""INSERT INTO test
    (vards,vecums)
    VALUES (:vards,:vecums)
""",{'vards':vards,'vecums':vecums})

db.commit()