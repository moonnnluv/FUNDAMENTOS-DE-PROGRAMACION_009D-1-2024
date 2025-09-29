# Ejercicio 2
# Crea un programa que te solicite la edad y la guarde en una cariable, la valide como numero y la imprima por pantalla
# En caso de error, debe manejarlo

flag = True

while flag:
    try:
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ", edad)
        flag = False # o break
    except:
        print("Ingrese una edad válida")