try:
    f = open('testfile', 'r')
    f.write('Tests')
except IOError:
    print("Error: Fails netika atrasts vai nevar tikt tam")
else:
    print("Viss sanaca!")
    f.close()

try:
    f = open('testfile', 'a')
    f.write('Tests 3')
    f.close()
finally:
    print("yay")

def askint():
    while True:
        try:
            val = int(input("Ievadi skaitli:"))
        except:
            print("Izskatas, ka tas nav skaitlis")
            val = int(input("Ievadi skaitli:"))
            continue
        else:
            print("Ja, tas ir skaitlis!")
            break
        finally:
            print("Es vienmer esmu seit")
            print(val)
    
askint()
