# Ejercicio 3. Cálcular la edad de una persona

import math

# ENTRADAS
print("¿Cuál es tu nombre?: ")
nombre = input()
añoActual = int(input("¿Cuál es el año actual?: "))
añoNacimiento = int(input("¿En qué año naciste?: "))


#PROCESOS
edad = añoActual - añoNacimiento


#SALIDAS
print(f"Nombre de la persona: {nombre}")
print(f"Tu edad = {edad}")