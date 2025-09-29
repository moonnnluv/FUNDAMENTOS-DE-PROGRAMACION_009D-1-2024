# Ejercicio 3
# Cree una lista de nombres de alumnos, y luego imprima hacia abajo acompañado de un numero de indice hacia abajo

lista_nombres = ["Juan", "Pedro", "Jose", "Maria"]

indice = 1
for elementos in lista_nombres:
    #print(indice,".",elementos)
    print(f"{indice}. {elementos}")
    indice = indice+1