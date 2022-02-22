import json
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
    if len(vecumss) <0 or len(vecumss) >100 or vecumss.isdigit() == False:
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

def dati(vards,uzvards,vecums,tel):
    with open('ievaktieDati.json','w',encoding='utf-8') as file:
        json.dump(vardnica,file,indent=4,ensure_ascii=False)
        

dati(vardss,uzvardss,vecumss,tell)


