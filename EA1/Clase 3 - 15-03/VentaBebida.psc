Proceso VentaBebida
	Definir opcion Como Entero;
	Definir nombreProducto Como Caracter;
	Definir precioProducto Como Entero;
	Definir cantidad, total Como Entero;
	
	Escribir "--------- MENÚ -------";
	Escribir "1. Coca Cola 		$900";
	Escribir "2. Fanta	 		$800";
	Escribir "3. Sprite 		$750";
	Escribir "						";
	Escribir "Ingrese opción:		";
	Leer opcion;
	
	Si opcion==1 Entonces
		nombreProducto="Coca Cola";
		precioProducto=900;
	FinSi
	Si opcion==2 Entonces
		nombreProducto="Fanta";
		precioProducto=800;
	FinSi
	Si opcion==3 Entonces
		nombreProducto="Sprite";
		precioProducto=750;
	FinSi
	
	Escribir "Ingrese la cantidad de ",nombreProducto;
	Leer cantidad;
	
	total = precioProducto*cantidad;
	
	Esperar 1 Segundos;
	Limpiar Pantalla;
	Escribir "------- BOLETA ----------";
	Escribir "Nombre producto: ",nombreProducto;
	Escribir "Cantidad: ",cantidad,"X ", precioProducto;
	Escribir "TOTAL $",total;	
FinProceso
