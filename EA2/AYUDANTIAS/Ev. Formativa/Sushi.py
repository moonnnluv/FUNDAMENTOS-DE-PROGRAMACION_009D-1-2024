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
Otaku Roll :1
Pulpo Venenoso Roll:1 
Anguila Eléctrica Roll:0
****************************** 
Subtotal por pagar: $19200
Descuento por código: $1920 
TOTAL: $17280

'''

# Variables

opcion = 0
cantidad = 0
precio = 0
precio_parcial = 0
precio_final = 0
descuento = 'N'
codigo_descuento = 'soyotaku'




opcion =(f''' ------- MENU -------
               Roll                Precio
         1. Pikachu Roll           $4500
         2. Otaku Roll             $5000
         3. Pulpo Venenoso         $5200
         4. Anguila Eléctrica      $4800
         Ingrese opción: ''')

if opcion in (1,2,3,4):
      cantidad = int(input("Ingrese cantidad: "))
else:
      print("opción invalida")
      
      
if opcion == 1:
      precio = 4500
      precio_inicial = precio * cantidad
      


      
descuento = str(int("¿Posee descuento?: "))

if descuento == 'S':
      if codigo_descuento == True:
            
            precio_parcial = precio_inicial * 0.1
            precio_final = precio_inicial - precio_parcial
      else:
            precio_final = precio_inicial
      
      

