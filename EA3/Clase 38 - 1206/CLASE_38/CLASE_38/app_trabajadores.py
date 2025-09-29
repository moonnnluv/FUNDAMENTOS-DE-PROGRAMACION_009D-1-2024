import os
import modelo_trabajadores as mt  #--> alias!!!

#-------- variables ---------------
op_menu = ""        # Selección del menú principal

#------ Código Principal ---------------
while True:
    os.system("cls")
    op_menu = str(input('''
    ========= App Trabajadores v1.0 =========                        
    1. Crear registro trabajador
    2. Listar trabajadores
    3. Crear planilla sueldos
    4. (en construcción)
    5. carga data testing
    6. Salir
    \n Elija opción:  '''))
    
    if op_menu == "1":
        os.system("cls")
        mt.registrar_trabajador()
        os.system("pause")
        
    if op_menu == "2":
        os.system("cls")
        mt.listar_trabajadores()
        os.system("pause")
    
    if op_menu == "3":
        os.system("cls")
        mt.imprimir_sueldos()
        os.system("pause")
    
    if op_menu == "4":
        os.system("cls")
        
        os.system("pause")
    
    if op_menu == "5":
        os.system("cls")
        mt.cargar_datos_test()
        os.system("pause")
    
    if op_menu == "6":
        break




