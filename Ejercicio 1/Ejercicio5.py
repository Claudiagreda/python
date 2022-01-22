# Ejercicio 5. Calcular la fórmula general

import math

# ENTRADAS
print("Ingresa el valor de a: ")
valora = int(input()) 
valorb = int(input("Ingresa el valor de b: ")) 
valorc = int(input("Por último, ingresa el valor de c: ")) 

#PROCESOS
forgeneral1 = (-(valorb) + pow(((valorb ** 2) - (4 * (valora * valorc))), 1/2)) / (2 * valora)
forgeneral2 = (-(valorb) - pow(((valorb ** 2) - (4 * (valora * valorc))), 1/2)) / (2 * valora)


#SALIDAS
print(f"Resultado raíz 1 = {forgeneral1}")
print(f"Resultado raíz 2 = {forgeneral2}")
