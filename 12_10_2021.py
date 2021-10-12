def skaitlis(a, b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a, b)
print (skaitlis(2, 4))