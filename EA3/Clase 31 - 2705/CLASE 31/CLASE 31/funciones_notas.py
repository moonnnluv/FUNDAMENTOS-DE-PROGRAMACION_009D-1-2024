def sacar_promedio(nota1, nota2, nota3):
    prom = (nota1+nota2+nota3)/3
    prom = round(prom, 1)  # --> 1 decimal
    return prom


def determinar_estado(prom):
    if prom >= 4:
        return "APROBADO"
    else:
        return "REPROBADO"


def calcular_nota_min_examen(prom):
    nota_min = (4-prom*0.60)/0.40
    nota_min = round(nota_min, 1) # aprox. a 1 decimal
    return nota_min


def imprimir_ticket(nota1, nota2, nota3, prom, estado):
    print(f'''
    ========== ticket ===========
    Nota1:{nota1} \t Nota2:{nota2} \t Nota3:{nota3}
    Promedio: {prom}
    Nota mínima examen: {calcular_nota_min_examen(prom)}
    ''')


def validar_nota(nota):
    ''' Ingresa la nota y la función retornará
    True si esta en el rango 1 a 7, False
    en caso contrario   '''
    if 1 <= nota <= 7:
        return True
    else:
        return False
