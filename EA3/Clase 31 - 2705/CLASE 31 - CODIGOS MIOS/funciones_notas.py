def sacar_promedio(nota1, nota2, nota3):
    suma = nota1 + nota2 + nota3
    promedio = suma/3
    promedio = round(promedio, 1) # 1 decimal
    return promedio


def validar_nota(nota): #  Nota en rango 1 a 7
    if 1 <= nota <= 7:
        return True
    else:
        return False
    

def estado(promedio):
    if promedio >= 4:
        return "APROBADO"
    else:
        return "REPROBADO"

    
def nota_examen(promedio):
    promedio = promedio * 0.6
    examen = (4 - promedio)/0.4
    examen = round(examen, 1)
    return examen
    
def ticket(nota1, nota2, nota3, promedio, estado):
    print(f'''
    \t \t   ======= TICKET =======
          Nota 1: {nota1} \t Nota 2: {nota2} \t Nota 3: {nota3}
    	  Promedio: {promedio}
          Estado: {estado}
        
          Necesitas un {nota_examen(promedio)} en el examen para aprobar

          ''')


   