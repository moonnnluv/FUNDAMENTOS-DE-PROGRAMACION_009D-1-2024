import os
os.system("cls")

# Vamos a crear 3 autos (diccionarios) y luego
# los vamos a almacenar en una UNICA LISTA

auto_1 = {
    "patente": "AABB11",
    "marca": "Kia",
    "modelo": "Rio",
    "año": 2012,
    "multas": [
        {
            "fecha": "21/feb/2020",
            "causa": "Exceso de velocidad"
        }
    ]
}


auto_2 = {
    "patente": "BBCC22",
    "marca": "Toyota",
    "modelo": "Yaris",
    "año": 2000,
    "multas": [
        {
            "fecha": "31/dic/2019",
            "causa": "Conducir bajor efectos del alcohol"
        },
        {
            "fecha": "21/feb/2020",
            "causa": "Exceso de velocidad"
        }
    ]
}


auto_3 = {
    "patente": "CCDD33",
    "marca": "Ford",
    "modelo": "Fiesta",
    "año": 2020,
    "multas": []  # --> sin multas
}

# creamos la lista y luego almacenamos los json
autos_list = []  # ---> lista vacia
autos_list.append(auto_1)
autos_list.append(auto_2)
autos_list.append(auto_3)

# LÓGICA: "de las lista de autos vamos a sacar un
# auto, este es un json"

# vamos a imprimir toda la información
# incluyendo las lista
# for auto in autos_list:
#     # print(auto)
#     for k in auto.keys():
#         if k == "multas":
#             for multa in auto["multas"]:
#                 print(f"Fecha:{multa["fecha"]} --> Causa:{multa["causa"]}")
#         else:
#             print(f"{k} --> {auto[k]}")
#     print("---------------------")       

# propuesto 1
# van a solicitar al usuario una patente y la van
# buscar dentro de la lista, si se encuentra
# imprimen todos los datos del auto

patente_buscar = str(input("Ingrese patente: ")).strip().upper()


encontrado = False
for auto in autos_list:
    if auto["patente"] == patente_buscar:
        encontrado = True
        print(f'''
        ========= DATOS ========
        Patente: {auto["patente"]}
        Marca: {auto["marca"]}
        Modelo: {auto["modelo"]}
        Año: {auto["año"]}
        Multas: {auto["multas"]} ''')     

if encontrado == False:
    print("NO hay registro para dicha patente")      
    
# PROPUESTO 2
# Los mismo anterior, pero una vez entrado el auto
# se la agregará otra multa a la lista     
    
