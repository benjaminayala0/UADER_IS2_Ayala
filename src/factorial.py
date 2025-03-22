#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* Calcula el factorial de un rango de números                             *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#* Modificación: Ahora acepta rangos "desde-hasta" como argumento          *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    """Calcula el factorial de un número."""
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

# Función para calcular factoriales en un rango
def calcular_factoriales(desde, hasta):
    for i in range(desde, hasta + 1):
        print(f"Factorial {i}! es {factorial(i)}")

# Verificar si se pasó un argumento
if len(sys.argv) <= 1:
    rango = input("Ingrese el rango en formato desde-hasta (ejemplo: 4-8): ")
else:
    rango = sys.argv[1]

# Validar el formato del rango
try:
    desde, hasta = map(int, rango.split('-'))
    if desde > hasta:
        print("El valor inicial debe ser menor o igual al final")
    else:
        calcular_factoriales(desde, hasta)
except ValueError:
    print("Formato incorrecto. Debe ser desde-hasta (ejemplo: 4-8)")