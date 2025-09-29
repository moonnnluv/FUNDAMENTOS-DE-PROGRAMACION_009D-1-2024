import os
import csv
import json
import modulo_imc as mi  #-->alias!!!!
os.system("cls")

lista = []   # lista en donde vamos ir dejando los json

# Vamos hacer lectura del archivo
# llamado usuarios_ficticios.csv

with open('usuarios_ficticios.csv','r',encoding='utf-8') as archivo_csv:
    # DictReader nos va crear un diccionario. K->V
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        nombre = fila["nombre"]
               # estamos conviertiendo de str a int
        peso = int(fila["peso"])
        estatura = float(fila["estatura"])
        # usamos la librería para determinar imc
        imc = mi.calcular_imc(peso, estatura)
        clasificacion = mi.clasificar_imc(imc)
        
        # vializaremos los datos
        print(f'''
              {nombre} - {peso} - {estatura}
              IMC:{imc}   Clasificación:{clasificacion}''')
        
        # Ahora por cada lectura de nuestro ciclo for
        # vamos a crear un objeto json 
        deportista = {
            "nombre":nombre,
            "peso":peso,
            "estatura":estatura,
            "imc":imc,
            "clasificación":clasificacion
        }
        lista.append(deportista)
       
print("=== se creo archivo json ====") 
# vamos a crear la salida como archivo json
with open('resultado_imc.json','w', encoding='utf-8') as archivo:
    # 1er parámetro es el objeto que deseas convertir
    # 2do parámetro es donde se va a escribir
    json.dump(lista, archivo, ensure_ascii=False, indent=4)        
        
    
    