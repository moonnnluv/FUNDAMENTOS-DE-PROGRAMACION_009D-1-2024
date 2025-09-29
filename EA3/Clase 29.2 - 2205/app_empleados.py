import os
# ---------- VARIABLES ------------------------
op_menu = ""         # Selección menú principal
nombre = ""
lista_nombres = []
edad = 18
lista_edades = []
sexo = "F"
lista_sexos = []
sueldo = 0
lista_sueldos = []
# ---------- CÓDIGO PRINCIPAL ----------------------
while True:
    os.system("cls")
    op_menu = str(input('''
    ---------- App Empleados ---------
    1. Cargar datos
    2. Listar datos
    3. Listar por sexo
    4. Listar por rango de edad
    5. Salir
    \n Elija opción: '''))

    if op_menu == "1":
        os.system("cls")
        nombre = str(input("Ingrese nombre: ")).strip()
        # validamos el datos
        # len cuenta la cantidad de caracteres del str
        while not len(nombre) > 0:
            print("Error, no puede ser vacio")
            nombre = str(input("Ingrese nombre: ")).strip()
        # Pasada la validación lo almacenamos en la lista
        lista_nombres.append(nombre)

        edad = int(input("Ingrese edad: "))
        while not edad >= 18:
            print("Error, mínimo 18 años")
            edad = int(input("Ingrese edad: "))
        lista_edades.append(edad)

        sexo = str(input("Ingrese sexo:")).strip().upper()
        while not sexo in ["F", "M"]:
            print("Error, son valido F o M")
            sexo = str(input("Ingrese sexo:")).strip().upper()
        lista_sexos.append(sexo)

        sueldo = int(input("Ingrese sueldo $"))
        while not sueldo >= 470000:
            print("Error, mínimo $470000")
            sueldo = int(input("Ingrese sueldo $"))
        lista_sueldos.append(sueldo)

        # --- vamos a visualizar las listas
        print(f'''
            {lista_nombres}
            {lista_edades}
            {lista_sexos}
            {lista_sueldos} ''')

        os.system("pause")

    if op_menu == "2":
        os.system("cls")
        print("\n----- Listar Datos -----")
        # El len determina la cantidad de elementos
        # que posee la lista
        cant_registros = len(lista_nombres)
        # el range(cant_elementos) nos dará las
        # posiciones a recorrer los datos
        for k in range(cant_registros):
            print(f'''
            --------- Empleado {k+1} -----
            Nombre: {lista_nombres[k]}
            Edad: {lista_edades[k]} años
            Sexo: {lista_sexos[k]}
            Sueldo ${lista_sueldos[k]}    ''')
        os.system("pause")

    if op_menu == "3":
        os.system("cls")
        encontrado = False
        print("\n---- Listar por sexo -----")
        sexo_buscar = str(input("Ingrese sexo: ")).strip().upper()

        cant_registros = len(lista_nombres)
        for k in range(cant_registros):
            if lista_sexos[k] == sexo_buscar:
                encontrado = True
                print(f'''
                Nombre: {lista_nombres[k]}
                Edad: {lista_edades[k]} años
                Sexo: {lista_sexos[k]}
                Sueldo ${lista_sueldos[k]}    ''')

        if encontrado == False:
            print("NO se encontro empleado de dicho sexo")
        os.system("pause")

    if op_menu == "4":
        os.system("cls")
        encontrado = False
        print("\n --- Listar por rango de edad ---")
        min = int(input("Ingrese edad mínima: "))
        max = int(input("Ingrese edad máxima: "))

        cant_registros = len(lista_nombres)

        for k in range(cant_registros):
            if min <= lista_edades[k] <= max:
                encontrado = True
                print(f'''
                Nombre: {lista_nombres[k]}
                Edad: {lista_edades[k]} años
                Sexo: {lista_sexos[k]}
                Sueldo ${lista_sueldos[k]}    ''')

        if encontrado == False:
            print("NO se encontro registro en el rango ingresado!!!")

        os.system("pause")

    if op_menu == "5":
        break
