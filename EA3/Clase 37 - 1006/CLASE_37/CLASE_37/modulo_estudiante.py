# Esta modulo contendra las funciones para las
# transacciones CRUD, se emulara una base de datos
estudiantes_list = []  # --> será la bd temporal


def registrar_estudiante():
    run = str(input("Ingrese run: ")).strip()
    nombre = str(input("Ingrese nombre: ")).strip()
    carrera = str(input("Ingrese carrera: ")).strip()
    jornada = str(input("Ingrese jornada D/V/A:")).strip()
    # creamos la entidad de engloba los datos
    estudiante = {
        "run": run,
        "nombre": nombre,
        "carrera": carrera,
        "jornada": jornada
    }
    # Agregamos la entidad a la colección
    estudiantes_list.append(estudiante)
    print("--- estudiante registrado ---")


def listar_estudiantes():
    # Consultamos si tiene datos la lista
    if not estudiantes_list:
        print("NO hay registros en la BD")
    else:
        for estudiante in estudiantes_list:
            print(f'''
            RUN: {estudiante["run"]}
            Nombre: {estudiante["nombre"]}
            Carrera: {estudiante["carrera"]}
            Jornada: {estudiante["jornada"]} ''')

# vamos a crear una función que va a crear
# un respaldo de los datos en un archivo txt
def grabar_datos():
    if not estudiantes_list:
        print("NO hay registros para respaldar")
    else:
        # vamos a parametrizar el nombre
        nombre_archivo = "respaldo_estudiantes.txt"
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            for estudiante in estudiantes_list:
                archivo.write(f"{estudiante["run"]} - {estudiante["nombre"]} - {estudiante["carrera"]} - {estudiante["jornada"]}\n")
        print("\n ======= RESPALDO CREADO ======")   
         
# Propuesto 1
# Crear la transacción buscar por run, si hay un estudiantes
# que posea el run se listará todos los datos
def buscar_por_run():
    run_buscar = str(input("Ingrese run a buscar: ")).strip()
    encontrado = False
    
    for estudiante in estudiantes_list:
        if estudiante["run"] == run_buscar:
            encontrado = True
            print(f'''
            RUN: {estudiante["run"]}
            Nombre: {estudiante["nombre"]}
            Carrera: {estudiante["carrera"]}
            Jornada: {estudiante["jornada"]} ''')
            break
    
    if encontrado == False:
        print(f"NO hay registro para el run {run_buscar}")
    

# Propuesto 2
# Crear la transacción buscar por jornada       
                 