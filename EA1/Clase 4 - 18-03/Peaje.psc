Proceso Peaje
	Definir Categoria Como Caracter;
	Definir Tarifa Como Caracter;
	Definir total Como Entero;
	
	Escribir "Ingrese categoria: ";
	Escribir "Ej: Auto, Camioneta, Moto, Bus, Camión ";
	Leer Categoria;
	
	Escribir "Ingrese tarifa: ";
	Escribir "Ej: Normal o Fin de Semana ";
	Leer Tarifa;
	
	Si Categoria == "Auto" o Categoria == "Camioneta" Entonces
		si Tarifa == "Normal" Entonces
			total = 2000;
		SiNo
			total = 3000;
		FinSi
		
	FinSi
	
	Si Categoria == "Camión" o Categoria == "Bus" Entonces
		si Tarifa == "Normal" Entonces
			total = 3500;
		SiNo
			total = 5200;
		FinSi
		
	FinSi
	
	Si Categoria == "Moto" Entonces
		si Tarifa == "Normal" Entonces
			total = 600;
		SiNo
			total = 900;
		FinSi
		
	FinSi
	
	Escribir "Total a pagar: $ ", total;
	Escribir "Gracias por Viajar en la Ruta doPrado";
	
	
FinProceso
