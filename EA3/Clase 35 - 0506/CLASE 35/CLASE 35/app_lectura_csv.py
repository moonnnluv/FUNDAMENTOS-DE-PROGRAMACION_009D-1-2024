import os
import csv
# Sintaxis: open('nombre_del_archivo.csv', 'modo', newline='')
# Modo común: 'r' (lectura)

print("LINEA \t ESTACIÓN \t COMUNA")
with open('metro.csv', 'r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(f"{fila[0]} \t {fila[1]} \t {fila[2]} ")

# Propuesto 1
# Listar los nombre de todas las estaciones de comuna Santiago
print("\n--- Estaciones comuna Santiago ----")
with open('metro.csv', 'r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        if fila[2] == "Santiago":
            print(f"{fila[1]}")

# Propuesto 2
# Determinar la cantidad de estaciones de metro que
# pertenecen a la comuna de Recoleta
estaciones_L2 =[]
with open('metro.csv', 'r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        if fila[2] == "Recoleta":
            estaciones_L2.append(fila[1]) # guadamos los nombres

print(f'''
    Hay {len(estaciones_L2)} estaciones en L2
    estas son: {sorted(estaciones_L2)}  
      ''')            


# Propuesto 3
# Determinar la cantidad de estaciones de metro que
# pertenecen a la LINEA 2, ademas de imprimir los
# nombres de estas en orden alfabetico
