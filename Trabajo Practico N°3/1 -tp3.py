class Factorial:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Factorial, cls).__new__(cls)
        return cls._instancia

    def calcular(self, numero):
        """Calcula el factorial de un número entero no negativo."""
        if numero < 0:
            raise ValueError("El número debe ser no negativo")
        if numero == 0 or numero == 1:
            return 1
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado
# Obtener la misma instancia desde diferentes variables
f1 = Factorial()
f2 = Factorial()

print(f1.calcular(5))  # Salida: 120
print(f2.calcular(3))  # Salida: 6

# Comprobación del Singleton
print(f1 is f2)  # Salida: True
