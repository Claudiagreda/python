# Ejercicio 2. Cálculo de las Operaciones Aritméticas

# Importar una librería de funciones matemáticas para
import math

# ENTRADAS
# Declarar dos variables para números
print("Escribe un número: ")
numero1 = int(input()) #Conversión de valores que ingresa el usuario a tipo de dato int
numero2 = int(input("Escribe otro número: ")) # Conversión de valores que ingresa el usuario a tipo de dato int


#PROCESOS (Cálculos u operaciones matemáticas y lógicas)
suma = numero1 + numero2 
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
potencia_cuadrado = numero1 ** 2
potencia_cubo = pow(numero2, 3)
raiz_cuadrada = pow(numero1, 1/2)
raiz_cubo = pow(numero2, 1/3)
raiz_cuadrada2 = math.sqrt(numero1) # Operaciones matemáticas con librería importada. El punto se utiliza para acceder a algo (en este caso se accede a la función sqrt)
modulo_residuo = numero1 % numero2



#SALIDAS
print(f"La suma = {suma}")
print(f"La resta = {resta}")
print(f"La multiplicacion = {multiplicacion}")
print(f"La división = {division}")
print(f"El cuadrado del número 1 = {potencia_cuadrado}")
print(f"El cubo del número 2 = {potencia_cubo}")
print(f"La raíz cuadrada del número 1 = {round(raiz_cuadrada, 3)}")
print(f"La raíz cúbica del número 2 = {round(raiz_cubo, 2)}")
print(f"El modulo = {modulo_residuo}")