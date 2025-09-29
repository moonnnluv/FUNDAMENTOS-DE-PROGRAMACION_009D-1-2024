# Ejercicio 6
# Guarda en una lista usando diccionarios los datos de las personas: Nombre, Edad, Genero (Masculino / Femenino / No Binario)
# El programa deberá solicitar en un inicio la cantidad de personas que se van a ingresar para saber cuantas veces el programa debe 
# solicitar la información y se deberá guardar en una tupla la cantidad de generos en total (m,f,nb)
# Para finalizar el programa deberá imprimir por pantalla todos los datos de las personas registradas y mostrar la estadística de los generos

lista_datos = []
contador = 0
cantidad_m = 0
cantidad_f = 0
cantidad_nb = 0

while True:
    try:
        cantidad_personas = int(input("Ingrese cantidad de personas: "))
        break
    except:
        print("Ingresa un numero valido.")


while contador < cantidad_personas:
    print(f"Persona N°{contador+1}")

    nombre = input("Ingrese Nombre: ")

    flag = True
    while flag == True:
        try:
            edad = int(input("Ingrese Edad: "))
            flag = False
        except:
            print("Ingrese una edad válida.")

    flag2 = True
    while flag2 == True:
        try:
            genero = input("Ingrese Género: ").lower()
            print("\n")
            if genero == "m" or genero == "f" or genero == "nb":
                flag2 = False
        except:
            print("Ingrese un genero válido.")

    if genero == "m":
        cantidad_m = cantidad_m + 1
    elif genero == "f":
        cantidad_f = cantidad_f + 1
    else:
        cantidad_nb = cantidad_nb + 1

    # Clave, valor
    diccionario = {"Nombre": nombre,
                "Edad": edad,
                "Género": genero}

    lista_datos.append(diccionario)
    contador = contador + 1


tupla_generos = (cantidad_m, cantidad_f, cantidad_nb)

print("======= Listado Personas =======")
for elemento in lista_datos:
    print("Nombre:",elemento["Nombre"], "\nEdad:",elemento["Edad"], "\nGenero:",elemento["Género"])
    print("\n")

print(f"Estadísticas de Géneros:")
print(f"Masculino (m): {tupla_generos[0]/cantidad_personas*100} %")
print(f"Femenino (f): {tupla_generos[1]/cantidad_personas*100} %")
print(f"No Binario (nb): {tupla_generos[2]/cantidad_personas*100} %")

