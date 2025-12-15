# Programa para calcular el promedio semanal del clima
# Usando Programación Orientada a Objetos (POO)

class ClimaDiario:
    """
    Clase que representa la información diaria del clima.
    Aplica encapsulamiento para proteger los datos.
    """
    def __init__(self, temperatura=0.0):
        self.__temperatura = temperatura  # atributo privado

    def set_temperatura(self, temperatura):
        """Método para asignar la temperatura del día."""
        self.__temperatura = temperatura

    def get_temperatura(self):
        """Método para obtener la temperatura del día."""
        return self.__temperatura


class ClimaSemanal:
    """
    Clase que gestiona las temperaturas de toda la semana.
    """
    def __init__(self):
        self.dias = []  # lista de objetos ClimaDiario

    def ingresar_temperaturas(self):
        """Método para ingresar las temperaturas de los 7 días."""
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            clima_dia = ClimaDiario()
            clima_dia.set_temperatura(temp)
            self.dias.append(clima_dia)

    def calcular_promedio(self):
        """Método para calcular el promedio semanal."""
        total = sum(dia.get_temperatura() for dia in self.dias)
        return total / len(self.dias)


def main():
    print("=== Promedio semanal del clima (POO) ===")
    semana = ClimaSemanal()
    semana.ingresar_temperaturas()
    promedio = semana.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Punto de entrada del programa
if __name__ == "__main__":
    main()