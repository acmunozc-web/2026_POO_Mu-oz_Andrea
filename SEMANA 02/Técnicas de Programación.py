#Sensores con ABSTRACCIÓN
# Importamos ABC y abstractmethod para crear clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta que define la interfaz de un Sensor
class Sensor(ABC):
    """
    Clase abstracta que representa un sensor genérico.
    Define los métodos esenciales que cualquier sensor debe implementar.
    """

    @abstractmethod
    def leer(self) -> float:
        """
        Método abstracto para obtener una lectura del sensor.
        Debe ser implementado por las clases hijas.
        """
        pass

    @abstractmethod
    def calibrar(self) -> None:
        """
        Método abstracto para calibrar el sensor.
        Debe ser implementado por las clases hijas.
        """
        pass


# Clase concreta que implementa un sensor de temperatura
class SensorTemperatura(Sensor):
    """
    Clase que representa un sensor de temperatura.
    Implementa los métodos definidos en la clase abstracta Sensor.
    """

    def __init__(self, offset: float = 0.0):
        # offset simula un ajuste de calibración
        self._offset = offset

    def calibrar(self) -> None:
        """
        Simula la calibración del sensor ajustando el offset.
        """
        self._offset = 0.5  # valor fijo de calibración

    def leer(self) -> float:
        """
        Simula la lectura de temperatura desde el hardware.
        Retorna la lectura ajustada con el offset.
        """
        lectura_cruda = 24.3  # valor simulado
        return lectura_cruda + self._offset


# Clase concreta que implementa un sensor de presión
class SensorPresion(Sensor):
    """
    Clase que representa un sensor de presión.
    Implementa los métodos definidos en la clase abstracta Sensor.
    """

    def __init__(self, factor: float = 1.0):
        # factor simula un ajuste de calibración
        self._factor = factor

    def calibrar(self) -> None:
        """
        Simula la calibración del sensor ajustando el factor.
        """
        self._factor = 1.1  # valor fijo de calibración

    def leer(self) -> float:
        """
        Simula la lectura de presión desde el hardware.
        Retorna la lectura ajustada con el factor.
        """
        lectura_cruda = 101.3  # valor simulado
        return lectura_cruda * self._factor


# Uso práctico de la abstracción
def mostrar_lectura(sensor: Sensor):
    """
    Función que recibe cualquier objeto que implemente la interfaz Sensor.
    Gracias a la abstracción, no importa si es temperatura o presión.
    """
    sensor.calibrar()
    print(f"Lectura del sensor: {sensor.leer()}")

# Ejemplo de uso
temp = SensorTemperatura()
presion = SensorPresion()

mostrar_lectura(temp)     # Lectura de temperatura calibrada
mostrar_lectura(presion)  # Lectura de presión calibrada

