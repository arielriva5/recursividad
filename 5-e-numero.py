n=int(input("ingrese un numero: "))
e=1
num=1
den=1
i=1
num=n**i
den=den*i
i=i+1
e=e+num/den
while not (num/den < 0.000001):
    num=n**i
    den=den*i
    i=i+1
    e=e+num/den

print("e elevado al ",n," es: ",e)