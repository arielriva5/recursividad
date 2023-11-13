inicio=2
limite=1000
primos=0

for i in range(inicio,limite):
    primo=True
    j=2
    
    while (i>j)and(primo==True):
        if i%j==0:
            primo=False
            break
        else:
            j=j+1
            
    if primo==True:
       print(i," es un numero primo")
       primos=primos+1
        
        
print ("del 1 a 1000 hay un total de ",primos," numeros primos")