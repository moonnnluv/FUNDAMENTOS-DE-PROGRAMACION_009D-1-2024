import os
import json

# una lista de objetos json de tipo celular
celulares_list = []


def crear_registro():
    # pediremos los datos al user y creamos el json
    numero = str(input("Ingrese N° ")).strip()
    marca = str(input("Ingrese marca: ")).strip()
    modelo = str(input("Ingrese modelo:")).strip()
    compañia = str(input("Ingrese compañia: ")).strip()

    celular = {
        "numero": numero,
        "marca": marca,
        "modelo": modelo,
        "compañia": compañia
    }
    celulares_list.append(celular)


def listar_registros():
    if not celulares_list:
        print("Falta crear la BD")
    else:
        os.system("cls")
        for celular in celulares_list:
            print(f'''
            N° {celular["numero"]}
            {celular["marca"]} - {celular["modelo"]}
            Compañia: {celular["compañia"]} ''')
