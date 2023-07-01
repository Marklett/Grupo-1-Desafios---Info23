from datetime import datetime

#Mensaje de bienvenida
print("\n\n------------------------------INFORMATORIO 2023----------------------------------------")
print("---------------------------------------------------------------------------------------")
print("--------------Desafío 8: Principios de programación orientada a objetos----------------- \n")
print("GRUPO 1- INTEGRANTES: Mercado Alejandro, Quiroz Agustín, Pedro Galarza, Fernández Braian\n")
print("--------------------------------------------------------------------------------------\n")

class Usuario:
    contador_id = 0

    def __init__(self, nombre, apellido, telefono, username, email, contraseña):
        Usuario.contador_id += 1
        self.id = Usuario.contador_id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = datetime.now()
        self.avatar = ""
        self.estado = "activo"
        self.online = False
    
    def login(self, username, contraseña):
        if self.username == username and self.contraseña == contraseña:
            self.online = True
            print("Inicio de sesión exitoso.")
        else:
            print("Nombre de usuario o contraseña incorrectos.")
    
    def comentar_articulo(self, articulos):
        if self.online:
            print("Artículos existentes:")
            for articulo in articulos:
                articulo.mostrar_informacion()

            id_articulo = int(input("Ingrese el ID del artículo en el que desea comentar: "))
            contenidoComentario = input("Ingrese su comentario: ")

            for articulo in articulos:
                if articulo.id == id_articulo:
                    comentario = Comentario(self.id, articulo.id, contenidoComentario)
                    articulo.agregar_comentario(comentario)
                    print("Comentario agregado exitosamente.")
                    break
            else:
                print("ID de artículo no encontrado.")
        else:
            print("Debes iniciar sesión para poder comentar en los artículos.")
    @staticmethod
    def mostrar_usuarios(usuarios):
        print("Usuarios registrados:")
        for usuario in usuarios:
            if isinstance(usuario, Publico):
                print("Público:")
                print(f"ID: {usuario.id}, Nombre: {usuario.nombre}")
            elif isinstance(usuario, Colaborador):
                print("Colaborador:")
                print(f"ID: {usuario.id}, Nombre: {usuario.nombre}")

