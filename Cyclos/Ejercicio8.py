# Ejercicio 8. Obtener un número y determinar lo siguiente:
# a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
# b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
# c) en otro caso imprimir No Válido


#ENTRADAS
print("Ingresa un número: ")
numero = int(input())


#PROCESOS
if (numero < 0 and numero > -100):
    for numero in range(-1, -100, -2):    
        print(numero)
elif(numero > 0 and numero < 100):
    # for numero in range(2, 101, 2):    
    #     print(numero) 
    numero >= 2              
    while (numero >= 2 and numero < 102):       
        print(numero)            
        numero = numero + 2  

else: print("No válido")


