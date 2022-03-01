import json
def kont_mekl():
    mekl_vards = input('Name Searching: ')

    with open('ievaktieDati.json','r',encoding='utf-8') as fails:
        json_data = json.load(fails)

    for key in json_data.keys():
        if key == mekl_vards:
            dati = json_data[key]
            break
        else:
            dati = 'Nav Saraksta'
    return dati


#varda parbaude
def kont_add():

    while True:
        vardss = input('ievadiet vardu: ')
        if vardss.isdigit() == False:
            if vardss.strip() == '':
                print('ievadiet vardu atkartoti')
                continue
            else:
                break
        else:
            print('ievadiet vardu atkartoti')
            continue

            
    #uzvarda parbaude
    while True:
        uzvardss = input('ievadiet uzvardu: ')
        if uzvardss.isdigit() == False:
            if uzvardss.strip() == '':
                print('ievadiet uzvardu atkartoti')
                continue
            else:
                break
        else:
            print('ievadiet uzvardu atkartoti')
            continue

    #vecuma parbaude
    while True:
        vecumss = input('ievadiet vecumu: ')
        if vecumss.isdigit():
            break
        else:
            print('ievadiet vecumu atkartoti')
            continue
    #telefona numura parbaude
    while True:
        tell = input('ievadiet telefona numuru: ')
        if tell.isdigit():
            if len(tell) == 8:
                break
        else:
            print('ievadiet telefona numuru atkartoti')
            continue


    vardnica = {
        "Uzvārds":uzvardss,
        "Vecums":vecumss,
        "Telefona numurs":tell
    }

    kont_save(vardss,vardnica)

def kont_save(vardss,vardnica):

    with open("ievaktieDati.json","r", encoding="utf-8") as fails:
        json_data = json.load(fails)

        ir_saraksta = True
        for key in json_data.keys():
            if key == vardss:
                if not isinstance(json_data[vardss],list):
                    json_data[vardss] = [json_data[vardss]]
                json_data[vardss].append(vardnica)
                if_saraksta = True
                print('ir saraksta')
                break
            else:
                ir_saraksta = False

        if not ir_saraksta:
            print('nav saraksta')
            json_data[vardss]=vardnica


    with open("ievaktieDati.json","w", encoding="utf-8") as fails:
        json.dump(json_data,fails, indent = 4, ensure_ascii=False)

while True:
    print('\nIzvelies darbibu: ')
    print('1 - kontakta pievienosana')
    print('2 - kontakta meklesana')
    print('3 - iziet')
    izvele = input()

    if izvele == '1':
        kont_add()
    elif izvele == '2':
        print(kont_mekl())
    elif izvele == '3':
        exit()
    else:
        print('\nIzvelies kadu darbibu velreiz!')