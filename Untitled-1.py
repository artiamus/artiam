rec = {'cukurs':0.6, 'kanelis':0.008, 'aboli':2.0, 'udens':0.2}
cena = {'cukurs':0.75, 'kanelis':0.3, 'aboli':0.0, 'udens':0.0}
skaits = {'cukurs':0.6, 'kanelis':0.008, 'aboli':2.0, 'udens':0.1}
nauda = 10

a = input()
if a == 'a':
    print (skaits['cukurs'])
elif a == 'b':
    print (skaits['kanelis'])
elif a == 'c':
    print (skaits['aboli'])
elif a == 'd':
    print (skaits['udens'])
    input ("nopirkt udens?")
else:
    print("nepareizi")
print (skaits['udens'], rec['udens'])