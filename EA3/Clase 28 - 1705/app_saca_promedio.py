import os
# ---------- variables ------------------
notas = []      # --> lista vacia
cantidad = 3    # Cantidad de notas a ingresar
estado = ""     # APROBADO o REPROBADO

# ------- Código Principal ---------
os.system("cls")
for k in range(cantidad):
    notas.append(float(input("Ingrese nota: ")))

prom = sum(notas)/len(notas)
maximo = max(notas)
minimo = min(notas)
print(f'''
    Notas: {notas}
    Min: {minimo}  \t  Max:{maximo}
    Promedio: {prom}
      ''')