class Publico(Usuario):
    def __init__(self, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(nombre, apellido, telefono, username, email, contraseña)
        self.es_publico = True

    def menu_comentar_articulo(self, articulos):
        print("Artículos existentes:")
        for articulo in articulos:
            articulo.mostrar_informacion()

        id_articulo = int(input("Ingrese el ID del artículo en el que desea comentar: "))
        contenido = input("Ingrese su comentario: ")

        for articulo in articulos:
            if articulo.id == id_articulo:
                comentario = Comentario(self.id, articulo.id, contenido)
                articulo.agregar_comentario(comentario)
                print("Comentario agregado exitosamente.")
                break
        else:
            print("ID de artículo no encontrado.")

class Colaborador(Usuario):
    def __init__(self, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(nombre, apellido, telefono, username, email, contraseña)
        self.es_colaborador = True

    def menu_comentar_articulo(self, articulos):
        print("Artículos existentes:")
        for articulo in articulos:
            articulo.mostrar_informacion()

        id_articulo = int(input("Ingrese el ID del artículo en el que desea comentar: "))
        contenidoComentario = input("Ingrese su comentario: ")

        for articulo in articulos:
            if articulo.id == id_articulo:
                comentario = Comentario(self.id, articulo.id, contenidoComentario)
                articulo.agregar_comentario(comentario)
                print("Comentario agregado exitosamente.")
                break
        else:
            print("ID de artículo no encontrado.")

    def crear_articulo(self, articulos):
        if self.online:
            titulo = input("Ingrese el título del artículo: ")
            resumen = input("Ingrese el resumen del artículo: ")
            contenido = input("Ingrese el contenido del artículo: ")
            fecha_publicacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            imagen = input("Ingrese el enlace de la imagen del artículo: ")
            estado = "publicado"

            articulo = Articulo(len(articulos) + 1, self.id, titulo, resumen, contenido, fecha_publicacion, imagen, estado)
            articulos.append(articulo)
            print("Artículo creado exitosamente.")
        else:
            print("Debes iniciar sesión para poder crear un artículo.")

class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado
        self.comentarios = []

    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)

    def mostrar_informacion(self):
        print("ID:", self.id)
        print("Título:", self.titulo)
        print("Resumen:", self.resumen)
        print("Contenido:", self.contenido)
        print("Fecha de publicación:", self.fecha_publicacion)
        print("Imagen:", self.imagen)
        print("Estado:", self.estado)
        print()

    @staticmethod
    def mostrar_articulos(articulos):
        print("Artículos registrados:")
        for articulo in articulos:
            articulo.mostrar_informacion()

class Comentario:
    def __init__(self, id_usuario, id_articulo, contenido):
        self.id_usuario = id_usuario
        self.id_articulo = id_articulo
        self.contenido = contenido
    
    @staticmethod
    def mostrar_comentarios(comentarios):
        print("Comentarios registrados:")
        for comentario in comentarios:
            print(f"ID de usuario: {comentario.id_usuario}, ID de artículo: {comentario.id_articulo}")
            print(f"Contenido: {comentario.contenido}")

usuarios = []
articulos = []

while True:
    print("---- Menú Principal ----")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Acceso Admin")
    print("0. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del nuevo usuario: ")
        apellido = input("Ingrese el apellido del nuevo usuario: ")
        telefono = input("Ingrese el teléfono del nuevo usuario: ")
        username = input("Ingrese el nombre de usuario del nuevo usuario: ")
        email = input("Ingrese el email del nuevo usuario: ")
        contraseña = input("Ingrese la contraseña del nuevo usuario: ")
        tipo_usuario = input("Seleccione el tipo de usuario (1-Usuario, 2-Colaborador): ")

        if tipo_usuario == "1":
            usuario = Publico(nombre, apellido, telefono, username, email, contraseña)
        elif tipo_usuario == "2":
            usuario = Colaborador(nombre, apellido, telefono, username, email, contraseña)
        else:
            print("Opción de usuario inválida.")
            continue

        usuarios.append(usuario)
        print("Usuario registrado exitosamente.")

    elif opcion == "2":
        username = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        usuario_encontrado = False
        for usuario in usuarios:
            if usuario.username == username:
                usuario.login(username, contraseña)
                usuario_encontrado = True

                if isinstance(usuario, Publico):
                    while True:
                        print("---- Menú Usuario ----")
                        print("1. Comentar artículo")
                        print("0. Volver al menú principal")

                        opcion_publico = input("Ingrese el número de opción: ")

                        if opcion_publico == "1":
                            usuario.menu_comentar_articulo(articulos)
                        elif opcion_colaborador == "0":
                            break
                        else:
                            print("Opción inválida. Por favor, ingrese un número válido.")
                            break
                if isinstance(usuario, Colaborador):
                    while True:
                        print("---- Menú Colaborador ----")
                        print("1. Comentar artículo")
                        print("2. Crear artículo")
                        print("0. Volver al menú principal")

                        opcion_colaborador = input("Ingrese el número de opción: ")

                        if opcion_colaborador == "1":
                            usuario.menu_comentar_articulo(articulos)
                        elif opcion_colaborador == "2":
                            usuario.crear_articulo(articulos)
                        elif opcion_colaborador == "0":
                            break
                        else:
                            print("Opción inválida. Por favor, ingrese un número válido.")
                            break

        if not usuario_encontrado:
            print("Nombre de usuario no encontrado.")

    elif opcion == "3":
# Acceso Admin para revisar los registros, si bien no se solicita nos fue de mucha ayuda a la hora de testear
        print("Acceso Admin:")
        Usuario.mostrar_usuarios(usuarios)
        Articulo.mostrar_articulos(articulos)
        Comentario.mostrar_comentarios([comentario for articulo in articulos for comentario in articulo.comentarios])

    elif opcion == "0":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")

    print()