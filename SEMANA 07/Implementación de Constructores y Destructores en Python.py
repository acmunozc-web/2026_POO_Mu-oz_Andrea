# Ejemplo de varias clases con constructores y destructores

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Persona creada: {self.nombre}, {self.edad} años.")

    def __del__(self):
        print(f"Persona {self.nombre} ha sido eliminada de la memoria.")


class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print(f"Auto {self.marca} {self.modelo} encendido.")

    def conducir(self):
        print(f"Conduciendo el {self.marca} {self.modelo}...")

    def __del__(self):
        print(f"Auto {self.marca} {self.modelo} apagado y liberado.")


class Cafetera:
    def __init__(self):
        self.encendida = True
        print("Cafetera encendida y lista para preparar café.")

    def preparar(self, tipo):
        print(f"Preparando un {tipo}... ☕🍪")

    def __del__(self):
        print("Cafetera apagada. Limpieza realizada.")


class Mascota:
    def __init__(self, nombre, especie, descripcion):
        self.nombre = nombre
        self.especie = especie
        self.descripcion = descripcion
        print(f"Mascota creada: {self.nombre}, especie {self.especie}, {self.descripcion}.")

    def jugar(self):
        print(f"{self.nombre} está jugando felizmente 🐾.")

    def __del__(self):
        print(f"Mascota {self.nombre} ya no está en memoria.")


# Uso de las clases
if __name__ == "__main__":
    persona = Persona("Andrea", 21)
    auto = Auto("Toyota", "Corolla")
    cafetera = Cafetera()
    mascota = Mascota("Luna", "perro", "churón blanco")

    auto.conducir()
    cafetera.preparar("nevado de Oreo")
    mascota.jugar()

    # Al finalizar el programa, los destructores se ejecutan automáticamente