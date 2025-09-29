lista_autos = []

def registro_auto():
    patente = input("Ingrese patente: ").upper()
    marca = input("Ingrese marca: ").upper()
    modelo = input("Ingrese modelo: ").upper()
    año = int(input("Ingrese año: "))

    while True:
        combustible = input("Ingrese combustible: ").upper()
        if combustible == "GASOLINA" or combustible == "DIESEL" or combustible == "ELECTRICO":
             valor = int(input("Ingrese valor: "))
             break
        else:
            print("Ingrese tipo de combustible valido (gasolina, diesel o electrico): ")

   

    # Diccionario con autos
    autos = {
            "Patente": patente,
            "Marca": marca,
            "Modelo": modelo,
            "Año": año,
            "Combustible": combustible,
            "Valor": valor,
        }
    lista_autos.append(autos)
    return

def listar_autos():
    if len(lista_autos) == 0:
        print("No existe registro.")
        return
    for compra in lista_autos:
        print(compra)


def imprimir_oferta():
    marcas = {" KIA", " TOYOTA", " HONDA"}
    print("Marcas disponibles: ", ",".join(marcas))
    marca_elegida = input("Seleccione una marca para imprimir oferta disponible: ").upper()
    with open(f'''oferta_{marca_elegida}.txt''', 'w') as archivo:
        for autos in lista_autos:
            if autos["Marca"] == marca_elegida:
                archivo.write(f'''
                                Patente: {autos['Patente']}
                                Marca: {autos['Marca']}
                                Modelo: {autos['Modelo']}
                                Año: {autos['Año']}
                                Combustible: {autos['Combustible']}
                                Valor: {autos['Valor']}''')
    print("\nArchivo txt listo!")

def estadisticas():
    if not lista_autos:
        print("No existe registro.")
        return
    
    total_autos = len(lista_autos)
    marcas_registradas = len(set(autos["Marca"] for autos in lista_autos))
    autos_electricos = sum(autos["Combustible"] == "ELECTRICO" for autos in lista_autos)
    
    print(f'''Cantidad de autos registrados: {total_autos}''')
    print(f'''Cantidad de marcas registradas: {marcas_registradas}''')
    print(f'''Cantidad de autos eléctricos: {autos_electricos}''')