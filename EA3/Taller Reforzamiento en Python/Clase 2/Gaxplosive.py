import os
import modulos_gaxplosive as mg
op_menu = 0


while True:

    op_menu = int(input(f'''======= MENU GAXPLOSIVE =======
      1. Registrar pedido
      2. Listar pedidos
      3. Imprimir hoja de ruta
      4. Salir
      
      Ingrese una opción: '''))
    
    if op_menu == 1:
        os.system("cls")
        mg.registro_pedido()
        os.system("pause")

    if op_menu == 2:
        os.system("cls")
        mg.listar_pedidos()
        os.system("pause")

    if op_menu == 3:
        os.system("cls")
        mg.hoja_ruta()
        os.system("pause")

    if op_menu == 4:
        os.system("cls")
        print("Gracias por comprar en Gaxplosive!")
        os.system("pause")
        break


    
    
