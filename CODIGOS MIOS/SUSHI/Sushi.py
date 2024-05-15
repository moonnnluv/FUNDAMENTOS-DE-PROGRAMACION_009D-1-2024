'''
En un delivery de Sushi vende 4 tipos de Sushi:
Pikachu Roll $4500
Otaku Roll $5000
Pulpo Venenoso Roll $5200
Anguila Eléctrica Roll $4800

La empresa le ha solicitado a usted, que genere una pequeña aplicación en Python para tomar el pedido de un cliente el cuál puede ir agregando Rolls a través de un menú uno por uno con solo seleccionar la opción (1 a 4)

La aplicación debe mostrar en un menú los Rolls que agregará el usuario, esto se debe repetir hasta que el usuario decida que su pedido está completo.

Luego de ello, debe preguntar al usuario si posee un código de descuento.
En caso de que posea el código, deberá ingresarlo. Si el código ingresado es “soyotaku”, debe realizar un 10% de descuento al total del pedido, en caso contrario enviar el mensaje “código no válido” y dar al usuario la opción de reingresar el código o volver al menú
tecleando “X”

Una vez realizado los pasos anteriores, debe mostrar el detalle del pedido contabilizando el total de productos y la cantidad de cada uno de ellos y si aplica o no el descuento


****************************** 
TOTAL PRODUCTOS:4
******************************
Pikachu Roll : 2 
Otaku Roll : 1
Pulpo Venenoso Roll: 1 
Anguila Eléctrica Roll: 0
****************************** 
Subtotal por pagar: $19200
Descuento por código: $1920 
TOTAL: $17280

'''

# Variables

opcion = " "
cantidad = 0
precio = 0
precio_inicial = 0
precio_parcial = 0
precio_final = 0
descuento = 'N'
valor_descuento = 0
codigo_descuento_valido = 'soyotaku'
total_productos = 0

# Cantidad Rolls

cantidad_pikachu = 0
cantidad_otaku = 0
cantidad_pulpoVenenoso = 0
cantidad_anguilaElectrica = 0



while True: # Ciclo hasta que se seleccione un roll o se presione 'X'
      print(f'''                ------- MENU -------
               Roll                     Precio
         1. Pikachu Roll                $4500
         2. Otaku Roll                  $5000
         3. Pulpo Venenoso Roll         $5200
         4. Anguila Eléctrica Roll      $4800
               
            ''')
      opcion = input("Seleccione un roll (1-4) o presione 'X' para terminar: ").upper()

      if opcion == "X":
            # Terminar el código
            break 
      elif opcion == "1":
            cantidad_pikachu += int(input("Ingrese cantidad de Pikachu Roll: ")) # Sumar cantidad a lo global del Roll (se repite en cada opcion == " ")
            precio = 4500
            precio_inicial += precio * cantidad_pikachu # Sumar precio a lo global del Roll (se repite en cada opcion == " ")
      elif opcion == "2":
            cantidad_otaku += int(input("Ingrese cantidad de Otaku Roll: "))
            precio = 5000
            precio_inicial += precio * cantidad_otaku
      elif opcion == "3":
            cantidad_pulpoVenenoso += int(input("Ingrese cantidad de Pulpo Venenoso Roll: "))
            precio = 5200
            precio_inicial += precio * cantidad_pulpoVenenoso
      elif opcion == "4":
            cantidad_anguilaElectrica += int(input("Ingrese cantidad de Anguila Eléctrica Roll: "))
            precio = 4800
            precio_inicial += precio * cantidad_anguilaElectrica
      else:
            print("Opción invalida")
            continue # Volver al inicio del bucle
            
      # Cantidad Global
      total_productos = cantidad_pikachu + cantidad_otaku + cantidad_pulpoVenenoso + cantidad_anguilaElectrica 

# Teniendo productos, se calcula el posible descuento y ticket
if total_productos > 0:
      descuento = str(input("¿Posee descuento? (S/N): ")).upper()

      if descuento == 'S':
            codigo_descuento = str(input("Ingrese codigo de descuento: ")).lower()
            if codigo_descuento == codigo_descuento_valido:
                  valor_descuento = precio_inicial * 0.1 # Calcular el 10%
                  precio_final = precio_inicial - valor_descuento
            else:
                  print("Codigo no valido")
                  precio_final = precio_inicial # Se mantiene al ingresar codigo equivocado
      else:
            precio_final = precio_inicial # Se mantiene al no existir descuento


      # Boleta final 

      print(f'''  ****************************** 
                  TOTAL PRODUCTOS: {total_productos}
                  ******************************
                  Pikachu Roll                {cantidad_pikachu}
                  Otaku Roll                  {cantidad_otaku}
                  Pulpo Venenoso Roll         {cantidad_pulpoVenenoso}
                  Anguila Eléctrica Roll      {cantidad_anguilaElectrica}
                        ******************************
                        Subtotal por pagar: $ {precio_inicial}
                        Descuento por codigo: $ {valor_descuento}
                        TOTAL: $ {precio_final}
      ''')     
     
      
      

