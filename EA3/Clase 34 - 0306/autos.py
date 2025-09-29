# LISTAS


auto_list = ["auto1", "auto2", "auto3"]

auto1 = {
    "patente": "AABB11",
    "marca": "Kia",
    "modelo": "Rio",
    "año": 2012,
    "multas": [
        {
            "fecha": "21/Feb/2020",
            "causa": "Exceso de velocidad"
        }
        ]
}

auto2 = {
    "patente": "BBCC22",
    "marca": "Toyota",
    "modelo": "Yaris",
    "año": 2000,
    "multas": [
        {
            "fecha": "31/Dic/2019",
            "causa": "Conducir bajo los efectos del alcohol"
        },
        {
            "fecha": "21/Feb/2020",
            "causa": "Exceso de velocidad"
        }
        ]
}

auto3 = {
    "patente": "CCDD33",
    "marca": "Ford",
    "modelo": "Fiesta",
    "año": 2020,
    "multas": []
}

# print(auto)

for auto in auto_list:
    for k in auto.keys():
        if k == "multas":
            for multa in auto["multas"]:
                print(f"Fecha:{multa ["fecha"]} --> Causa: {multa["causa"]}")
        else:
            print(f"{k} --> {auto[k]}")


# Propuesto 1
# Buscar patente e imprimir la informacion del vehiculo

buscar_patente = str(input("Ingrese patente: ")).strip().upper()

for auto in auto_list:
    if auto["patente"] == buscar_patente:
        encontrado = True
        print(f'''
              ======= DATOS =======
              Patente: {auto["patente"]}
              Marca: {auto["marca"]}
              Modelo: {auto["modelo"]}
              Año: {auto["año"]}
              Multas: {auto["multas"]}
              ''')
                
if encontrado == False:
    print("No hay registro para dicha patente")