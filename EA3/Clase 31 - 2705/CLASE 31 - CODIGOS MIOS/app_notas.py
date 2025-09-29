# ------- IMPORTAR -------
import funciones_notas as fn # Alias
import os

# ------- VARIABLES -------
op_menu = 0
nota1, nota2, nota3, promedio = 0, 0, 0, 0
estado = " "

# Estadisticas
promedios_calculados = 0
promedio_curso = 0

# ------- CODIGO -------

while True:
    op_menu = int(input(f'''
                    ======== MENU PRINCIPAL =======
                    1. Calcular Promedio
                    2. Estadisticas
                    3. Salir
                       
                    Seleccione una opcion: '''))
    
    
    if op_menu == 1:

        os.system("cls")

        nota1 = float(input("Ingrese primera nota: "))
        while not fn.validar_nota(nota1):
            print("Error, nota no valida")
            nota1 = float(input("Ingrese primera nota: "))

        nota2 = float(input("Ingrese segunda nota: "))
        while not fn.validar_nota(nota2):
            print("Error, nota no valida")
            nota2 = float(input("Ingrese segunda nota: "))

        nota3 = float(input("Ingrese tercera nota: "))
        while not fn.validar_nota(nota2):
            print("Error, nota no valida")
            nota3 = float(input("Ingrese tercera nota: "))

        promedio = fn.sacar_promedio(nota1, nota2, nota3)
        estado = fn.estado(promedio)
        fn.ticket(nota1, nota2, nota3, promedio, estado)

        promedios_calculados = promedios_calculados + 1

        os.system("pause")


    
    if op_menu == 2:
        
        os.system("cls")

        print(f'''
                    ======== ESTADISTICAS =======
                    Total promedios: {promedios_calculados}
                    Promedio curso: {promedio_curso} ''')
        
    os.system("cls")
    if op_menu == 3:
        break