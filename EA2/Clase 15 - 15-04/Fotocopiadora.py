# Fotocopiadora

'''Realice un programa que determine el pago a realizar a una fotocopiadora, en donde el precio por cada fotocopiadora es de $20. 
Al imprimir más de 30 fotocopias se realiza un descuento al total de la compra del 10%.'''



hojas = int(input("Ingrese cantidad de hojas: "))

if hojas > 30:
    total = hojas * 20 * 0.9
else:
    total = hojas * 20
    
total = int(total)
    
print ("Usted imprimió ", hojas)
print ("Su valor es: $", total)