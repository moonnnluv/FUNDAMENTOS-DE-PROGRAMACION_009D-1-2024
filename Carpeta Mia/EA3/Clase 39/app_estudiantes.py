import os
import modulo_estudiante as me


while True:
    op_menu = str(input('''
    ====== App Estudiantes ====
    1. crear alumnos list
    2. listar alumnos list
    3. Crear reporte
    4.
    5. 
    6. Salir                    
    \nElija opción:    '''))

    if op_menu == "1":
        os.system("cls")
        me.lista_alumnos()
        os.system("pause")



    if op_menu == "2":
        os.system("cls")
        me.listar_alumnos()
        os.system("pause")
        
    if op_menu == "3":
        os.system("cls")
        me.crear_reporte()
        os.system("pause")
        
    #if op_menu == "4":
        
    #if op_menu == "5":

    #if op_menu == "6":
    
