Proceso AppProductoraFoodAndDance
	Definir opcion_menu Como Caracter;  //--> opci�n de men� seleccionada por el usuario
	Definir text_asistentes Como Caracter;//--> cantidad de asistentes forma texto 
	Definir opcion_cant_menu Como Caracter;//--> opci�n del men� segundario para determinar 1 o 2 opciones de men�
	Definir precio_cant_menu Como Entero; //--> monto que representa el precio de la opcion(es) de men� seleccionada
	Definir con_buffet_postres Como Caracter; //--> Si lleva buffet se le sumar� un monto fijo de $500.000
	Definir total como Entero; //--> monto final a pagar
	
	//---- variables para app c�clica ------
	Definir op_menu_principal Como Caracter;
	Definir total_recaudado como Entero; // acumulador
	Definir cant_clientes_atendidos Como Entero; // contador
	Definir cant_clientes_postre Como Entero; // contador
	
	
	op_menu_principal="1";
	total_recaudado=0;
	cant_clientes_atendidos=0;
	cant_clientes_postre=0;
	
	Mientras  op_menu_principal <> "3" Hacer
		Limpiar Pantalla;
		Escribir "------ MEN� PRINCIPAL ------";
		Escribir "1. Realizar venta evento		";
		Escribir "2. Ver estad�sticas			";
		Escribir "3. Salir						";
		Leer op_menu_principal;	
		
		Si op_menu_principal =="1" Entonces
			Limpiar Pantalla;
			Escribir "  ===================== Food and Dance  =====================		";
			Escribir "      Cant. de    |                Tarifas			 			";
			Escribir "     Asistentes   |   Precio 1 men�   |   Precio 2 op. men�s		";
			Escribir "  ---------------------------------------------------------		";
			Escribir "  1.-  Hasta 50   |   $1.000.000      |     $1.500.000			";
			Escribir "  2.- Hasta 100   |   $1.800.000      |     $2.300.000			";
			Escribir "  3.- Hasta 200   |   $3.500.000      |     $4.000.000			";
			Escribir "  4.- Hasta 300   |   $4.100.000      |     $4.600.000			";
			Escribir "  																";
			Escribir "  Elija opci�n:	";
			Leer opcion_menu;
			
			
			//------------------  Seg�n la opci�n de men� seleccionada anterioremente se determina la cantidad de asistentes 
			// ------------------ y DENTRO de cada condici�n se ofrece la cantidad de opciones de men� 
			//------------------- con esto ultimo determinamos el precio a cobrar    ---------------------
			
			Si opcion_menu=="1" Entonces
				text_asistentes="Hasta 50";
				Escribir "  _______________________________________________";
				Escribir "  |                Tarifas			 			";
				Escribir "  |   Precio 1 men�   |   Precio 2 op. men�s		";
				Escribir "  ------------------------------------------		";
				Escribir "  |   $1.000.000      |     $1.500.000			";
				Escribir "													";
				Escribir " �Cu�ntas opciones de men� desea?  1/2 			";
				Leer opcion_cant_menu;
				Si opcion_cant_menu=="1" Entonces
					precio_cant_menu=1000000;
				FinSi
				Si opcion_cant_menu=="2" Entonces
					precio_cant_menu=1500000;
				FinSi
			FinSi
			
			Si opcion_menu=="2" Entonces
				text_asistentes="Hasta 100";
				Escribir "  _______________________________________________";
				Escribir "  |                Tarifas			 			";
				Escribir "  |   Precio 1 men�   |   Precio 2 op. men�s		";
				Escribir "  ------------------------------------------		";
				Escribir "  |   $1.800.000      |     $2.300.000			";
				Escribir "													";
				Escribir " �Cu�ntas opciones de men� desea?  1/2 			";
				Leer opcion_cant_menu;
				Si opcion_cant_menu=="1" Entonces
					precio_cant_menu=1800000;
				FinSi
				Si opcion_cant_menu=="2" Entonces
					precio_cant_menu=2300000;
				FinSi
			FinSi
			
			Si opcion_menu=="3" Entonces
				text_asistentes="Hasta 200";
				Escribir "  _______________________________________________";
				Escribir "  |                Tarifas			 			";
				Escribir "  |   Precio 1 men�   |   Precio 2 op. men�s		";
				Escribir "  ------------------------------------------		";
				Escribir "  |   $3.500.000      |     $4.000.000			";
				Escribir "													";
				Escribir " �Cu�ntas opciones de men� desea?  1/2 			";
				Leer opcion_cant_menu;
				Si opcion_cant_menu=="1" Entonces
					precio_cant_menu=3500000;
				FinSi
				Si opcion_cant_menu=="2" Entonces
					precio_cant_menu=4000000;
				FinSi
			FinSi
			Si opcion_menu=="4" Entonces
				text_asistentes="Hasta 300";
				Escribir "  _______________________________________________";
				Escribir "  |                Tarifas			 			";
				Escribir "  |   Precio 1 men�   |   Precio 2 op. men�s		";
				Escribir "  ------------------------------------------		";
				Escribir "  |   $4.100.000      |     $4.600.000			";
				Escribir "													";
				Escribir " �Cu�ntas opciones de men� desea?  1/2 			";
				Leer opcion_cant_menu;
				Si opcion_cant_menu=="1" Entonces
					precio_cant_menu=4100000;
				FinSi
				Si opcion_cant_menu=="2" Entonces
					precio_cant_menu=4600000;
				FinSi
			FinSi
			
			
			
			//------------------  El programa pregunta al usuario si desea Buffet  ---------------------------------	
			
			Escribir "   ___________________________________________________	";
			Escribir "  |    Disponemos de servicio de Buffet de Postres   |	";
			Escribir "  |   Por un monto fijo de $500.000                  |	";
			Escribir "   ---------------------------------------------------	";
			Escribir "  														";
			Escribir "															";
			Escribir " �Desea incorporar el buffet de postres?  S/N			";
			Leer con_buffet_postres;
			
			
			//------------------  Determinamos el total de la compra    ---------------------------------	
			
			Si con_buffet_postres=="S" o con_buffet_postres=="s" Entonces
				total = precio_cant_menu + 500000;
				cant_clientes_postre = cant_clientes_postre+1;
			SiNo
				total = precio_cant_menu;		
			FinSi			
			//------------------  Cerramos transacci�n con la boleta  ---------------------------------
			
			Escribir "   _______________________________________________________________	";
			Escribir "  |    		Eventos Food and Dance                              |	";
			Escribir "  |    ", text_asistentes ,"         $",precio_cant_menu,"       |	";
			
			Si con_buffet_postres=="S" o con_buffet_postres=="s" Entonces
				Escribir "  |    Buffet de Postres         $500.000                    |	";		
			FinSi
			Escribir "  |    TOTAL                         $", total,"					|	";	                                      
			Escribir "  |_______________________________________________________________	";
			
			
			//------------- estad�sticas -------------------
			cant_clientes_atendidos = cant_clientes_atendidos+1;
			total_recaudado = total_recaudado + total;
			
			
			Esperar Tecla;
		FinSi  //-------------> FIN CLAUSULA 1  ----------------------------
		
		Si op_menu_principal =="2" Entonces
			Limpiar Pantalla;
			Escribir "------- Estad�sticas -----------";
			Escribir "Cant. clientes atendidos:",cant_clientes_atendidos;
			Escribir "Total recaudado $",total_recaudado;
			Escribir "Cant. clientes piden postre:",cant_clientes_postre;			
			Esperar Tecla;
		FinSi
		
		
		
	FinMientras
	
	
	
	
	
	
	
	//------------------  El programa inicia con el men� principal  ---------------------------------
	
	Limpiar Pantalla;
	Escribir "  ===================== Food and Dance  =====================		";
	Escribir "      Cant. de    |                Tarifas			 			";
	Escribir "     Asistentes   |   Precio 1 men�   |   Precio 2 op. men�s		";
	Escribir "  ---------------------------------------------------------		";
	Escribir "  1.-  Hasta 50   |   $1.000.000      |     $1.500.000			";
	Escribir "  2.- Hasta 100   |   $1.800.000      |     $2.300.000			";
	Escribir "  3.- Hasta 200   |   $3.500.000      |     $4.000.000			";
	Escribir "  4.- Hasta 300   |   $4.100.000      |     $4.600.000			";
	Escribir "  																";
	Escribir "  Elija opci�n:	";
	Leer opcion_menu;
	
	
	//------------------  Seg�n la opci�n de men� seleccionada anterioremente se determina la cantidad de asistentes 
	// ------------------ y DENTRO de cada condici�n se ofrece la cantidad de opciones de men� 
	//------------------- con esto ultimo determinamos el precio a cobrar    ---------------------
	
	Si opcion_menu=="1" Entonces
		text_asistentes="Hasta 50";
		Escribir "  _______________________________________________";
		Escribir "  |                Tarifas			 			";
		Escribir "  |   Precio 1 men�   |   Precio 2 op. men�s		";
		Escribir "  ------------------------------------------		";
		Escribir "  |   $1.000.000      |     $1.500.000			";
		Escribir "													";
		Escribir " �Cu�ntas opciones de men� desea?  1/2 			";
		Leer opcion_cant_menu;
		Si opcion_cant_menu=="1" Entonces
			precio_cant_menu=1000000;
		FinSi
		Si opcion_cant_menu=="2" Entonces
			precio_cant_menu=1500000;
		FinSi
	FinSi
	
	Si opcion_menu=="2" Entonces
		text_asistentes="Hasta 100";
		Escribir "  _______________________________________________";
		Escribir "  |                Tarifas			 			";
		Escribir "  |   Precio 1 men�   |   Precio 2 op. men�s		";
		Escribir "  ------------------------------------------		";
		Escribir "  |   $1.800.000      |     $2.300.000			";
		Escribir "													";
		Escribir " �Cu�ntas opciones de men� desea?  1/2 			";
		Leer opcion_cant_menu;
		Si opcion_cant_menu=="1" Entonces
			precio_cant_menu=1800000;
		FinSi
		Si opcion_cant_menu=="2" Entonces
			precio_cant_menu=2300000;
		FinSi
	FinSi
	
	Si opcion_menu=="3" Entonces
		text_asistentes="Hasta 200";
		Escribir "  _______________________________________________";
		Escribir "  |                Tarifas			 			";
		Escribir "  |   Precio 1 men�   |   Precio 2 op. men�s		";
		Escribir "  ------------------------------------------		";
		Escribir "  |   $3.500.000      |     $4.000.000			";
		Escribir "													";
		Escribir " �Cu�ntas opciones de men� desea?  1/2 			";
		Leer opcion_cant_menu;
		Si opcion_cant_menu=="1" Entonces
			precio_cant_menu=3500000;
		FinSi
		Si opcion_cant_menu=="2" Entonces
			precio_cant_menu=4000000;
		FinSi
	FinSi
	Si opcion_menu=="4" Entonces
		text_asistentes="Hasta 300";
		Escribir "  _______________________________________________";
		Escribir "  |                Tarifas			 			";
		Escribir "  |   Precio 1 men�   |   Precio 2 op. men�s		";
		Escribir "  ------------------------------------------		";
		Escribir "  |   $4.100.000      |     $4.600.000			";
		Escribir "													";
		Escribir " �Cu�ntas opciones de men� desea?  1/2 			";
		Leer opcion_cant_menu;
		Si opcion_cant_menu=="1" Entonces
			precio_cant_menu=4100000;
		FinSi
		Si opcion_cant_menu=="2" Entonces
			precio_cant_menu=4600000;
		FinSi
	FinSi
	
	
	
	//------------------  El programa pregunta al usuario si desea Buffet  ---------------------------------	
	
	Escribir "   ___________________________________________________	";
	Escribir "  |    Disponemos de servicio de Buffet de Postres   |	";
	Escribir "  |   Por un monto fijo de $500.000                  |	";
	Escribir "   ---------------------------------------------------	";
	Escribir "  														";
	Escribir "															";
	Escribir " �Desea incorporar el buffet de postres?  S/N			";
	Leer con_buffet_postres;
	
	
	//------------------  Determinamos el total de la compra    ---------------------------------	
	
	Si con_buffet_postres=="S" o con_buffet_postres=="s" Entonces
		total = precio_cant_menu + 500000;
	SiNo
		total = precio_cant_menu;		
	FinSi
	
	
	
	//------------------  Cerramos transacci�n con la boleta  ---------------------------------
	
	Escribir "   _______________________________________________________________	";
	Escribir "  |    		Eventos Food and Dance                              |	";
	Escribir "  |    ", text_asistentes ,"         $",precio_cant_menu,"       |	";
	
	Si con_buffet_postres=="S" o con_buffet_postres=="s" Entonces
		Escribir "  |    Buffet de Postres         $500.000                    |	";		
	FinSi
	Escribir "  |    TOTAL                         $", total,"					|	";	                                      
	Escribir "  |_______________________________________________________________	";
	
	
FinProceso
