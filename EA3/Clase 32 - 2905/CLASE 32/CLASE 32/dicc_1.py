import os

usuario = {}  #--> diccionario vacio

rut = str(input("Ingrese rut: ")).strip().upper()
nombre = str(input("Ingrese nombre:")).strip()
edad = int(input("Ingrese edad: "))

usuario = {
    "rut": rut,
    "nombre":nombre,
    "edad":edad
}

print(usuario)

# Dentro de las funciones propias de los diccionarios tenemos:
print("\n -- podemos imprimir TODAS LAS KEY ---")
print(usuario.keys())

print("\n -- podemos imprimir TODOS LOS VALUES ---")
print(usuario.values())

print("\n -- podemos recorrer items, un item es Key->value")
for k, v in usuario.items():
    print(f'''
        Clave: {k}   Valor: {v}
          
          ''')

