import imp


import random

variants = ['1', '2', '3']
a = input("izvelies varianu 1(papirs), 2(skeres), 3(akmens): ")
randoms = random.choice(variants)
if a == '1' and randoms == '1':
    print("vienads")
elif a == '1' and randoms == '2':
    print("zaudeji")
elif a == '1' and randoms == '3':
    print("uzvara")
elif a == '2' and randoms == '1':
    print("uzvara")
elif a == '2' and randoms == '2':
    print("vienads")
elif a == '3' and randoms == '1':
    print("zaudeji")
elif a == '3' and randoms == '2':
    print("uzvara")
elif a == '3' and randoms == '3':
    print("vienads")
else:
    print("kluda")