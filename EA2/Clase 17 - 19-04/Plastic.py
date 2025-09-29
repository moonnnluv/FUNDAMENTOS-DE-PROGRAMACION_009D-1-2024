# Variables

op_menu = " "
producto = " "
precio = 0
cantidad = 0
mayorista = False
descuento = 0
pago_efectivo = "N"
total_pago = 0

# Menú

print("Bienvenido/a a PlasTic, ofrecemos los siguientes productos: ")
print(" ")
print("Producto              Valor Unitario")
print("1. Tazón                  $ 500")
print("2. Llavero                $ 200")
print("3. Polera estampada       $ 3.000")

op_menu = int(input("Ingrese producto a elegir: "))
cantidad = (int(input("Ingrese cantidad: ")))

if op_menu == "1":
    producto = "Tazón"
    cantidad = cantidad
    if cantidad >= 100:
        precio = 300
        mayorista = True
    else:
        precio = 500
        
if op_menu == "2":
    producto = "Llavero"
    cantidad = cantidad
    if cantidad >= 300:
        precio = 150
        mayorista = True
    else:
        precio = 200
        
if op_menu == "3":
    producto = "Polera estampada"
    cantidad = cantidad
    if cantidad >= 50:
        precio = 2000
        mayorista = True
    else:
        precio = 3000
        

# Cálculo precio sin descuento
    
total_pago = precio * cantidad

# Aplicar descuento si corresponde

pago_efectivo = str(input("¿Paga con efectivo?")).upper()

if mayorista == True and pago_efectivo == "S":
    descuento = total_pago * 0.10
    pago_final = total_pago - descuento
else:
    pago_final = total_pago
    
# Boleta

print ("------- BOLETA -------")
print ("Producto: ", producto)
print ("Cantidad: ", cantidad)
print ("Precio: $ ", precio)
print ("Pago: ", total_pago)
print ("Descuento: $", descuento)
print ("Pago final: $", pago_final)