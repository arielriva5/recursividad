capital=float(input("ingrese el total para la capital: "))

años=int(input("los años que se acomularan antes de retirar: "))

intereses=int(input("los intereses por año: "))

for i in range(años):
 capital = capital*( 1 + intereses/100)
 

print("la capital total con los interese son: ",capital)

