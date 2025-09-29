Proceso Pub
	Definir Opcion Como Entero;
	Definir Cantidad Como Entero;
	Definir HappyHour Como Caracter;
	Definir Total Como Entero;
	Definir Precio Como Entero;
	Definir Producto Como Caracter;
	
	Escribir  "N°       Producto       Precio";
	Escribir  "1.       Vodka Tonica       $5500";
	Escribir  "2.       Ron Cola       $5000";
	Escribir  "3.       Cerveza       $2000";
	Escribir  "4.       Bebida       $1500";
	
	Escribir "Ingrese opcion: ";
	Leer Opcion;
	
	Escribir "Ingrese cantidad: ";
	Leer Cantidad;
	
	Escribir "¿Happy Hour? ";
	Leer HappyHour;
	
	Si Opcion==1 Entonces
		Producto <- 'Vodka Tonica';
		Precio <- 5500;
	SiNo
		Si Opcion == 2 Entonces
			Producto = "Ron cola";
			Precio = 5000;
		SiNo
			Si Opcion == 3 Entonces
				Producto = "Cerveza";
				Precio = 2000;
			SiNo
				Si Opcion == 4 Entonces
					Producto = "Bebida";
					Precio = 1500;
				FinSi
			FinSi
		FinSi
	FinSi
	
	Total = Precio * Cantidad;
	
	Si HappyHour == "Si" Entonces
		Total = Total /2;
	FinSi
	
	Escribir "------- Boleta de compra -------";
	Escribir "Valor a pagar $ ", Total;
	
	
FinProceso
