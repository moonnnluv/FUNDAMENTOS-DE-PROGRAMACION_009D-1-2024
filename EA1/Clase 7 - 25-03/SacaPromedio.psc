Proceso SacaPromedio
	// Menu ciclico
	
	Definir opcionMenu, estado Como Caracter;
	Definir nota1, nota2, nota3, promedio Como Real;
	
	opcionMenu = "1";
	
	Mientras opcionMenu <> "3" Hacer
		Limpiar Pantalla;
		Escribir "------- MENU -------";
		Escribir "1.   Sacar Promedio ";
		Escribir "2.   Cant. de aprobados/reprobados";
		Escribir "3.   Salir          ";
		Leer opcionMenu;
		
		
		Si opcionMenu == "1" Entonces
			Escribir "Ingrese nota 1: ";
			Leer nota1;
			Escribir "Ingrese nota 2: ";
			Leer nota2;
			Escribir "Ingrese nota 3: ";
			Leer nota3;
			
			promedio = (nota1+nota2+nota3)/3;
			
			Si promedio >= 4 Entonces
				estado = "aprobado";
			SiNo
				estado = "reprobado";
			FinSi
			
			Escribir  "El promedio del alumno/alumna es ", promedio;
			Escribir "El alumno/alumna está ", estado;
			Esperar Tecla;
		FinSi
		
		Si opcionMenu = "3" Entonces
			Escribir "Gracias por usar Saca Promedio!";
			Esperar 5 segundos;
			Limpiar Pantalla;
		FinSi
		
	FinMientras
	
FinProceso
