# -------------------------------
# Ejemplo de Tienda de Víveres con POO
# -------------------------------

# Clase Producto: representa un artículo de la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        # Atributos básicos de cada producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        # Método para disminuir el stock cuando se compra un producto
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            return False

    def __str__(self):
        # Representación en texto del producto
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"


# Clase Cliente: representa a un comprador
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Cliente: {self.nombre}"


# Clase Carrito: contiene los productos seleccionados por el cliente
class Carrito:
    def __init__(self, cliente):
        # Relaciona el carrito con un cliente
        self.cliente = cliente
        self.items = []  # Lista de tuplas (producto, cantidad)

    def agregar_producto(self, producto, cantidad):
        # Método para añadir productos al carrito
        if producto.reducir_stock(cantidad):
            self.items.append((producto, cantidad))
            print(f"{cantidad} {producto.nombre} agregado al carrito.")
        else:
            print(f"No hay suficiente stock de {producto.nombre}.")

    def calcular_total(self):
        # Calcula el total a pagar sumando precio * cantidad de cada producto
        return sum(prod.precio * cant for prod, cant in self.items)

    def mostrar_carrito(self):
        # Muestra el detalle del carrito con los productos y el total
        print(f"Carrito de {self.cliente.nombre}:")
        for prod, cant in self.items:
            print(f"- {prod.nombre} x{cant} = ${prod.precio * cant}")
        print(f"Total a pagar: ${self.calcular_total()}")


# ------------------ DEMOSTRACIÓN ------------------

# Crear productos de la tienda
arroz = Producto("Arroz", 1.20, 50)
leche = Producto("Leche", 0.90, 30)
pan = Producto("Pan", 0.15, 100)

# Crear cliente
cliente1 = Cliente("Andrea Muñoz")

# Crear carrito para el cliente
carrito1 = Carrito(cliente1)

# Agregar productos al carrito
carrito1.agregar_producto(arroz, 2)   # Andrea compra 2 arroces
carrito1.agregar_producto(leche, 3)   # Andrea compra 3 leches
carrito1.agregar_producto(pan, 10)    # Andrea compra 10 panes

# Mostrar el carrito y el total
carrito1.mostrar_carrito()