#Cuenta bancaria con ENCAPSULACIÓN
class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria.
    Demuestra el principio de encapsulación al proteger el atributo 'saldo'
    y controlar su acceso mediante métodos públicos.
    """

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        # Atributo privado: no debe ser accedido directamente desde fuera de la clase
        self.__saldo = max(0.0, saldo_inicial)
        self.titular = titular

    @property
    def saldo(self) -> float:
        """
        Propiedad que permite consultar el saldo de manera segura.
        No permite modificarlo directamente.
        """
        return self.__saldo

    def depositar(self, monto: float) -> None:
        """
        Método público para aumentar el saldo.
        Aplica validaciones para evitar depósitos inválidos.
        """
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.__saldo += monto

    def retirar(self, monto: float) -> None:
        """
        Método público para disminuir el saldo.
        Aplica validaciones para evitar retiros inválidos o superiores al saldo.
        """
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes.")
        self.__saldo -= monto


# -------------------------------
# Uso práctico de la encapsulación
# -------------------------------

# Crear una cuenta con saldo inicial
cuenta = CuentaBancaria("Andrea", 100)

# Consultar saldo mediante la propiedad
print(f"Saldo inicial: {cuenta.saldo}")  # 100

# Realizar operaciones seguras
cuenta.depositar(50)
print(f"Saldo después del depósito: {cuenta.saldo}")  # 150

cuenta.retirar(30)
print(f"Saldo después del retiro: {cuenta.saldo}")  # 120

# Intentar acceder directamente al atributo privado (no recomendado)
# print(cuenta.__saldo)  # Esto generará un error: AttributeError

#Sistema de empleados con HERENCIA
# -------------------------------
# Clase base (Padre)
# -------------------------------
class Empleado:
    """
    Clase base que representa a un empleado genérico.
    Contiene atributos y métodos comunes a todos los empleados.
    """

    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_pago(self) -> float:
        """
        Método que calcula el pago mensual del empleado.
        En la clase base, simplemente retorna el salario base.
        """
        return self.salario_base

    def mostrar_info(self) -> None:
        """
        Muestra la información básica del empleado.
        """
        print(f"Empleado: {self.nombre}, Salario base: {self.salario_base}")


# -------------------------------
# Clase derivada (Hija)
# -------------------------------
class EmpleadoVentas(Empleado):
    """
    Clase que representa a un empleado del área de ventas.
    Hereda de la clase Empleado y agrega el atributo 'comision'.
    """

    def __init__(self, nombre: str, salario_base: float, comision: float):
        # Llamamos al constructor de la clase padre con super()
        super().__init__(nombre, salario_base)
        self.comision = comision

    def calcular_pago(self) -> float:
        """
        Sobrescribe el método de la clase padre.
        El pago incluye el salario base más la comisión.
        """
        return super().calcular_pago() + self.comision

    def mostrar_info(self) -> None:
        """
        Extiende el método de la clase padre para mostrar también la comisión.
        """
        print(f"Empleado de Ventas: {self.nombre}, "
              f"Salario base: {self.salario_base}, "
              f"Comisión: {self.comision}")


# -------------------------------
# Otra clase derivada (Hija)
# -------------------------------
class EmpleadoGerente(Empleado):
    """
    Clase que representa a un gerente.
    Hereda de la clase Empleado y agrega un bono adicional.
    """

    def __init__(self, nombre: str, salario_base: float, bono: float):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_pago(self) -> float:
        """
        Sobrescribe el método de la clase padre.
        El pago incluye el salario base más el bono.
        """
        return super().calcular_pago() + self.bono

    def mostrar_info(self) -> None:
        """
        Extiende el método de la clase padre para mostrar también el bono.
        """
        print(f"Gerente: {self.nombre}, "
              f"Salario base: {self.salario_base}, "
              f"Bono: {self.bono}")


# -------------------------------
# Uso práctico de la herencia
# -------------------------------

# Crear instancias de diferentes tipos de empleados
empleado_general = Empleado("Luis", 1200)
empleado_ventas = EmpleadoVentas("Ana", 1000, 300)
empleado_gerente = EmpleadoGerente("Carlos", 2000, 800)

# Mostrar información y calcular pagos
empleado_general.mostrar_info()
print("Pago:", empleado_general.calcular_pago(), "\n")

empleado_ventas.mostrar_info()
print("Pago:", empleado_ventas.calcular_pago(), "\n")

empleado_gerente.mostrar_info()
print("Pago:", empleado_gerente.calcular_pago(), "\n")

#Figuras geométricas con POLIMORFISMO
# -------------------------------
# Clase base (Padre)
# -------------------------------
class Figura:
    """
    Clase base que representa una figura geométrica.
    Define el método 'area' que será sobrescrito por las clases hijas.
    """

    def area(self) -> float:
        """
        Método genérico para calcular el área.
        En la clase base no tiene implementación concreta.
        """
        raise NotImplementedError("Este método debe ser implementado por las clases hijas.")


# -------------------------------
# Clase hija: Círculo
# -------------------------------
class Circulo(Figura):
    """
    Clase que representa un círculo.
    Implementa el método 'area' de manera específica.
    """

    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        """
        Calcula el área de un círculo usando la fórmula:
        A = π * r^2
        """
        import math
        return math.pi * (self.radio ** 2)


# -------------------------------
# Clase hija: Rectángulo
# -------------------------------
class Rectangulo(Figura):
    """
    Clase que representa un rectángulo.
    Implementa el método 'area' de manera específica.
    """

    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    def area(self) -> float:
        """
        Calcula el área de un rectángulo usando la fórmula:
        A = ancho * alto
        """
        return self.ancho * self.alto


# -------------------------------
# Clase hija: Triángulo
# -------------------------------
class Triangulo(Figura):
    """
    Clase que representa un triángulo.
    Implementa el método 'area' de manera específica.
    """

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        """
        Calcula el área de un triángulo usando la fórmula:
        A = (base * altura) / 2
        """
        return (self.base * self.altura) / 2


# -------------------------------
# Uso práctico del polimorfismo
# -------------------------------

# Creamos una lista de figuras distintas
figuras = [
    Circulo(5),        # Círculo con radio 5
    Rectangulo(4, 6),  # Rectángulo de 4x6
    Triangulo(3, 7)    # Triángulo con base 3 y altura 7
]

# Iteramos sobre la lista y llamamos al mismo método 'area'
# Gracias al polimorfismo, cada clase ejecuta su propia versión del método
for figura in figuras:
    print(f"Área de {figura.__class__.__name__}: {figura.area()}")
