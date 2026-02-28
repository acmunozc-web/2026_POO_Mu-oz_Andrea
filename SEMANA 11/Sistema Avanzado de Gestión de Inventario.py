import json

# -------------------------------
# Clase Producto
# -------------------------------
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id} - {self.nombre} | Cantidad: {self.cantidad} | Precio: {self.precio}"


# -------------------------------
# Clase Inventario
# -------------------------------
class Inventario:
    def __init__(self):
        # Diccionario para almacenar productos: {id: Producto}
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("️ Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id] = producto
            print(" Producto agregado correctamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(" Producto eliminado.")
        else:
            print("️ No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            print(" Producto actualizado.")
        else:
            print(" No se encontró un producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("️ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            for p in self.productos.values():
                print(p)
        else:
            print("️ El inventario está vacío.")

    def guardar_en_archivo(self, archivo):
        with open(archivo, "w") as f:
            json.dump({id: vars(p) for id, p in self.productos.items()}, f)
        print(" Inventario guardado en archivo.")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                self.productos = {id: Producto(**info) for id, info in data.items()}
            print(" Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("️ No se encontró el archivo, se iniciará un inventario vacío.")


# -------------------------------
# Menú Interactivo
# -------------------------------
def menu():
    inventario = Inventario()

    # Precargar productos de supermercado
    productos_iniciales = [
        Producto("001", "Arroz", 50, 1.20),
        Producto("002", "Leche", 30, 0.95),
        Producto("003", "Pan", 40, 0.50),
        Producto("004", "Huevos", 60, 0.10),
        Producto("005", "Aceite", 25, 3.50),
        Producto("006", "Azúcar", 35, 1.00),
        Producto("007", "Café", 20, 4.75),
        Producto("008", "Sal", 15, 0.40),
        Producto("009", "Fideos", 45, 0.80),
        Producto("010", "Galletas", 50, 1.50),
    ]

    for p in productos_iniciales:
        inventario.agregar_producto(p)

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            inventario.actualizar_producto(
                id,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.json")

        elif opcion == "7":
            print(" Saliendo del sistema...")
            break

        else:
            print("️ Opción inválida, intente nuevamente.")


# -------------------------------
# Programa Principal
# -------------------------------
if __name__ == "__main__":
    menu()