#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* collatz.py                                                              *
#* Calcula la secuencia de Collatz para los números entre 1 y 10000       *
#* y grafica el número de iteraciones para cada número de inicio.         *
#* Dr.P.E.Colla (c) 2025                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

import matplotlib.pyplot as plt

#calcular el numero de iteraciones en la secuencia de Collatz
def collatz_iterations(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

#generamos listas para los números de inicio y el número de iteraciones
numbers = []
iterations = []

#Calculamos la secuencia de Collatz para los números entre 1 y 10000
for i in range(1, 10001):
    numbers.append(i)
    iterations.append(collatz_iterations(i))

#grafico
plt.figure(figsize=(10, 6))
plt.scatter(iterations, numbers, s=1, color='blue', alpha=0.5)
plt.title("Número de Iteraciones de la Secuencia de Collatz")
plt.xlabel("Número de Iteraciones")
plt.ylabel("Número de Inicio")
plt.grid(True)
plt.tight_layout()

#grafico en un archivo
plt.savefig('collatz_iterations.png')

#mostrar el grafico
plt.show()