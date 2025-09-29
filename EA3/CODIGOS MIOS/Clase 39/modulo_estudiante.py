import os
import random       # Numeros aleatorios
import csv

nombres = ["Juan", "Pedro", "Carol", "Luis", "Pia"]
lista_promedios = []
lista_examenes = []
lista_alumnos = [] #Lista JSON

# Notas aleatorias
def lista_aleatoria():
    lista_aleatoria = []
    # Lista con 5 numeros aleatorios
    for k in range(5):
        nota = round(random.uniform(1,7),1) # Notas aleatorias de 1 a 7, redondeado a la primera décima
        lista_aleatoria.append(nota)
    return lista_aleatoria

# Listar alumnos en un json
def lista_alumnos():
    global lista_alumnos # Hacerle entender al programa que es una variable global

    # Reiniciar lista
    lista_alumnos = []
    # Notas random para rellenar promedio y examenes
    lista_promedios = lista_aleatoria()
    lista_examenes = lista_aleatoria()

    # JSON
    for k in range(5):
        # Nota final
        nota_final = round(lista_promedios[k] * 0.6 + lista_examenes[k] * 0.4, 1)
        # Estado
        if nota_final >=4:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        alumno = {
            "nombre": nombres[k],
            "promedio": lista_promedios[k],
            "examen": lista_examenes[k],
            "nota final": nota_final,
            "estado": estado
        }

        # Ingresar los json en la lista
        print(alumno)
        lista_alumnos.append(alumno)

# Printear lista de alumnos
def listar_alumnos():
    os.system("cls")
    for alumno in lista_alumnos:
        print(f"{alumno["nombre"]} - {alumno["promedio"]} - {alumno["examen"]} - {alumno["nota final"]} - {alumno["estado"]}")

# Crear archivo csv
def crear_reporte():
    if not lista_alumnos:
        print("\nPrimero debe crear la lista de alumnos, opción 1 del menú")
    else:
        archivo_salida = "reporte_alumnos.csv"
        with open(archivo_salida, "w", encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            # Cabeceras de archivo
            writer.writerow(["nombre", "promedio", "examen", "nota final", "estado"])
            # Recorrer el json
            for alumno in lista_alumnos:
                fila = [alumno["nombre"], alumno["promedio"], alumno["examen"], alumno["nota final"], alumno["estado"]]
                writer.writerow(fila)

    print("\n ======= REPORTE CREADO =======")
