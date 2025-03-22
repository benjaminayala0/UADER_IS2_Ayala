#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                         *
#* Calcula el factorial de un rango de números con orientación a objetos   *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

class Factorial:
    def __init__(self, desde=1, hasta=60):
        """
        Constructor para la clase Factorial.
        Permite inicializar un rango de números, con valores por defecto.
        """
        self.desde = desde
        self.hasta = hasta

    def factorial(self, num):
        """
        Método para calcular el factorial de un número.
        Si el número es negativo, muestra un mensaje de error.
        """
        if num < 0:
            print(f"Factorial de {num} no existe (número negativo)")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min, max):
        """
        Método que calcula y muestra el factorial de los números en el rango [min, max].
        """
        self.desde = min
        self.hasta = max

        for i in range(self.desde, self.hasta + 1):
            print(f"Factorial {i}! es {self.factorial(i)}")

# Verificar si se pasó un argumento
if __name__ == "__main__":
    import sys

    # Valores por defecto
    LIMITE_SUPERIOR = 60
    LIMITE_INFERIOR = 1

    if len(sys.argv) <= 1:
        rango = input("Ingrese el rango en formato desde-hasta (ejemplo: 4-8, -10, 5-): ")
    else:
        rango = sys.argv[1]

    # Validar el formato del rango ingresado
    try:
        if "-" in rango:
            partes = rango.split("-")
            if len(partes) == 2:
                if partes[0] == "":  # Caso "-hasta" (sin límite inferior)
                    desde = LIMITE_INFERIOR
                    hasta = int(partes[1])
                elif partes[1] == "":  # Caso "desde-" (sin límite superior)
                    desde = int(partes[0])
                    hasta = LIMITE_SUPERIOR
                else:  # Caso "desde-hasta"
                    desde, hasta = map(int, partes)
            else:
                raise ValueError
        else:
            raise ValueError

        # Validar que desde <= hasta
        if desde > hasta:
            print("Error: El valor inicial debe ser menor o igual al final.")
        else:
            # Crear una instancia de la clase Factorial y calcular factoriales en el rango
            f = Factorial()
            f.run(desde, hasta)

    except ValueError:
        print("Formato incorrecto. Debe ser desde-hasta, -hasta o desde-. Ejemplo: 4-8, -10, 5-")