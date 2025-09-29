//En una tienda de venta de video-juegos existen los siguientes precios:
	//Categoría         Precio
//-------------         ---------
//1         Nintendo Wii     $19.000
//2          Play Station      $9.000
//3         XBOX                 $15.000
//De Lunes a Jueves se realiza un descuento del 10% del video en todas las categorías.
	
//Imprima el total a pagar considerando que debe seleccionar una categoría, un día de la   
//semana y la cantidad de videos de la categoría a comprar.



Proceso JuegosConsola
	
	Definir dia, juego Como Caracter;
	Definir precio Como Entero;
	
	Escribir "Bienvenido/a! Elija que juego requiere comprar: ";
	Leer juego;
	
	Escribir "Ingrese día de su compra: ";
	Leer dia;
	
	Si juego = "Wii" Entonces
		precio = 19000;
	FinSi
	
	Si juego = "Play" Entonces
		precio = 9000;
	FinSi
	
	Si juego = "Xbox" Entonces
		precio = 15000;
	FinSi
	
	Si dia = "Lunes" o dia = "Martes" o dia = "Miercoles" o dia = "Jueves" Entonces
		precio = precio * 0.8;
	FinSi
	
	Escribir "Total a pagar: ", precio;
	
	
FinProceso
