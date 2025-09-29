import os
# -------- variables -----------
lista_usuarios = []  # --> lista vacia
op_menu = ""
rut = ""
nombre = ""
edad = 0
#------ funciones locales --------------
def mostrar_menu():
    op_menu = str(input('''
    ========== MENÚ PRINCIPAL =======
    1. Crear usuario
    2. Listar usuarios
    3. Eliminar usuario por rut
    4. Salir
    \n Elija opción:    '''))
    return op_menu

# ------ Código Principal --------------
while True:
    os.system("cls")
    op_menu = mostrar_menu()
    
    if op_menu=="1":
        os.system("cls")
        print("\n ---- CREAR USUARIO ----")
        rut = str(input("Ingrese rut: ")).strip().upper()
        nombre = str(input("Ingrese nombre:")).strip()
        edad = int(input("Ingrese edad: "))

        usuario = {
            "rut": rut,
            "nombre":nombre,
            "edad":edad
        }
        # Ahora vamos a agregar el usuario a la lista (colección)
        lista_usuarios.append(usuario)
        # vamos  a visualizar los datos 
        print(lista_usuarios)
        
        os.system("pause")
        
    if op_menu=="2":
        os.system("cls")
        print("\n ---- Listar usuarios -----")
        for usuario in lista_usuarios:
            print(f'''
                Rut : {usuario["rut"]}  
                Nombre: {usuario["nombre"]}  
                Edad: {usuario["edad"]} años
                  ''')
        
        os.system("pause")
    
    if op_menu=="3":
        os.system("cls")
        print("\n -- Eliminar usuario por rut ---")
        rut_eliminar = str(input("Ingrese rut: ")).strip().upper()
        # Lógica aplicada... debemos recorrer la lista y por cada
        # elemento de esta, es decir, un usuario vamos a consultar
        # por el rut de este, si coincide con el rut buscado eliminamos
        for usuario in lista_usuarios:
            if usuario["rut"] == rut_eliminar:                                
                lista_usuarios.remove(usuario)
        os.system("pause")
    
    if op_menu=="4":
        break
        