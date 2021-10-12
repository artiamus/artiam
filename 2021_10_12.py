def vards(a, b):
    if a[0] == b[0]:
        return (True)
    else:
        return (False)
print (vards("liela", "dama"))
def vards2(a):
    a = a.split()
    if a[0][0] == a[1][0]:
        return True
    else:
        return False
print (vards2("liela lama"))