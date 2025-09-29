import os
import modulo_venta_gas as mv 
#---------- variables ---------------
op_menu = ""   # Selección del menú principal

#-------- Código Principal ----------------
while True:
    os.system("cls")
    op_menu = str(input('''
    ========= App Venta GAS ================                        
    1. Crear BD de ventas
    2. Listar ventas
    3. Crear reporte
    4. Estadísticas
    5. (En construcción)
    6. Salir
    \n Elija opción:  '''))
    
    if op_menu =="1":
        os.system("cls")
        mv.crear_ventas_list()
        os.system("pause")
        
    if op_menu =="2":
        os.system("cls")
        
        os.system("pause")
    
    if op_menu =="3":
        os.system("cls")
        
        os.system("pause")
    
    if op_menu =="4":
        os.system("cls")
        
        os.system("pause")
    
    if op_menu =="5":
        os.system("cls")
        
        os.system("pause")
    
    if op_menu =="6":
        break