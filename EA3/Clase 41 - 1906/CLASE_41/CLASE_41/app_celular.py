import os
import modulo_celular as mc 

# ----------- variables ------------
op_menu = ""

#---------- Código Principal -------------
while True:
    os.system("cls")
    op_menu = str(input('''
    ========  App Celular ===============                        
    1. Crear registro celular
    2. Listar celulares
    3.
    4. Salir
    \n ELija opción: '''))
    
    if op_menu =="1":
        os.system("cls")
        mc.crear_registro()        
        os.system("pause")
        
    if op_menu =="2":
        os.system("cls")
        mc.listar_registros()
        os.system("pause")
    
    if op_menu =="3":
        os.system("cls")
        
        os.system("pause")
    
    if op_menu =="4":
        break
