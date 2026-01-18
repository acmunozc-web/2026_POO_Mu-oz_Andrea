# Clase base: Persona
# → Representa un objeto genérico con atributos comunes
class Persona:
    def __init__(self, nombre, edad):
        # Encapsulación: atributos privados (convención con "_")
        self._nombre = nombre
        self._edad = edad

    # Método para acceder al nombre (getter)
    def get_nombre(self):
        return self._nombre

    # Método para acceder a la edad (getter)
    def get_edad(self):
        return self._edad

    # Método genérico que luego será sobrescrito (polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self._nombre} y tengo {self._edad} años."


# Clase derivada: Estudiante
# → Ejemplo de herencia: Estudiante hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Uso de super() para reutilizar constructor de la clase base
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Polimorfismo: redefinimos el método presentarse
    def presentarse(self):
        return f"Soy {self.get_nombre()}, estudio {self.carrera} y tengo {self.get_edad()} años."


# Clase derivada: Profesor
# → Otro ejemplo de herencia y polimorfismo
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    # Polimorfismo: comportamiento distinto al de Estudiante
    def presentarse(self):
        return f"Soy el profesor {self.get_nombre()}, enseño {self.materia} y tengo {self.get_edad()} años."


# Programa principal
if __name__ == "__main__":
    # Instancias de las clases derivadas
    estudiante = Estudiante("Andrea", 22, "Ingeniería en TIC")
    profesor = Profesor("Carlos", 30, "Programación")

    # Demostración de herencia, encapsulación y polimorfismo
    print(estudiante.presentarse())
    print(profesor.presentarse())