Proceso Cafeteria
	
	Definir agregadoElegido,cafeElegido,agregadoSi Como Caracter;
	Definir precioCafe, precioAgregado, cafe, total, agregado Como Entero;
	
	Escribir "------- Menú -------";
	Escribir "N°     Producto     Precio";
	Escribir "1     Espresso     $750";
	Escribir "2     Capuccino     $850";
	Escribir "3     Latte     $800";
	Escribir "4     Mocha     $830";
	Escribir "                          ";
	Escribir "Ingrese Producto";
	Leer cafe;
	
	
	Si cafe == 1 Entonces
		cafeElegido = "Espresso";
		precioCafe = 750;
	FinSi
	
	Si cafe == 2 Entonces
		cafeElegido = "Capuccino";
		precioCafe = 850;
	FinSi
	
	Si cafe == 3 Entonces
		cafeElegido = "Latte";
		precioCafe = 800;
	FinSi
	
	Si cafe == 4 Entonces
		cafeElegido = "Mocha";
		precioCafe = 830;
	FinSi
	
	
	Escribir "¿Desea agregado?";
	Leer agregadoSi;
	
	Si agregadoSi == "si" Entonces
		Escribir "------- Agregados -------";
		Escribir "N°     Producto     Precio";
		Escribir "1     Leche     $300";
		Escribir "2     Chocolate     $200";
		Escribir "3     Ambos     $500";
		Escribir "                          ";
		Leer agregado;
		
		
		Si agregado == 1 Entonces
			agregadoElegido = "Leche";
			precioAgregado = 300;
		FinSi
		
		Si agregado == 2 Entonces
			agregadoElegido = "Chocolate";
			precioAgregado = 200;
		FinSi
		
		Si agregado == 3 Entonces
			agregadoElegido = "Ambos";
			precioAgregado = 500;
		FinSi
	SiNo
		total = precioCafe;
	FinSi
	
	
	
	
	
	
	
	

	
FinProceso
