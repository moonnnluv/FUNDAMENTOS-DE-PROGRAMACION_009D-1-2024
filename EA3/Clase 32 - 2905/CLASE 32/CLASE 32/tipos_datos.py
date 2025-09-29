import os

# Una estructura de dato, es una forma de representar
# información para que sea util
# Python posee diversidad de tipos de datos: conjuntos, 
# tuplas, diccionarios, etc

print("---- ejemplo de conjunto----")
# En un conjunto los datos no se pueden repetir
conjunto = {"A", 3, "B", "A"}
print(conjunto)

print("\n--- ejemplo de tupla ----")
# En una tupla NO SE PUEDEN MODIFICAR LOS DATOS
tupla_1 = ("222-2", "Pablo", 26)
print(tupla_1)

print("\n--- ejemplo de diccionario ----")
# En un diccionario los datos se almacenan con el concepto
# key -> value 
persona_1 = {
    "rut": "111-k",
    "nombre":"Pablo",
    "edad": 26
}
print(persona_1)

# LAS KEY SON INALTERABLES, pero los values se puede alterar
persona_1["nombre"] = "Carol" 
print(persona_1)

# Podemos agregar un nuevo Key->Value al diccionario
persona_1["carrera"] = "turismo"
print(persona_1)

