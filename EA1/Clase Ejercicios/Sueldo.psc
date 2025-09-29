// realice un pseudocódigo en pseint que permita ingresar el sueldo y nombre de 3 empleados e indique el sueldo y nombre del empleado con mayor sueldo
Proceso SueldoEmpleados
	Definir nombre1, nombre2, nombre3 Como Cadena;
	Definir sueldo1, sueldo2, sueldo3 Como Entero;
	Definir sueldo_mayor Como Entero;
	Escribir 'Ingrese nombre del primer empleado: ';
	Leer nombre1;
	Escribir 'Ingrese sueldo del primer empleado: ';
	Leer sueldo1;
	Escribir 'Ingrese nombre del segundo empleado: ';
	Leer nombre2;
	Escribir 'Ingrese sueldo del segundo empleado: ';
	Leer sueldo2;
	Escribir 'Ingrese nombre del tercer empleado: ';
	Leer nombre3;
	Escribir 'Ingrese sueldo del tercer empleado: ';
	Leer sueldo3;
	
	
	Si sueldo1>sueldo2 Y sueldo1>sueldo3 Entonces
		Escribir 'El empleado ', nombre1, ' tiene un sueldo de ', sueldo1;
		Escribir nombre1, ' tiene el mayor sueldo en la empresa.';
	SiNo
		Si sueldo2>sueldo3 Y sueldo1<sueldo2 Entonces
			Escribir 'El empleado ', nombre2, ' tiene un sueldo de ', sueldo2;
			Escribir nombre2, ' tiene el mayor sueldo en la empresa.';
		SiNo
			Si sueldo3>sueldo2 Y sueldo1<sueldo3 Entonces
				Escribir 'El empleado ', nombre3, ' tiene un sueldo de ', sueldo3;
				Escribir nombre3, ' tiene el mayor sueldo en la empresa.';
			FinSi
		FinSi
	FinSi
	
FinProceso
