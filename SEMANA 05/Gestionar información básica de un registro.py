# Programa de gestión básica de un registro de estudiantes
# Este programa permite añadir estudiantes a un registro,
# mostrar la lista completa y buscar un estudiante por su ID.

# Definimos una estructura de datos: lista de diccionarios
registro_estudiantes = []


def agregar_estudiante(estudiante_id: int, nombre: str, edad: int, promedio: float, activo: bool):
    """
    Función para agregar un estudiante al registro.
    Parámetros:
        estudiante_id (int): Identificador único del estudiante
        nombre (str): Nombre del estudiante
        edad (int): Edad del estudiante
        promedio (float): Promedio académico del estudiante
        activo (bool): Estado del estudiante (True = activo, False = inactivo)
    """
    estudiante = {
        "id": estudiante_id,
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio,
        "activo": activo
    }
    registro_estudiantes.append(estudiante)


def mostrar_registro():
    """Función que imprime todos los estudiantes en el registro."""
    print("\n--- Registro de Estudiantes ---")
    for estudiante in registro_estudiantes:
        estado = "Activo" if estudiante["activo"] else "Inactivo"
        print(f"ID: {estudiante['id']} | Nombre: {estudiante['nombre']} | "
              f"Edad: {estudiante['edad']} | Promedio: {estudiante['promedio']} | Estado: {estado}")


def buscar_estudiante(estudiante_id: int):
    """Función que busca un estudiante por su ID."""
    for estudiante in registro_estudiantes:
        if estudiante["id"] == estudiante_id:
            print("\nEstudiante encontrado:")
            estado = "Activo" if estudiante["activo"] else "Inactivo"
            print(f"ID: {estudiante['id']} | Nombre: {estudiante['nombre']} | "
                  f"Edad: {estudiante['edad']} | Promedio: {estudiante['promedio']} | Estado: {estado}")
            return
    print("\nNo se encontró un estudiante con ese ID.")


# Programa principal
def main():
    print("Bienvenido al sistema de gestión de estudiantes")

    # Agregamos los estudiantes solicitados
    agregar_estudiante(1, "Andrea Muñoz", 21, 9.1, True)
    agregar_estudiante(2, "Nathaly Ponguillo", 22, 8.7, True)
    agregar_estudiante(3, "Gustavo Fernandez", 23, 7.8, False)

    # Mostramos el registro completo
    mostrar_registro()

    # Ejemplo: buscamos un estudiante por ID
    buscar_estudiante(2)


# Punto de entrada del programa
if __name__ == "__main__":
    main()