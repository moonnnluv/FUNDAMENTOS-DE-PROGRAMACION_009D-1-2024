# Saca Promedio


import os
os.system("cls") # limpiar pantalla


nombre = str(input("Ingrese su nombre: "))
edad = str(input("Ingrese su edad: "))

nota_1 = float(input("Ingrese nota 1: "))
nota_2 = float(input("Ingrese nota 2: "))
nota_3 = float(input("Ingrese nota 3: "))

promedio = (nota_1 + nota_2 + nota_3)/3

if promedio >= 4:
    estado = "aprobado"
else:
    estado = "reprobado" 
    
    
    
os.system("cls")

print ("Su promedio es: ", promedio)
print ("Usted está ", estado)