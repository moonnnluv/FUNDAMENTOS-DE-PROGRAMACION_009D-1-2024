
def calcular_imc(peso, estatura):
    return round(peso/estatura**2, 1)  # 1 decimal


def clasificar_imc(imc):
    clasificacion = ""
    if imc < 18.5:
        clasificacion = "Bajo Peso"
    elif 18.5 <= imc <= 24.9:
        clasificacion = "Normal"
    elif 25 <= imc <= 29.9:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    return clasificacion
