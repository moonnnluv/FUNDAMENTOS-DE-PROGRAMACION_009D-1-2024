import os
os.system("cls")

# Una lista sirve para almacenar un grupo de datos

print("\n ----- ejemplo 1 --------")

# indice-----> 0            1         2
verduras = ["zanahoria", "tomate", "palta"]

# Podemos imprimir la lista como UN TODO
print(verduras)

# Tambien podemos recorrer los datos usando for
for k in verduras:
    print(k)

# Tambien podemos hacer la referencia a un
# elemento en particular indicando su posición
print(verduras[2])    #---> palta!!!!! 

#----------- funciones con listas ------------------
print("\n Podemos agregar un elemento usando append")
verduras.append("papas")
print(verduras)


print("\n Podemos insertar un elemento usando insert")
verduras.insert(1,"lechuga")
print(verduras)

print("\n Podemos eliminar un elemento usando pop")
verduras.pop(3)
print(verduras)
verduras.pop()   #-->elimina el elemento ultima posición
print(verduras)




    