Proceso MenuCiclico
	
	Definir opcionMenu Como Caracter;
	
	opcionMenu = "1";
	
	Mientras opcionMenu <> "3" Hacer
		Limpiar Pantalla;
		Escribir "------- MENU -------";
		Escribir "Opcion 1";
		Escribir "Opcion 2";
		Escribir "Salir";
		
		si opcionMenu == "1" Entonces
			Escribir "Opcion 1";
			Esperar Tecla;
		FinSi
		
		si opcionMenu == "2" Entonces
			Escribir "Opcion 2";
			Esperar Tecla;
		FinSi
		
		si opcionMenu == "3" Entonces
			Escribir "Saliendo...";
			Esperar 1 Segundos;;
		FinSi
	FinMientras
	
FinProceso
