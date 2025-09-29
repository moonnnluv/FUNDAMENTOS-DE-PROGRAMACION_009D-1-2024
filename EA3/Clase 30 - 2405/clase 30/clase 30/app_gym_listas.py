# vamos a seleccionar el archivo y luego importar
# que nos interesa de este
from imprimir_formato import imprimir_ticket as it

import os
# ---------- variables -------------------
op_menu = ""
nombre = ""
lista_nombres = []
edad = 0
lista_edades = []
peso = 0
lista_pesos = []
estatura = 0
lista_estaturas = []
imc = 0
lista_imc = []
clasificacion = ""
lista_clasificaciones = []
# --------- Código Principal -------------
while True:
    os.system("cls")
    op_menu = str(input('''
    --------- App Gym --------
    1. Cargar datos y determinar IMC
    2. Listar datos
    3. Listar por clasificación
    4. Salir
    \n Elija opción: '''))

    if op_menu == "1":
        os.system("cls")
        print("\n---Cargar datos y determinar IMC --")
        nombre = str(input("Ingrese nombre:")).strip()
        while not len(nombre) > 0:
            print("Error, no puede ser vacio")
            nombre = str(input("Ingrese nombre:")).strip()
        lista_nombres.append(nombre)

        edad = int(input("Ingrese edad: "))
        while not edad > 0:
            print("Error, debe ser mayor a cero")
            edad = int(input("Ingrese edad: "))
        lista_edades.append(edad)

        peso = int(input("Ingrese peso Kg:"))
        while not peso > 0:
            print("Error, debe ser mayor a cero")
            peso = int(input("Ingrese peso Kg:"))
        lista_pesos.append(peso)

        estatura = float(input("Ingrese estatura m:"))
        while not estatura > 0:
            print("Error, debe ser mayor a cero")
            estatura = float(input("Ingrese estatura m:"))
        lista_estaturas.append(estatura)

        # vamos a realizar los calculos determinar imc
        imc = peso/estatura**2
        lista_imc.append(imc)

        if imc < 18.5:
            clasificacion = "Bajo peso"
        elif 18.5 <= imc <= 24.9:
            clasificacion = "Normal"
        elif 25 <= imc <= 29.9:
            clasificacion = "Sobrepeso"
        elif clasificacion >= 30:
            clasificacion = "Obesidad"

        lista_clasificaciones.append(clasificacion)
        
        os.system("cls")
        it(nombre, edad, peso, estatura, imc, clasificacion)

        os.system("pause")

    if op_menu == "2":
        os.system("cls")

        os.system("pause")

    if op_menu == "3":
        os.system("cls")

        os.system("pause")

    if op_menu == "4":
        break
