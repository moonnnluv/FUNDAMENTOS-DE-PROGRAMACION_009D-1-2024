// La empresa distribuidora de combustible Ezzo, ha decidido automatizar las transacciones y desea implementar un sistema para la venta de sus combustibles y dar alguna promoción a sus clientes del Club Ezzo.
// Por esto, se debe tener presente los ítems de combustibles y sus valores por litro:
// ítem Valor por litro
// Gasolina 93 $1600
// Gasolina 95 $1700
// Gasolina 97 $1800
// Diesel $1400
// Kerosene $1000
//OBS: Por otra parte, la empresa como promoción para fidelizar a sus clientes, a dispuesto el Club Ezzo, en el cual el cliente por el solo hecho de pertenecer a este disponible de un descuento de un 20% en su compra de combustible
//Se pide crear un algoritmo que permite realizar la transacción de venta de combustible, tenga presente:
			// El cliente puede seleccionar solo UN ítem (tipo de bencina)
			// Debe indicar la cantidad de litros requeridos
			// Indicar si es socio al Club Ezzo, para obtener descuentos, solo si corresponde (ver observación).
					// Imprimir el ticket de compra indicando:
					// Combustible: XXXXXXXX
					// Litros: XXX Valor Litro: $ XXX
					//o Total $ XXXXX
					//o Descuento (SOLO SI CORRESPONDE) $XXXXX
					//o Total a pagar $ XXXXXX





Proceso combustibles_ezzo
	
	Definir tipo_gasolina, club_ezzo, descuento Como Caracter;
	Definir precio_litro, litros, descuento_final, pago_parcial, pago_final Como Entero;
	
	Escribir "Bienvenido/a a Combustibles Ezzo, ofrecemos los siguientes productos: ";
	Escribir "              ";
	Escribir "     Item           Valor por Litro";
	Escribir "1. Gasolina 93          $1600";
	Escribir "2. Gasolina 95          $1700";
	Escribir "3. Gasolina 97          $1800";
	Escribir "4. Diesel               $1400";
	Escribir "5. Kerosene             $1000";
	
	Esperar 1.5 Segundos;
	
	Escribir "          ";
	Escribir "Seleccione producto a elegir: ";
	Leer tipo_gasolina;
	
	Si tipo_gasolina = "1" Entonces
		precio_litro = 1600;
	FinSi
	
	Si tipo_gasolina = "2" Entonces
		precio_litro = 1700;
	FinSi
	
	Si tipo_gasolina = "3" Entonces
		precio_litro = 1800;
	FinSi
	
	Si tipo_gasolina = "4" Entonces
		precio_litro = 1400;
	FinSi
	
	Si tipo_gasolina = "5" Entonces
		precio_litro = 1000;
	FinSi
	
	Escribir "Seleccione cantidad de litros: ";
	Leer litros;
	
	pago_parcial = precio_litro * litros;
	
	Escribir "¿Pertenece al Club Ezzo? (S/N)";
	Leer club_ezzo;
	
	Si club_ezzo = "S" Entonces
		descuento_final = pago_parcial * 0.2;
		pago_final = pago_parcial - descuento_final;
	SiNo
		descuento_final = 0;
		pago_final = pago_parcial;
	FinSi
	
	
	
	Escribir "------- BOLETA -------";
	Escribir "Combustible: ", tipo_gasolina;
	Escribir "Litros: ", litros;
	Escribir "Valor Litro: $ ", precio_litro;
	Escribir "Total: $ ", pago_parcial;
	Escribir "Descuento: ", descuento_final;
	Escribir "Total a pagar: $ ", pago_final;
	
	
	
	
FinProceso
