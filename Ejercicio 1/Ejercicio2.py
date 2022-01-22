# Ejercicio 2. Calcular área y perímetro de un círculo

import math

# ENTRADAS
print("¿cuál es el radio del círculo?: ")
radio = int(input()) 
PI = 3.1416

#PROCESOS
area = PI * radio ** 2

# area = PI * radio * radio
# area = PI * pow(radio, 2)

perimetro = (math.pi * radio) * 2



#SALIDAS
print(f"El área del círculo es = {round (area, 2)}")
print(f"El perímetro del círculo es = {round (perimetro, 2)}")
