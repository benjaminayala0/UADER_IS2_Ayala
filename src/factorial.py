#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* Calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#* Modificación: Ahora solicita el número si no se proporciona como arg.   *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# Verificar si se pasó un argumento
if len(sys.argv) <= 1:
    num = int(input("Ingrese un número para calcular su factorial: "))
else:
    num = int(sys.argv[1])

print(f"Factorial {num}! es {factorial(num)}")