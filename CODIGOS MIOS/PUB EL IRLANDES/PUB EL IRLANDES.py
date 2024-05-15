# Variables

op_menu = 0
producto_bebestible = " "
producto_alimento = " "
bebestible_ticket = " "
papafrita_ticket = " "
completo_ticket = " "
precio_bebestible = 0
precio_papafrita = 0
precio_completos = 0
cantidad_bebestible = 0
cantidad_papafrita = 0
cantidad_completos = 0
total_bebestible = 0
total_papafrita = 0
total_completos = 0
total_alimento = 0
condicion_socio = " "
socio = True
cliente = " "
metodo_pago = " "
precio_parcial = 0
descuento = 0
precio_total = 0

# Estadisticas

cantidad_clientes = 0
total_recaudado = 0


while True:
    op_menu = str(input(f'''                      ------- MENU PRINCIPAL -------
                           1. Vender
                           2. Ver estadísticas
                           3. Salir
                           
                           Elija opcion: '''))


    if op_menu == "1":
        print("Bienvenido/a a El Irlandes, ofrecemos el siguiente menú")
        print("                                                        ")
        print(f'''                ------- MENU BEBESTIBLES -------
                                    
        Bebestible            Valor General            Valor Socio
                                    
        1. Cerveza                $5.000                 $3.000
        2. Whisky                 $13.000                $10.000
        3. Agua Mineral           $3.000                 $2.000 ''')
        
        producto_bebestible = int(input("Seleccione una opción: "))
        
        condicion_socio = str(input("¿Usted es socio de nuestro pub? (S/N): "))
        condicion_socio.upper()

        if condicion_socio == "N":
            socio == False
            cliente = "NO SOCIO"
        else:
            socio == True
            cliente = "SOCIO"

        if producto_bebestible == 1:
            bebestible_ticket = "Cerveza"
            if socio == False:
                precio_bebestible = 5000
            else:
                precio_bebestible = 3000

        if producto_bebestible == 2:
            bebestible_ticket = "Whisky"
            if socio == False:
                precio_bebestible = 13000
            else:
                precio_bebestible = 10000

        if producto_bebestible == 3:
            bebestible_ticket = "Agua Mineral"
            if socio == False:
                precio_bebestible = 3000
            else:
                precio_bebestible = 2000

        cantidad_bebestible = int(input("Seleccione la cantidad del producto elegido: "))

        total_bebestible = precio_bebestible * cantidad_bebestible


    
        menu_alimento =  print(f''' ------- MENU ALIMENTOS -------

            Alimento                   Valor General            Valor Socio

            1. Papas Fritas                $3.500                 $2.500
            2. Completo                    $4.500                 $3.500
                                ''') 
        
        # Papa Frita

        papafrita_ticket = "Papas fritas"
        cantidad_papafrita = int(input("Ingrese cantidad de Papas Fritas que desea comprar, en caso de no querer, ingrese 0: "))


        if socio == False:
            precio_papafrita = 3500
        else:
            precio_papafrita = 2500
                
        # Completos

        completo_ticket = "Completos"
        cantidad_completos = int(input("Ingrese cantidad de Completos que desea comprar, en caso de no querer, ingrese 0: "))

        if socio == False:
            precio_completos = 4500
        else:
            precio_completos = 3500


        total_papafrita = cantidad_papafrita * precio_papafrita
        total_completos = cantidad_completos * precio_completos

        total_alimento = total_papafrita + total_completos
        precio_parcial = total_bebestible + total_alimento

        metodo_pago = int(input(f'''Seleccione su método de pago: 
                                1. Efectivo (Posee un 10% de descuento!)
                                2. Tarjeta débito/crédito
                                '''))
        
        if metodo_pago == 1:
            descuento = precio_parcial * 0.1
            precio_total = precio_parcial - descuento
        else:
            precio_total = precio_parcial
            
        # Cambio en estadisticas

        cantidad_clientes = cantidad_clientes + 1
        total_recaudado = precio_total



        print(f''' ------- TICKET -------
            Cliente: {cliente}
            Bebestible: {cantidad_bebestible} {bebestible_ticket} a ${precio_bebestible} c/u
            Comida: {cantidad_papafrita} {papafrita_ticket} a ${precio_papafrita} c/u
                    {cantidad_completos} {completo_ticket} a ${precio_completos} c/u

            Subtotal: $ {precio_parcial}
            Descuento 10%: $ {descuento}
            Total: $ {precio_total}

        ''')
    elif op_menu == "2":
        print("Clientes atendidos: ", cantidad_clientes)
        print("Total recaudado: ", total_recaudado)

    elif op_menu == "3":
        print("¡Gracias por su visita!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")