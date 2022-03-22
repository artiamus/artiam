import random
import json
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
        continue
    else:
        break

print(vecums)


while True:
    vards = input("Ievadi savu vārdu:")

    if vards.strip() == "":
        print(vards)
        continue
    else:
        break

print(vards)

with open("ievaktieDati.json","r", encoding="utf-8") as fails:
    json_data = json.load(fails)

db = sqlite3.connect("test.db")

dati = db.execute("Vecums * FROM Vārds")
for rinda in dati:
    print("Vecums:", rinda[0])
    print("Vārds:", rinda[1], "/n")

db.close()