import os
os.system("cls")

# Esta lista va almacenar nombres de profesores
lista_profes = []  # --> lista vacia!!!

# vamos a almacenar 3 profesores
# RECORDEMOS--> range(3)=0,1,2
for k in range(3):
    lista_profes.append(str(input(f'''
    Ingrese nombre profesor {k+1}: ''')).upper())

print(lista_profes)

lista_profes.sort()  #--> ordenamos alfabeticamente
print(lista_profes)