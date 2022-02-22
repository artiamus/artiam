import json
from operator import truediv
while True:
    vardss = input('ievadiet vardu: ')
    if vardss.strip() == "" or vardss.isdigit() == True:
        print("ievadi velreiz")
    else:
        break
while True:
    uzvardss = input('ievadiet uzvardu: ')
    if uzvardss.strip() == "" or uzvardss.isdigit() == True:
        print("ievadi velreiz")
    else:
        break
while True:
    vecumss = input('ievadiet vecumu:')
    if len(vecumss) <1 or len(vecumss) >3 or vecumss.isdigit() == False:
        continue
    else:
        break
while True:
    tell = input('ievadiet telefona numuru: ')
    if len(tell) <8 or tell.isdigit() == False or len(tell) >8:
        continue
    else:
        break

vardnica = {}
vardnica[vardss] = {
    'Uzvards':uzvardss,
    'Vecums':vecumss,
    'Telefona Numurs':tell
}

with open("ievaktieDati.json", "r", encoding="utf-8") as fails:
    json_data = json.load(fails)

    ir_saraksta = False
    for key in json_data.keys():
        if key == vardss:
            break
        if key != vardss:
            ir_saraksta = True

if ir_saraksta== False:
    print('Vards ir saraksta')
else:
    json_data[vardss]=vardnica

def dati(vards,uzvards,vecums,tel):
    with open('ievaktieDati.json','w',encoding='utf-8') as file:
        json.dump(json_data,file,indent=4,ensure_ascii=False)
        
dati(vardss,uzvardss,vecumss,tell)
