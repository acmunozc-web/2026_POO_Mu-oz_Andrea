# Programa para calcular el promedio semanal del clima
# Usando Programación Tradicional (estructuras de funciones)

def ingresar_temperaturas():
    """
    Función para ingresar las temperaturas diarias de la semana.
    Retorna una lista con las 7 temperaturas.
    """
    temperaturas = []
    for dia in range(1, 8):  # 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función para calcular el promedio semanal de las temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal que organiza el flujo del programa.
    """
    print("=== Promedio semanal del clima (Programación Tradicional) ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Punto de entrada del programa
if __name__ == "__main__":
    main()