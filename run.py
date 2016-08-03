import math
def mantysa(x):
    mantysa = ''
    while(x<1):
        x*=2
        if x < 1:
            mantysa = mantysa+'0'
        elif x >= 1:
            mantysa = mantysa+'1'
            x = float('0' + str(x)[1:])
        if len(mantysa) > 51:
            break
    return mantysa
            
x = eval(input("Podaj liczbe:"))
p = int((math.log(abs(x),2)))
cz_u = float('0.' + str(x / math.pow(2,p))[2:])
b = ''
if x > 0:
    b = b + '0' + bin(1023+p)[2:] + mantysa(cz_u)
elif x < 0:
    b = b + '1' + bin(1023-p)[2:] + mantysa(cz_u)
else:
    b = '0'

print(b)
