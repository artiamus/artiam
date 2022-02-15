import json

py_data = {
    'Vards':'Xingqui',
    'Vecums':96,
    'Dzivs':True,
    'Nedzivs':False,
    'Berni':('Xiangling','Xingyang'),
    'Dzivnieki':None,
    'Masinas':[
        {'Modelis':'Nissan GTR','Gads':2002},
        {'Modelis':'Toyota 69','Gads':1996}
    ]
}

print(json.dumps(py_data, indent=4, separators=(',',':')))

fileja = open('jsonchiks.json','w',encoding='utf-8')
json.dump(py_data,fileja,indent=4, ensure_ascii=False)
fileja.close()

fileja = open('jsonchiks.json','r',encoding='utf-8')
json_dati = json.load(fileja)

#vardnicas garums
print(len(json_dati))

#Visas atslegas
print(json_dati.keys())

#Visas vertibas
print(json_dati.values())

#Parbaudi, vai dota atslega ir vardnica un izvadi tas vertibu
atslega = 'Dzivs'

for key in json_dati:
    if key == atslega:
        print(json_dati[key])

#Nodefinet funkciju, kura ka argumentus izmantos datnes nosaukumu un atslegas nosaukumu
#jaizvada atslegas vertiba
def funkcija(datnes_name,key_name):
    for key in datnes_name.keys():
        if key == key_name:
            print(datnes_name[key_name])
            return
        else:
            break
    print(f'Nav atslegas')

funkcija(json_dati,'Vards')