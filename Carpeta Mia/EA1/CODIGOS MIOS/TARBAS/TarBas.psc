// La empresa de buses TarBas, dedicada al transporte de pasajeros al sur de Chile desea implementar un sistema para la venta de pasajes como también dar descuentos cuando se compra pasaje y vuelta.
// Todos los servicios de buses comienzan en Santiago y los destinos junto con los valores de pasajes tanto ida como ida y vuelta son:

//Destino Ida Ida y vuelta
//Curicó 10000 18000
//Temuco 18000 30000
//Puerto Montt 25000 40000

//Por otra parte si se cancela en efectivo se tendrá un 10% de descuento en el total de la compra promoción solo válida para los pasajes de Ida y Vuelta.

Proceso TarBas
	
	Definir destino, opcion_menu, tipo_pasaje Como Caracter;
	Definir precio, cantidad, total, total_pasajes, descuento_final, descuento, precio_final, cantidad_pasajes, cantidad_dinero Como Entero;
	
	cantidad_dinero = 0;
	cantidad_pasajes = 0;
	
	
	
	Repetir 
		
		Escribir "              ";
		Escribir "------- MENU -------";
		Escribir "1.- Vender Pasaje ";
		Escribir "2.- Estadistica de venta  ";
		Escribir "3.- Salir ";
		Leer opcion_menu;
		
		Si opcion_menu = "1" Entonces
			
			Escribir "Bienvenido/a a TarBas, ofrecemos los siguientes servicios: ";
			Escribir "              ";
			Escribir "Destino          Ida       Ida y Vuelta";
			Escribir "Curicó          10000         18000";
			Escribir "Temuco          18000         30000";
			Escribir "Puerto Montt    25000         40000";
			Esperar 1.5 Segundos;
			
			Escribir "              ";
			
			Escribir "Seleccione su destino: ";
			Leer destino;
			
			Si destino = "Curicó" Entonces
				Escribir "¿Pasaje Ida o Ida y vuelta?";
				Leer tipo_pasaje;
				Si tipo_pasaje = "Ida" Entonces
					precio = 10000;
				SiNo
					precio = 18000;
				FinSi
			FinSi
			
			Si destino = "Temuco" Entonces
				Escribir "¿Pasaje Ida o Ida y vuelta?";
				Leer tipo_pasaje;
				Si tipo_pasaje = "Ida" Entonces
					precio = 18000;
				SiNo
					precio = 30000;
				FinSi
			FinSi
			
			Si destino = "Puerto Montt" Entonces
				Escribir "¿Pasaje Ida o Ida y vuelta?";
				Leer tipo_pasaje;
				Si tipo_pasaje = "Ida" Entonces
					precio = 25000;
				SiNo
					precio = 40000;
				FinSi
			FinSi
			
			Escribir "Ingrese cantidad de pasajes a comprar: ";
			Leer cantidad;
			
			precio = precio * cantidad;
			
			Si tipo_pasaje == "Ida y vuelta" Entonces
				descuento = precio * 0.1;
			SiNo
				descuento = 0;
			FinSi
			
			precio_final = precio - descuento;
			
			
			
			Escribir "------- BOLETA -------";
			Escribir "Destino: ", destino;
			Escribir "Tipo de pasaje: ", tipo_pasaje;
			Escribir "Cantidad de pasajes: ", cantidad;
			Escribir "Descuento: ",descuento;
			Escribir "Total a pagar: $ ",precio_final;
			
			cantidad_dinero = cantidad_dinero + precio_final;
			cantidad_pasajes = cantidad_pasajes + cantidad;	
			
			Esperar Tecla;
			
			
		FinSi
		
		Si opcion_menu = "2" Entonces
			Escribir "------- ESTADISTICAS -------";
			Escribir "Dinero recaudado: $ ", cantidad_dinero;
			Escribir "Pasajes vendidos: ", cantidad_pasajes;
			Escribir "              ";
			
		FinSi
	Hasta Que opcion_menu = "3";

	
	


	
	
	
	
FinProceso
