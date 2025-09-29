import os

lista_pedidos = []

lista_cliente = []
lista_direccion = []
lista_sector = []
lista_5kg = []
lista_15kg = []
lista_45kg = []

def registro_pedido():
    print(f'''======= PEDIDO =======
          ''')
    nombre = input("Ingrese su nombre: ").lower()
    direccion = input("Ingrese su direccion: ").lower()
    sector = input("Ingrese su sector: ").lower()
    cil_5kg = (input("Ingrese cantidad de Cilindros de 5kg: "))
    cil_15kg = (input("Ingrese cantidad de Cilindros de 15kg: "))
    cil_45kg = (input("Ingrese cantidad de Cilindros de 45kg: "))
    
    # Diccionario con pedidos
    pedido = {
                "Nombre": nombre,
            "Direccion": direccion,
            "Sector": sector,
            "Cilindro 5kg": cil_5kg,
            "Cilindro 15kg": cil_15kg,
            "Cilindro 45kg": cil_45kg
        }
    lista_pedidos.append(pedido)
    return

def listar_pedidos():
    if len(lista_pedidos) == 0:
        print("No hay datos registrados")
        return
    print("\nListado de pedidos: ")
    for clientes in lista_pedidos:
        print(clientes)

def hoja_ruta():
    sectores = {"centro", "colina", "industrias"}
    print("Sectores disponibles:", ", ".join(sectores))
    sector_elegido = input("Ingrese al sector para imprimir la hoja de ruta: ")
    with open(f'''hoja_ruta_{sector_elegido}.txt''', 'w') as archivo:
        for pedido in lista_pedidos:
            if pedido["Sector"] == sector_elegido:
                archivo.write(f'''Nombre: {pedido['Nombre']}
                                Dirección: {pedido['Direccion']}
                                Sector: {pedido['Sector']}
                                Cilindro 5kg: {pedido['Cilindro 5kg']}
                                Cilindro 15kg: {pedido['Cilindro 15kg']}
                                Cilindro 45kg: {pedido['Cilindro 45kg']}\n\n''')

