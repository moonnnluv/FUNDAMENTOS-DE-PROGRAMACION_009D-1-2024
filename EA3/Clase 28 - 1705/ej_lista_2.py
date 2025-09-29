import os
os.system("cls")

notas = []   #--> lista vacia!!!

while True:
    notas.append(float(input("Ingrese nota: ")))
    
    # sum ...suma todos los elementos de la lista
    # len ..cuenta cuantos elementos tiene la lista
    prom = sum(notas)/len(notas)
    
    print(f'''
          notas: {notas}
          Promedio {prom}''')