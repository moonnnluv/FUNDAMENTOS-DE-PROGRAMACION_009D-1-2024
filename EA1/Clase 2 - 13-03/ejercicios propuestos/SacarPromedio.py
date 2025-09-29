"""
Proceso SacarPromedio
	
	Definir nota1, nota2, nota3 Como Real;
	Definir suma, promedio Como Real;
	Definir estado Como Caracter;
	
	Escribir "Ingrese nota1";
	Leer nota1;
	
	Escribir "Ingrese nota2";
	Leer nota2;
	
	Escribir "Ingrese nota3";
	Leer nota3;

	suma = nota1+nota2+nota3;
	promedio = suma/3;
	
	Si promedio>=4 Entonces
		estado = "APROBADO";
	SiNo
		estado = "REPROBADO";
	FinSi
	
	Escribir "---- RESULTADO ----";
	Escribir "Promedio:", promedio;
	Escribir "Estado:", estado;

	
FinProceso
"""

nota1 = int(input("Ingrese Nota 1: "))
nota2 = int(input("Ingrese Nota 2: "))
nota3 = int(input("Ingrese Nota 3: "))

suma = nota1+nota2+nota3
promedio = suma/3

if promedio >= 4:
    estado = "Aprobado"
else:
    estado = "Reprobado"

print("Resultado")
print("Promedio: ", promedio)
print("Estado:", estado)
    
