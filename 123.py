pirmais = {'atsl1':'vert1', 'atsl2':'vert2'}
print (pirmais)
print (pirmais['atsl1'])
otrais = {'atsl1': [1, 2, 3], 'atsl2': 'tekts', 'atsl3':5}
print (otrais['atsl1'],otrais['atsl3'])
pirmais = {}
print (pirmais)
pirmdiena = {'stunda1':'latviesu', 'stunda2':'matematika', 'stunda3':'krievu'}
print (pirmdiena['stunda1'], pirmdiena['stunda2'], pirmdiena['stunda3'])
pirmdiena = {'stunda2':'matematika', 'stunda3':'krievu'}
pirmdiena['stunda1'] = {}
print (pirmdiena['stunda1'], pirmdiena['stunda2'], pirmdiena['stunda3'])
print (pirmdiena['stunda2'], pirmdiena['stunda3'])