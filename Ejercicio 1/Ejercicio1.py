# Ejercicio 1. Cálculo de promedio de tres calificaciones

import math

# ENTRADAS
print("Escribe una calificación: ")
calificacion1 = float(input()) 
calificacion2 = float(input("Escribe otra calificación: ")) 
calificacion3 = float(input("Escribe una calificación más: ")) 

#PROCESOS
suma = calificacion1 + calificacion2 + calificacion3 
division = suma / 3

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

if (promedio >= 6):
    print("Aprobado")
elif (promedio < 6):
   print("Reprobado")

#SALIDAS
#print(f"El promedio de las calificaciones = {division}")

print(f"El promedio de las calificaciones = {promedio}")

