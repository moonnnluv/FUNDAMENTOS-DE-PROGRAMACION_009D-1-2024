import os
import csv
import random  # --> para los N° aleatorios

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

# tendrá valores entre $20.000 y $28.000
valor_gas_list = []

# tendrá valores entre 200 y 300
cant_vendida_list = []

# contendrá json (venta)
ventas_list = []


def generar_valores_aleatorios(min, max):
    '''
    Función que crea y retorna una lista de 12 valores
    enteros aleatorios en el rango min y max ingresados
    por parámetro a la función
    '''
    lista_valores = []
    for k in range(12):
        valor = random.randrange(min, max)
        lista_valores.append(valor)
    return lista_valores


def cargar_data_test():
    '''
    El valor del gas estará entre $20.000 y $28.000
    La cantidad estará entre 200 y 300
    '''
    global valor_gas_list
    global cant_vendida_list
    valor_gas_list = generar_valores_aleatorios(20000, 28000)
    cant_vendida_list = generar_valores_aleatorios(200, 300)


def imprimir_listas():
    print(f'''
        GAS       {valor_gas_list}
        CANTIDAD  {cant_vendida_list}
          ''')


def crear_ventas_list():
    global ventas_list  # -> cargamos de datos esta varible global
    ventas_list = []  # --> limpiamos datos anteriores
    #--- cargamos los datos de test ---
    cargar_data_test()
    
    # ahora creamos los json venta y los agregamos
    for pos in range(12):
        total_mes = valor_gas_list[pos]*cant_vendida_list[pos]
        venta = {
            "mes": meses[pos],
            "valor_gas": valor_gas_list[pos],
            "cantidad": cant_vendida_list[pos],
            "total_mes": total_mes
        }
        print(venta)
        ventas_list.append(venta)        
    print("\n ==== BD creada!!!! ========")    
