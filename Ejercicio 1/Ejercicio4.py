# Ejercicio 4. Pedir la cantidad de grados y convertirlos a °C, °F y K.

import math

# ENTRADAS
print("¿Cuáles son los grados?: ")
grados = int(input())

#PROCESOS
# Conversión de Fahrenheit a Celsius
celsius = ((grados - 32) * 5) / 9

# Conversión de Fahrenheit a Kelvin
kelvin = (5 * (grados - 32)) / (9 + 273.15)

# Conversión de Celsius a Fahrenheit
fahrenheit = (9 * grados / 5) + 32


#SALIDAS
print(f"Los grados Celsius son = {round (celsius, 2)}")
print(f"Los grados Kelvin son = {round (kelvin, 2)}")
print(f"Los grados Fahrenheit son = {round (fahrenheit, 2)}")