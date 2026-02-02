import os
import subprocess

def mostrar_codigo(ruta_script):
    """Muestra el contenido de un archivo .py o .txt"""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Contenido de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    """Ejecuta un script Python en una terminal nueva"""
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix/Linux/Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def crear_nueva_tarea(ruta_sub_carpeta):
    """Crea un archivo de texto para notas o tareas rápidas"""
    nombre_tarea = input("Escribe el nombre de tu nueva tarea/nota: ") + ".txt"
    ruta_tarea = os.path.join(ruta_sub_carpeta, nombre_tarea)
    try:
        with open(ruta_tarea, 'w', encoding='utf-8') as archivo:
            contenido = input("Escribe el contenido inicial de la tarea: ")
            archivo.write(contenido)
        print(f"Tarea/nota '{nombre_tarea}' creada en {ruta_sub_carpeta}")
    except Exception as e:
        print(f"No se pudo crear la tarea: {e}")

def mostrar_menu():
    """Menú principal con áreas de organización"""
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Casa',
        '2': 'Trabajo',
        '3': 'Proyectos_Personales'
    }

    while True:
        print("\n===== Dashboard de Organización =====")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    """Submenú para explorar carpetas dentro de cada unidad"""
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\n--- Submenú ---")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

def mostrar_scripts(ruta_sub_carpeta):
    """Muestra scripts y notas dentro de la carpeta seleccionada"""
    archivos = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and (f.name.endswith('.py') or f.name.endswith('.txt'))]

    while True:
        print("\n--- Archivos disponibles ---")
        for i, archivo in enumerate(archivos, start=1):
            print(f"{i} - {archivo}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")
        print("N - Crear nueva tarea/nota")

        eleccion = input("Elige un archivo, '0' para regresar, '9' para menú principal o 'N' para nueva tarea: ")
        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        elif eleccion.upper() == 'N':
            crear_nueva_tarea(ruta_sub_carpeta)
        else:
            try:
                eleccion = int(eleccion) - 1
                if 0 <= eleccion < len(archivos):
                    ruta_archivo = os.path.join(ruta_sub_carpeta, archivos[eleccion])
                    codigo = mostrar_codigo(ruta_archivo)
                    if codigo and ruta_archivo.endswith('.py'):
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_archivo)
                        else:
                            print("No se ejecutó el script.")
                        input("\nPresiona Enter para volver al menú de archivos.")
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()