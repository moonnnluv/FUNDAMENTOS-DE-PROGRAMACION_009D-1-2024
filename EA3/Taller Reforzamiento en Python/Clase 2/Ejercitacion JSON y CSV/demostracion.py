import csv
import json

# Ruta
json_ruta = 'archivo.json'
csv_ruta = 'archivo.csv'
txt_ruta = 'archivo.txt'

# Guardar ruta

def leer_json(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo: # Leer archivo
        return json.load(archivo) # Printear
    

def leer_csv(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo: # Leer archivo
        return list(csv.DictReader(archivo)) # Printear y listar los datos
    
def leer_txt(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo: # Leer archivo
        return archivo.readlines() # Printear

# Guardar datos

datos_json = leer_json(json_ruta)
print(datos_json)

datos_csv = leer_csv(csv_ruta)
print(datos_csv)

datos_txt = leer_txt(txt_ruta)
print(datos_txt)

