// . Genere un algoritmo que pida el Ingreso del Nombre de Una Persona,  Su estatura en Metros y su peso en Kilogramos.
// Luego entregue el Índice de Masa Corporal (ICM) determinado por la siguiente fórmula: Peso / Estatura ^2
// Luego de entregar este valor entregue el resultado de la condición de peso de acuerdo a la siguiente clasificación:
	
// Bajo Peso	Menor que 18.5	
// Normal	Entre 18.5 y 24.9	
// Sobrepeso	Entre 25 y 29.9	
// Obesidad	Sobre o igual a 30	

// Secuencia Lógica:
// 1.	Se ingresa el nombre del usuario, se carga NOMBRE
// 2.	Se ingresa la estatura en metros, se carga ESTATURA
// 3.	Se ingresa el peso de la persona en kilogramos, se carga PESO
// 4.	Se calcula el IMC de la persona
// 5.	Se determina la clasificación de la persona de acuerdo al IMC
// a.	Si IMC es menor a 18.5 
// i.	La CLASIFICACION es "Bajo peso"
// b.	Si IMC está entre 18.5 y 24.9
// i.	La CLASIFICACION es "Normal"
// c.	Si IMC está entre 25 y 29.9
// i.	La CLASIFICACION es "Sobrepeso"
// d.	Si IMC es igual a mayor a 30
// i.	La CLASIFICACION es "Obesidad"
								
// 6.	Se imprime el ticket con los resultados.



Proceso IMC
	
	Definir nombre, resultado Como Caracter;
	Definir calculo_imc, estatura, peso Como Real;

	
	Escribir "Ingrese su nombre: ";
	Leer nombre;
	
	Escribir "Ingrese su peso (kg): ";
	Leer peso;
	
	Escribir "Ingrese su estatura (m): ";
	Leer estatura;
	
	calculo_imc = (peso) / (estatura)^2;
	
	// Bajo Peso	Menor que 18.5	
	// Normal	Entre 18.5 y 24.9	
	// Sobrepeso	Entre 25 y 29.9	
	// Obesidad	Sobre o igual a 30	
	
	si calculo_imc < 18.5 Entonces
		resultado = "Bajo peso";
	FinSi
	
	si calculo_imc > 18.5 y calculo_imc < 24.9 Entonces
		resultado = "Normal";
	FinSi
	
	si calculo_imc > 25 y calculo_imc < 29.9  Entonces
		resultado = "Sobrepeso";
	FinSi
	
	si calculo_imc >= 30  Entonces
		resultado = "Obesidad";
	FinSi
	
	Escribir "------- IMC -------";
	Escribir "Nombre:          ", nombre;
	Escribir "Peso:            ", peso;
	Escribir "Estarura:        ", estatura;
	Escribir "Su IMC es:        ", calculo_imc;
	Escribir "Usted se encuentra: ",resultado;
	
FinProceso
