import os
# vamos a importar nuestra libreria y la
# llamaremos por un alias (apodo) que será fn
import funciones_notas as fn

# ------------ variables ------------
op_menu = ""
nota1, nota2, nota3, prom = 0, 0, 0, 0
estado = ""
# ------- Código Principal ----------
while True:
    os.system("cls")
    op_menu = str(input('''
    ----- App Saca Promedio v4.0 ----
    1.- Ingresar notas y determinar promedio
    2.- Ver estadísticas
    3.- Salir   
    \n Elija opción:  '''))

    if op_menu == "1":
        os.system("cls")
        print("\n ---Ingresar notas y determinar promedio--")
        nota1 = float(input("Ingrese nota1: "))
        while not fn.validar_nota(nota1):
            print("Error, nota no valida")
            nota1 = float(input("Ingrese nota1: "))
        
        nota2 = float(input("Ingrese nota2: "))
        while not fn.validar_nota(nota2):
            print("Error, nota no valida")
            nota2 = float(input("Ingrese nota2: "))            
            
        nota3 = float(input("Ingrese nota3: "))
        while not fn.validar_nota(nota3):
            print("Error, nota no valida")
            nota3 = float(input("Ingrese nota2: "))            
                
        prom = fn.sacar_promedio(nota1, nota2, nota3)
        
        estado = fn.determinar_estado(prom)
        
        fn.imprimir_ticket(nota1, nota2, nota3,  prom, estado)
        
        os.system("pause")

    if op_menu == "2":
        os.system("cls")

        os.system("pause")

    if op_menu == "3":
        break
