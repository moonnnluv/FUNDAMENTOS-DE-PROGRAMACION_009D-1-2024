Proceso Fotocopiadora
	Definir HOJAS Como Entero;
	Definir total Como Entero;
	
	
	Escribir 'Ingrese cantidad de hojas: ';
	Leer HOJAS;
	
	total = hojas*20;
	
	Si HOJAS>30 Entonces
		total= total*0.9;
	FinSi
	
	Escribir '---- RESULTADO ----';
	Escribir 'Se debe pagar un total de: ", total, " pesos";
	
	
FinProceso
