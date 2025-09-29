# Ejercicio 5
# Ahora crea un programa, en el cual el usuario deba ingresar datos como en el ejercicio anterior, debe solicitar nombre y edad
# Esto con el fin de que luego de que el usuario no quiera ingresar mas datos, estos se impriman por pantalla
# El ejercicio debe manejar posibles errores y manejar el hecho de que el usuario no quiera ingresar mas datos usando la palabra 'salir'

lista_datos = []
flag = True

'''
while True:
    try:
        nombre.lower() == "salir"
        break
    except:
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        datos = [nombre, edad]
        lista_datos.append(datos)
        print(lista_datos)
'''

while True:
    nombre = input("Ingrese su nombre: ")
    if nombre.lower() == "salir":
        break
    else:
        while flag == True:
            try:
                edad = int(input("Ingrese su edad: "))
                flag = False
            except:
                print("Ingresa una edad valida")

    if flag == False:
        datos = [nombre, edad]
        lista_datos.append(datos)
    

    flag = True
print("Datos: ")
for elementos in lista_datos:
    print(f"Nombre: {elementos[0]} \nEdad: {elementos[1]}")