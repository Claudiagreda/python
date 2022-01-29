# Ejercicio 10. Pedir números enteros en un ciclo mientras sean positivos y en caso de
# que un número sea negativo cerrar el ciclo y al final promediar los
# números positivos ingresados por el usuario.


#ENTRADAS
print("Ingresa un número: ")
numero = int(input())
suma = 0
contador = 0


#PROCESOS
while (numero > 0):    
    if (numero >= 0):
        suma = suma + numero      # Variable acumulador (para acumular números)
        contador = contador + 1   # Variable contador 
        numero = int(input("Ingresa otro número: "))
    if (numero < 0):        # Si se utiliza if ambas condiciones se detectan. Con elif si no se cumple la primera entonces pasa a la siguiente 
        print("valor no válido")
        # promedio = suma / contador
        # print(promedio)

promedio = suma / contador 


# SALIDAS       
print(f"Promedio = {promedio}")




