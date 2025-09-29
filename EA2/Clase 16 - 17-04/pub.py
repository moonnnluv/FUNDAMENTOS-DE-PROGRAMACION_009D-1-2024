import os

op_menu = " "
producto = " "
precio = 0
cantidad = 0
happy = "N"
total = 0

# menú

print ("Bienvenido/a! ")
print (" 1. Vodka Tonica       $5500")
print (" 2. Ron Cola       $5000")
print (" 3. Cerveza       $2000")
print (" 4. Bebida       $1500")
op_menu = int(input("Elija su opción: "))


if op_menu == "1":
    producto = "Vodka Tónica"
    precio = 5500

if op_menu == "2":
    producto = "Ron Cola"
    precio = 5000
    
if op_menu == "3":
    producto = "Cerveza"
    precio = 2000
    
if op_menu == "4":
    producto = "Bebida"
    precio = 1500
    
cantidad = int(input("¿Que cantidad de producto desea?: "))

happy = str(input("¿Con happy hour?: ")).upper()

# cálculo 

total = precio * cantidad

if happy == "S":
    total = total/2

os.system("cls")

print("------- TICKET -------")
print ("Producto: ", producto, " X ", cantidad," a $ ", precio, " c/u")
print ("$ ", total)