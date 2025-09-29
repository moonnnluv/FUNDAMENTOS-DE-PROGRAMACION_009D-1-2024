Proceso AppFotocopiadora
	Definir opcion_menu Como Caracter;
	Definir hojas Como Entero;
	Definir total Como Real;
	Definir total_recaudado Como Real;
	Definir cant_clientes Como Entero;
	Definir cant_hojas Como Entero;
	
	opcion_menu="1";
	cant_clientes=0;
	cant_hojas=0;
	total_recaudado=0;
	
	Mientras opcion_menu<>"3" Hacer
		Limpiar Pantalla;
		Escribir "---- App Fotocopiadora ----";
		Escribir "1. Realizar venta fotocopiado";
		Escribir "2. Ver reporte				";
		Escribir "3. Salir						";
		leer opcion_menu;
		
		Si opcion_menu=="1" Entonces
			Limpiar Pantalla;
			Escribir "---- FOTOCOPIADO ----";
			Repetir
				Escribir "Ingrese la cantidad de hojas";
				Leer hojas;
			Hasta Que hojas>0;			
			
			Si hojas>30 Entonces
				total = 20*hojas*0.9;
			SiNo
				total = 20*hojas;
			FinSi
		//---------------- ESTADISTICAS -------------------
			
			total_recaudado = total_recaudado + total;
			
			cant_clientes = cant_clientes + 1;
			
			cant_hojas = cant_hojas + hojas;
		//-------------------------------------------------
			
			Escribir "-----Ticket ----";
			Escribir hojas,"X $20 =",total;
			Si hojas>30 Entonces
				Escribir "<< Incluye descuento >>";
			FinSi
			Esperar Tecla;
		FinSi
		
		Si opcion_menu=="2" Entonces
			Limpiar Pantalla;
			Escribir "----- REPORTE ------";
			Escribir "Total recaudado $",total_recaudado;
			Escribir "Cant. clientes: ",cant_clientes;
			Escribir "Cant. hojas utilizadas:",cant_hojas;
			Esperar Tecla;
		FinSi
		
		Si opcion_menu=="3" Entonces
			
		FinSi
	FinMientras
	
	
FinProceso
