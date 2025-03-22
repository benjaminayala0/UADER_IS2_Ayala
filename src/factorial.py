#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* Calcula el factorial de un rango de números                             *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#* Modificación: Ahora acepta rangos con valores omitidos ("-hasta" y "desde-") *
#*-------------------------------------------------------------------------*

import sys

def factorial(num): 
    """
    Calcula el factorial de un número.
    Si el número es negativo, muestra un mensaje de error
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
#changes1 20-03-2025

def calcular_factoriales(desde, hasta):
    """
    Calcula y muestra el factorial de todos los números en el rango [desde, hasta]
    """
    for i in range(desde, hasta + 1):
        print(f"Factorial {i}! es {factorial(i)}")

# Verificar si se pasó un argumento
if len(sys.argv) <= 1:
    rango = input("Ingrese el rango en formato desde-hasta (ejemplo: 4-8, -10, 5-): ")
else:
    rango = sys.argv[1]

# Valores por defecto
LIMITE_SUPERIOR = 60  # Si se omite el final, se asume hasta 60
LIMITE_INFERIOR = 1   # Si se omite el inicio, se asume desde 1

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
        print("Error: El valor inicial debe ser menor o igual al final")
    else:
        calcular_factoriales(desde, hasta)

except ValueError:
    print("Formato incorrecto. Debe ser desde-hasta, -hasta o desde-. Ejemplo: 4-8, -10, 5-")

#changes2 20-03-2025