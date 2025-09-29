import os

lista_trabajadores = []  # --> emula la BD

# vamos a crear una función especial
# que nos cargue datos de prueba


def cargar_datos_test():
    # vamos a crear objetos json (trabajador)
    trabajador_1 = {
        "nombre": "Pablo",
        "cargo": "músico",
        "sueldo_bruto": 500000,
        "salud": 35000,
        "pension": 65000,
        "liquido": 400000
    }
    trabajador_2 = {
        "nombre": "Carol",
        "cargo": "analista",
        "sueldo_bruto": 800000,
        "salud": 56000,
        "pension": 104000,
        "liquido": 640000
    }
    trabajador_3 = {
        "nombre": "Pedro",
        "cargo": "analista",
        "sueldo_bruto": 1000000,
        "salud": 70000,
        "pension": 130000,
        "liquido": 800000
    }
    # almacenamos los datos
    lista_trabajadores.append(trabajador_1)
    lista_trabajadores.append(trabajador_2)
    lista_trabajadores.append(trabajador_3)
    print(" --- data de test cargada ----")


def calcular_descuentos(sueldo_bruto):
    salud = round(sueldo_bruto*0.07, 1)
    pension = round(sueldo_bruto*0.13, 1)
    liquido = sueldo_bruto-salud-pension
    return salud, pension, liquido


def registrar_trabajador():
    os.system("cls")
    # Pediremos los datos al usuario
    # crearemos el json correspondiente
    nombre = str(input("Ingrese nombre:")).strip()
    cargo = str(input("Ingrese cargo:")).strip()
    sueldo_bruto = int(input("Ingrese sueldo bruto $"))
    salud, pension, liquido = calcular_descuentos(sueldo_bruto)
    # creamos el json
    trabajador = {
        "nombre": nombre,
        "cargo": cargo,
        "sueldo_bruto": sueldo_bruto,
        "salud": salud,
        "pension": pension,
        "liquido": liquido
    }
    # agregamos el json a la lista
    lista_trabajadores.append(trabajador)
    print("\n --- registro almacenado ---")


def listar_trabajadores():
    os.system("cls")
    print("Trabajador \t Cargo \t Sueldo Bruto \t Desc. Salud \t Desc. AFP \t Líquido a pagar")
    for trabajador in lista_trabajadores:
        print(f"{trabajador["nombre"]} \t {trabajador["cargo"]} \t {trabajador["sueldo_bruto"]} \t {
              trabajador["salud"]} \t {trabajador["pension"]} \t {trabajador["liquido"]}\n")


def imprimir_sueldos():
    os.system("cls")
    op_cargo = str(input('''
    Seleccione el tipo de reporte
    1. Por cargo
    2. Todos los trabajadores
                        
    Ingrese opción:    '''))

    if op_cargo == "1":
        cargo = str(input("Ingrese cargo: ")).strip()
        nombre_archivo = f"planilla_cargo_{cargo}.txt"
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            for trabajador in lista_trabajadores:
                if trabajador["cargo"] == cargo:
                    archivo.write(f"{trabajador["nombre"]} \t {trabajador["cargo"]} \t {trabajador["sueldo_bruto"]} \t {trabajador["salud"]} \t {trabajador["pension"]} \t {trabajador["liquido"]}\n")
    if op_cargo == "2":
        nombre_archivo = f"planilla_todos.txt"
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            for trabajador in lista_trabajadores:            
                archivo.write(f"{trabajador["nombre"]} \t {trabajador["cargo"]} \t {trabajador["sueldo_bruto"]} \t {trabajador["salud"]} \t {trabajador["pension"]} \t {trabajador["liquido"]}\n")
    print("\n ==========se creo la planilla =========")
