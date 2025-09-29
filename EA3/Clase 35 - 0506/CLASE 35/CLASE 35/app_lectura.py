import os
import json  # --> gestion de json

# vamos a leer el json
with open('data.json', 'r', encoding='utf-8') as archivo:
    data = json.load(archivo)

# print(data)

# Recuerden que items() te va a devolver cada item
# del json ..y un item esta compuesto por k->v
for pais, valor in data.items():
    print(f'''
          Pais: {pais}
          Capital:{valor["capital"]}
          Población: {valor["población"]} hab.
          Superficie: {valor["superficie"]} m^2
          Moneda: {valor["moneda"]}
          Lengua: {valor["lengua"]}
          ========================''')
