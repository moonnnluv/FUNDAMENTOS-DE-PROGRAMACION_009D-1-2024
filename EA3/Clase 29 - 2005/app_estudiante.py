import os
# ------------- VARIABLES ------------------------
op_menu = ""        # Selección menú principal
nombre = ""         # Nombre estudiante
lista_nombres = []
edad = 0            # Edad estudiante
lista_edades = []
run = ""            # RUN del estudiante
lista_runs = []

# ------------ CÓDIGO PRINCIPAL ------------
while True:
    os.system("cls")
    op_menu = str(input('''
    =========== App Estudiantes =============                  
    1. Cargar datos
    2. Listar datos
    3. Buscar por run
    4. Salir
    \n Elija opción: '''))

    if op_menu == "1":
        os.system("cls")
        print("\n -------- Cargar datos -------")
        # capturamos el dato
        run = str(input("Ingrese run: ")).strip().upper()
        # validamos el dato, que no sea cadena vacia!!
        # El len cuenta la cantidad de caracteres del str
        while not len(run) > 0:
            print("Error, no puede ser vacio")
            run = str(input("Ingrese run: ")).strip().upper()
        # Una vez que pasa la validación lo almacenamos
        lista_runs.append(run)

        nombre = str(input("Ingrese nombre: ")).strip()
        while not len(nombre) > 0:
            print("Error, no puede ser vacio")
            nombre = str(input("Ingrese nombre: ")).strip()
        lista_nombres.append(nombre)

        edad = int(input("Ingrese edad: "))
        while not edad > 0:
            print("Error, mayor a cero!!")
            edad = int(input("Ingrese edad: "))
        lista_edades.append(edad)

        # imprimos para visualizar los datos
        print(f'''
            {lista_runs}
            {lista_nombres}
            {lista_edades} ''')

        os.system("pause")

    if op_menu == "2":
        os.system("cls")
        print("\n --- Listar Datos ----")
        # Len cuenta la cantidad de elementos de la lista
        cant_estudiantes = len(lista_runs)
        # Ahora vamos a recorrer las listas
        for k in range(cant_estudiantes):
            print(f'''
            Run:{lista_runs[k]}
            Nombre: {lista_nombres[k]}
            Edad: {lista_edades[k]} años ''')

        os.system("pause")

    if op_menu == "3":
        os.system("cls")
        print("\n ---- Buscar Por RUN ----")
        run_buscar = str(input("Ingrese run a buscar:")).strip().upper()

        if lista_runs.count(run_buscar)==0:
            print("No hay registro para el run")
        else:
            cant_estudiantes = len(lista_runs)
            for k in range(cant_estudiantes):
                if lista_runs[k] == run_buscar:
                    print(f'''
                    Run:{lista_runs[k]}
                    Nombre: {lista_nombres[k]}
                    Edad: {lista_edades[k]} años ''')
                    
        os.system("pause")

    if op_menu == "4":
        break
