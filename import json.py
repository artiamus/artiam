import json

kopa = {}
def jason(nam1,nam2):
    f1 = open(nam1, 'r',encoding='utf-8')
    f2 = open(nam2, 'r',encoding="utf-8")
    a = json.load(f1)
    b = json.load(f2)
    kopa['uwu'] = a
    kopa['uwu1'] = b
    f1.close()
    f2.close()
    f3 = open('bebra.json','w',encoding='utf-8' )
    json.dump(kopa,f3,indent=4)


jason('pirmaisJson.json','otraisJson.json')

