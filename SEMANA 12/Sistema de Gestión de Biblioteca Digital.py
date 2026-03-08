# --------------------------------------------
# Sistema de Gestión de Biblioteca Digital
# --------------------------------------------

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla inmutable para título y autor
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}          # Diccionario {ISBN: Libro}
        self.usuarios = set()     # Conjunto de IDs únicos
        self.historial = []       # Historial de préstamos (lista de tuplas)

    # Añadir libro
    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("ISBN no encontrado en la biblioteca.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios:
            self.usuarios.add(usuario.user_id)
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya existe.")

    # Dar de baja usuario
    def baja_usuario(self, usuario):
        if usuario.user_id in self.usuarios:
            self.usuarios.remove(usuario.user_id)
            print(f"Usuario dado de baja: {usuario}")
        else:
            print("Usuario no encontrado.")

    # Prestar libro
    def prestar_libro(self, usuario, isbn):
        if isbn in self.libros and usuario.user_id in self.usuarios:
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            self.historial.append((usuario.user_id, libro.isbn))
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("No se pudo realizar el préstamo (usuario o libro no válido).")

    # Devolver libro
    def devolver_libro(self, usuario, isbn):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f"Libro devuelto: {libro} por {usuario.nombre}")
                return
        print("El usuario no tiene este libro prestado.")

    # Buscar libros
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # Listar libros prestados de un usuario
    def listar_prestados(self, usuario):
        return usuario.libros_prestados


# --------------------------------------------
# Ejemplo de uso y pruebas
# --------------------------------------------
if __name__ == "__main__":
    # Crear biblioteca
    biblio = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "12345")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "67890")
    libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "11111")

    # Agregar libros
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)
    biblio.agregar_libro(libro3)

    # Crear usuario
    usuario1 = Usuario("Andrea", "U001")
    biblio.registrar_usuario(usuario1)

    # Prestar libro
    biblio.prestar_libro(usuario1, "12345")

    # Buscar libro por autor
    print("\nResultados de búsqueda por autor 'Antoine':")
    resultados = biblio.buscar_libros("autor", "Antoine")
    for r in resultados:
        print(r)

    # Listar libros prestados
    print("\nLibros prestados a Andrea:")
    for l in biblio.listar_prestados(usuario1):
        print(l)

    # Devolver libro
    biblio.devolver_libro(usuario1, "12345")

    # Dar de baja usuario
    biblio.baja_usuario(usuario1)

    # Mostrar historial de préstamos
    print("\nHistorial de préstamos:")
    for registro in biblio.historial:
        print(f"Usuario ID: {registro[0]}, ISBN: {registro[1]}")