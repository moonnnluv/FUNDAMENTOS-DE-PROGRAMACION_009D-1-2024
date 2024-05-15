import os

# Variables

opcion_menu = 0
dia = " "
tipo_entrada = " "
descuento = "N"
tipo_descuento = 0
precio_inicial = 0
precio_parcial = 0
precio_final = 0
cantidad_entradas = 0

# Estadisticas

total_entradas = 0
total_recaudado = 0


menu = print(f'''------- Bienvenido/a Teatro Moro -------
             - - - MENU - - -
             1. Comprar entradas
             2. Ver estadisticas
             3. Salir''')
opcion_menu = int(input("Seleccione una opcion: "))

if opcion_menu == 1:   # Compra entradas
    print(f'''Día Función       General       Estudiante
             Viernes          $15.000       $10.000
             Sábado           $18.000       $12.000
             Domingo          $20.000       $15.000''')
    dia = str(input("Seleccione día: "))
    tipo_entrada = str(input("Seleccione tipo de entrada: "))
    
    dia = dia.upper()
    tipo_entrada = tipo_entrada.upper()
    
    '''
    if dia == 'Viernes' and tipo_entrada == 'General':
        precio_inicial = 15000
    if dia == 'Viernes' and tipo_entrada == 'Estudiante':
        precio_inicial = 10000
        
    if dia == 'Sábado' and tipo_entrada == 'General':
        precio_inicial = 18000
    if dia == 'Sábado' and tipo_entrada == 'Estudiante':
        precio_inicial = 12000
    
    if dia == 'Domingo' and tipo_entrada == 'General':
        precio_inicial = 20000
    if dia == 'Domingo' and tipo_entrada == 'Estudiante':
        precio_inicial = 15000
    '''
    if dia == 'viernes':
        if tipo_entrada == 'general':
            precio_inicial = 15000
        else:
            precio_inicial = 10000
    elif dia == 'sabado':
        if tipo_entrada == 'general':
            precio_inicial = 18000
        else:
            precio_inicial = 12000
    else:
        if tipo_entrada == 'general':
            precio_inicial = 20000
        else:
            precio_inicial = 15000
        
    cantidad_entradas = int(input("Seleccione cantidad de entradas a comprar: "))
    precio_inicial = precio_inicial * cantidad_entradas
        
    descuento = str(input("¿Posee descuento?: "))
    descuento = descuento.upper()

    
    
    if descuento.upper() == 'S' or descuento.upper() == 'SI':
        tipo_descuento = int(input('''Seleccione descuento:
                                1. Zona Entel 30%
                                2. Club Metrogas 10%: '''))
        
        if tipo_descuento == 1:
            precio_parcial = precio_inicial * 0.3
        elif tipo_descuento == 2:
            precio_parcial = precio_inicial * 0.1

        precio_final = precio_inicial - precio_parcial
    elif descuento.upper() == 'N' or descuento.upper() == 'NO':
        precio_final = precio_inicial

    precio_parcial = int(precio_parcial)
    precio_final = int(precio_final)

    print(f'''------- TICKET COMPRA -------
            Día función: {dia} 
            Cantidad de entradas: {cantidad_entradas} 
            Tipo de entrada: {tipo_entrada} 
            Subtotal: $ {precio_inicial} 
            Descuento: {tipo_descuento}  ${precio_parcial} 
            Total $ {precio_final}''')
    
    total_entradas = total_entradas + cantidad_entradas
    total_recaudado = total_recaudado + precio_final


if opcion_menu == 2:   # Ver estadísticas
    print("Total entradas vendidas: ", total_entradas)
    print("Total recaudado: $ ", total_recaudado)

if opcion_menu == 3:
