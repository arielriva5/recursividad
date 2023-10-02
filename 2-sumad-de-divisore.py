print("ingrese un número, y para acabar uno negativo:")
num=int( input("num: "))
while num>0:
    Suma=0
    for i in range(num):
       if num % i==0 :
        Suma=Suma+i
print("la suma de los divisores del número es:", Suma)