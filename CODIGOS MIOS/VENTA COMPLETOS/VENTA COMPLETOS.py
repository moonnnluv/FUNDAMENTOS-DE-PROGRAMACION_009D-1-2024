# ------- VARIABLES -------

op_menu = " "
tipo_completo = " "
precio = 0
precio_papas = 2000
precio_bebida = 1200
cantidad = 0
adicional = " "
cantidad_papas = 0
cantidad_bebida = 0
total_inicial = 0
total_parcial = 0
total_final = 0

# Nombres
nombre_completo = " "
completo = "Completo"
italiano = "Italiano"
dinamico = "Dinamico"
papas_fritas = "Papas Fritas"
bebida = "Bebida 500cc"

# Estadisticas
clientes_atendidos = 0
total_recaudado = 0

# ------- CODIGO -------

while True:
    op_menu = int(input(f'''------- MENU PRINCIPAL -------
                    
                    1. Venta
                    2. Estadisticas
                    3. Salir
                    
                    Elija una opcion: '''))



    if op_menu == 1:
        print((f'''------- MENU COMPLETOS -------
                    TIPO COMPLETO          VALOR

                    1. Completo            $1.200
                    2. Italiano            $1.600
                    3. Dinamico            $1.700
                    
                    '''))
        tipo_completo = int(input("Seleccione tipo de completo a comprar: "))

        if tipo_completo == 1:
            nombre_completo = completo
            precio = 1200
            cantidad = int(input(f'''Seleccione cuantos {completo} desea comprar: '''))
        if tipo_completo == 2:
            nombre_completo = italiano
            precio = 1600
            cantidad = int(input(f'''Seleccione cuantos {italiano} desea comprar: '''))
        if tipo_completo == 3:
            nombre_completo = dinamico
            precio = 1700
            cantidad = int(input(f'''Seleccione cuantos {dinamico} desea comprar: '''))

        total_inicial = precio * cantidad
        adicional = str(input("¿Desea adicional?  S/N: ")).upper().strip()

        if adicional == "S":
            print((f'''------- MENU ADICIONALES -------
                    ADICIONALES                VALOR

                    1. Papas Fritas            $2.000
                    2. Bebida 500cc            $1.200
                    
                    '''))
            cantidad_papas = int(input(f'''Ingrese cantidad de {papas_fritas}: '''))
            cantidad_bebida = int(input(f'''Ingrese cantidad de {bebida}: '''))
            total_parcial = total_inicial + (cantidad_papas*precio_papas) + (cantidad_bebida+precio_bebida)
            total_final = total_parcial
        if adicional == "N":
            total_final = total_inicial

    print(f''' ------- TICKET -------
         {nombre_completo} {precio} X {cantidad}
         {papas_fritas} {precio_papas} X {cantidad_papas}
         {bebida} {precio_bebida} X {cantidad_bebida}

         Total a pagar: {total_final}
    ''')
    
    clientes_atendidos += 1
    total_recaudado += total_final

    if op_menu == 2:
        print(f'''Clientes atendidos: {clientes_atendidos} ''')
        print(f'''Total recaudado: {total_recaudado}''')

    if op_menu == 3:
        break
