resto=0
n=int(input("Ingrese un numero "))
while (n>0):
	resto=n % 10
	
	n=n//10
	print(resto)