import os
os.system("cls")

auto_1 = {
    "patente": "AABB11",
    "marca": "Kia",
    "modelo": "Rio",
    "año": 2002
}

auto_2 = {
    "patente": "BCC11",
    "marca": "Toyota",
    "modelo": "Yaris",
    "año": 2013
}

auto_3 = {
    "patente": "FFDD22",
    "marca": "Ford",
    "modelo": "Fiesta",
    "año": 2001
}

# Vamos a crear una lista y vamos almacenar
# los diccionarios dentro de la lista

# lista_autos = [auto_1,auto_2, auto_3]
lista_autos = []   #---> lista vacia
lista_autos.append(auto_1)
lista_autos.append(auto_2)
lista_autos.append(auto_3)

# Vamos a recorrer la lista de autos
for auto in lista_autos:
    print(auto)
    
print("\n vamos a desplegar la información de cada diccionario")    
for auto in lista_autos:
    for k, v in auto.items():
        print(f'''
            {k} --> {v}  
              ''')
        
# Otra forma de hacer le recorrido, la k representa
# posiciones dentro del lista
print("Recorriendo los autos solicitando KEYS")
for auto in lista_autos:
    for clave in auto.keys():
        print(f"{clave} --> {auto[clave]}")
    
