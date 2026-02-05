def add(a, b, plus=0): # Here a and b are parameters
    x= a + b + plus
    return x


c=add(3, 5, 2) # Here 3 and 5 are arguments
print(c)

c1=add(b=5, a=3)