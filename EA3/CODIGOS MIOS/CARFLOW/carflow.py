import os
import modulos_carflow as mcf

op_menu = 0

while True:
    op_menu = int(input(f''' 
                        ======= CARFLOW =======
                        1. Registrar auto
                        2. Listar autos
                        3. Imprimir oferta de auto por marca
                        4. Estadisticas
                        5. Salir del programa

                        Elija una opción: '''))
    
    if op_menu == 1:
        os.system("cls")
        mcf.registro_auto()
        os.system("pause")

    if op_menu == 2:
        os.system("cls")
        mcf.listar_autos()
        os.system("pause")

    if op_menu == 3:
        os.system("cls")
        mcf.imprimir_oferta()
        os.system("pause")

    if op_menu == 4:
        os.system("cls")
        mcf.estadisticas()
        os.system("pause")

    if op_menu == 5:
        os.system("cls")
        print("Gracias por usar CarFlow!\n")
        os.system("pause")
        break
