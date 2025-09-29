import os
import modulo_estudiante as me  #--> alias!!!

#------ variables --------------------
op_menu = ""     # Selección del menú principal

#------- Código Principal -------------
while True:
    os.system("cls")
    op_menu = str(input('''
    ========== App CRUD estudiantes  ============
    1. Crear registro estudiante
    2. Listar estudiantes
    3. Crear archivo respaldo BD
    4. Salir
    \n Elija opción: '''))
    
    if op_menu =="1":
        os.system("cls")
        me.registrar_estudiante()
        os.system("pause")
        
    if op_menu =="2":
        os.system("cls")
        me.listar_estudiantes()
        os.system("pause")
    
    if op_menu =="3":
        os.system("cls")
        me.grabar_datos()
        os.system("pause")
    
    if op_menu =="4":
        print("... saliendo de la app")
        break
