import os

os.system("cls")

# range es un rango, en este caso 0,1,2
# range(n)=0,1,2.....(n-1)
print(range(3))

# en este ciclo la variable k adopta
# cada uno de los valores del rango
for k in range(3):
    print(k, end=" ")
    
# Creamos una lista
lista = ["A","B","C"]    
for k in lista:
    print(k, end=" ")   #--> cada elemento de la lista
    
# vamos a recorrer a 2 variables
print("\n vamos a recorrer la lista enumerando")
for pos, valor in enumerate(lista):
    print(f" {pos} --> {valor}") 
    
    