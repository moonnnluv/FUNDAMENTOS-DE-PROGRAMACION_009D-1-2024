Proceso AppCafeteria
	Definir opcion_menu Como Caracter;
	Definir opcion_cafe Como Entero;
	Definir nombre_cafe Como Caracter;
	Definir precio_cafe Como Entero;
	Definir desea_agregado Como Caracter; // S/N
	Definir opcion_agregado Como Entero;
	Definir nombre_agregado Como Caracter;
	Definir precio_agregado Como Entero;	
	Definir total Como Entero;
	Definir pagar, vuelto Como Entero;
	Definir cant_ventas Como Entero;
	Definir cant_espresso, cant_cappuccino Como Entero;
	Definir cant_latte, cant_mocha Como Entero;
	Definir total_recaudado Como Entero;
	
	opcion_menu="1";
	cant_ventas=0;
	cant_espresso=0;
	cant_cappuccino=0;
	cant_latte=0;
	cant_mocha=0;
	total_recaudado=0;
	
	Mientras opcion_menu<>"3" Hacer
		Limpiar Pantalla;
		Escribir "----- App Cafetería -----";
		Escribir "1. Realizar venta de café";
		Escribir "2. Ver estadísticas		";
		Escribir "3. Salir					";
		Escribir "Elija opción:				";
		Leer opcion_menu;
		
		Si opcion_menu=="1" Entonces
			Limpiar Pantalla;
			Escribir "---------- MENÚ CAFÉ -----------";
			Escribir "N°     producto     precio";
			Escribir "1	     Espresso     $750";
			Escribir "2	     Cappuccino    $850";
			Escribir "3	     Latte     $800";
			Escribir "4	     Mocha     $830";
			Escribir "Ingrese opción del menú:";
			Leer opcion_cafe;
			
			Si opcion_cafe==1 Entonces
				nombre_cafe="Espresso";
				precio_cafe=750;
				cant_espresso= cant_espresso+1;
			FinSi
			
			Si opcion_cafe==2 Entonces
				nombre_cafe="Cappuccino";
				precio_cafe=850;
				cant_cappuccino=cant_cappuccino+1;
			FinSi
			
			Si opcion_cafe==3 Entonces
				nombre_cafe="Latte";
				precio_cafe=800;
				cant_latte=cant_latte+1;
			FinSi
			
			Si opcion_cafe==4 Entonces
				nombre_cafe="Mocha";
				precio_cafe=830;
				cant_mocha=cant_mocha+1;
			FinSi
			
			Escribir "¿Desea agregado ?  S/N";
			Leer desea_agregado;
			
			Si desea_agregado=="S" Entonces
				Escribir "----- AGREGADOS ------------";
				Escribir "1. Leche         $300";
				Escribir "2. Chocolate     $200";
				Escribir "3. Ambos         $500";
				Escribir "Elija opción:  ";
				Leer opcion_agregado;
				
				Si opcion_agregado==1 Entonces
					nombre_agregado="Leche";
					precio_agregado=300;
				FinSi
				Si opcion_agregado==2 Entonces
					nombre_agregado="Chocolate";
					precio_agregado=200;
				FinSi
				Si opcion_agregado==3 Entonces
					nombre_agregado="Leche y chocolate";
					precio_agregado=500;
				FinSi		
			FinSi
			
			//--------- estamos calculando el total de la compra -----
			Si desea_agregado=="S" Entonces
				total = precio_cafe + precio_agregado;
			SiNo
				total = precio_cafe;
			FinSi
			
			Escribir "Total compra $",total;
			
			Repetir
				Escribir "¿Con cuánto paga?";
				Leer pagar;
			Hasta Que pagar>=total;
			
			
			
			Si pagar>total Entonces
				vuelto =pagar-total;
			FinSi
			
			//----------- variables estadisticas ------------
			cant_ventas = cant_ventas+1;
			
			total_recaudado = total_recaudado+total;
			
			// ----- Imprimimos la boleta ----------------------------
			Limpiar Pantalla;
			Escribir "Tipo café:",nombre_cafe;
			Si desea_agregado=="S" Entonces
				Escribir "Agregados:", nombre_agregado;
			FinSi
			Escribir "Total compra:$ ",total;
			Escribir "Cancelo con:$",pagar;
			Escribir "Vuelto:$",vuelto;		
			
			Esperar Tecla;			
		FinSi
		
		Si opcion_menu=="2" Entonces
			Limpiar Pantalla;
			Escribir "-------- ESTADÍSTICAS ------------";
			Escribir "Cant. de ventas: ",cant_ventas;
			Escribir "----------------------------------";
			Escribir "Cant. Espresso: ",cant_espresso;
			Escribir "Cant. Cappuccino: ",cant_cappuccino;
			Escribir "Cant. Latte: ",cant_latte;
			Escribir "Cant. Mocha: ",cant_mocha;
			Escribir "----------------------------------";
			Escribir "TOTAL recaudado $",total_recaudado;
			Esperar Tecla;
		FinSi
		
	FinMientras
	
	
FinProceso
