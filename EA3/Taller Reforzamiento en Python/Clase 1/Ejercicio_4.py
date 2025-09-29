# Ejercicio 4
# Crea una lista de listas, donde la lista interna deberá ser un par ordenado de [nombre, edad], luego imprime de la siguiente manera los datos de tu lista:
# "Tu nombre es {nombre} y tienes {edad} años cumplidos"

lista = [["Alejandra", 20], ["Alonso", 11], ["Emilia", 10]]

for elemento in lista:
    print(f"Tu nombre es {elemento[0]} y tienes {elemento[1]} años cumplidos")