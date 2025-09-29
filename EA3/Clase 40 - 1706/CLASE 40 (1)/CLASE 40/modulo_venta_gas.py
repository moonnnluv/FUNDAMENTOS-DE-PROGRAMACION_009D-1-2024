import os
import csv
import random  # --> para los N° aleatorios
import modulo_mat as mm 

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

# tendrá valores entre $20.000 y $28.000
valor_gas_list = []

# tendrá valores entre 200 y 300
cant_vendida_list = []

# contendrá json (venta)
ventas_list = []


# NUEVA variable de tipo lista, con los valores de cada mes
totales_mes_list = []




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
    # --- cargamos los datos de test ---
    cargar_data_test()

    # ahora creamos los json venta y los agregamos
    for pos in range(12):
        total_mes = valor_gas_list[pos]*cant_vendida_list[pos]
        # vamos agregar el total a la lista de totales
        totales_mes_list.append(total_mes)
        venta = {
            "mes": meses[pos],
            "valor_gas": valor_gas_list[pos],
            "cantidad": cant_vendida_list[pos],
            "total_mes": total_mes
        }
        # print(venta)
        ventas_list.append(venta)
    print("\n ==== BD creada!!!! ========")


def listar_ventas_list():
    if not ventas_list:
        print("Primero la BD, opción 1")
    else:
        for venta in ventas_list:
            print(f'''
            Mes: {venta["mes"]}
            Valor gas ${venta["valor_gas"]}
            Cantidad: {venta["cantidad"]}
            Total ${venta["total_mes"]} ''')


def crear_reporte_ventas():
    if not ventas_list:
        print("Primero la BD, opción 1")
    else:
        archivo_salida = "reporte_ventas.csv"
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            # colocamos las cabeceras al archivo
            escritor.writerow(["MES", "VALOR", "CANTIDAD", "TOTAL"])
            for venta in ventas_list:
                fila = [venta["mes"], venta["valor_gas"], venta["cantidad"], venta["total_mes"]]
                escritor.writerow(fila)
        print(f"\n==== archivo {archivo_salida} creado exitosamente =====")
        
def determinar_estadisticas():
    global ventas_list
    if not ventas_list:
        print("Primero la BD, opción 1")        
    else:
        mm.estadisticas_basicas(totales_mes_list)
        mm.media_geometrica(totales_mes_list)
