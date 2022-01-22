metros = int(input("¿Cuál es el nivel del agua en metros de la cisterna?: "))

if (metros > 6):
    print("Desbordamiento de agua en cisterna")
elif (metros == 6):
   print("Apagar Bomba")
elif (metros >= 4 and metros < 6):
   print("Desacelerar Bomba")
elif (metros >= 2 and metros < 4):
   print("Bomba trabajando")
elif (metros > 0 and metros < 2):
   print("Acelerar Bomba de Agua")
elif (metros == 0):
   print("Encender Bomba de Agua")
elif (metros < 0):
   print("Fuga en cisterna")




