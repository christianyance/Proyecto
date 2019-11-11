import os
os.system('cls')

username = input("Ingrese nombre:")
print(".")
print("Bienvenido", username)
print("Esta app hara los calculos para una nivelacion topografica simple.")
print("Ingrese 1 para una introduccion del tema, 2 para hacer los calculos o 3 para salir.")

while True:
     x = float(input("Ingrese opcion:"))
     if x in range(1,4):
         break
if x == 1:
    print(".")
    print("La nivelación en topografía es un proceso de medición de elevaciones o altitudes de puntos sobre la superficie de la Tierra.")
    print("La nivelacion simple es aquella en la cual desde una sola posición del aparato se puede conocer las cotas de todos los puntos ")
    print("del terreno que se desea nivelar. Sus elementos son:.")
    print("-> Punto visado: Es el lugar donde colocamos la mira y realizamos la lectura.")
    print("-> Elevación o altitud: La distancia vertical medida desde una superficie de referencia hasta el punto considerado.")
    print("-> Vista atras: Es la primera lectura que se hace al estacionar el equipo o al realizar un cambio de estación.")
    print("-> Vista adelante: Son las lecturas que se realizan, en los puntos de tomados o al crear nuevos puntos de cambio.")
    print("-> Cota: Altura de un punto sobre el nivel del mar o sobre otro plano de nivel.")
    print(".")
    print("Ingrese 1 para hacer los calculos o 2 para salir ")
while True:
    y = float(input("Ingrese opcion:"))
    if y in range(1,3):
        break
    #Meter aqui todo el calculo denuevo
    
if x == 2 or y == 1:
    n = int(input("Ingrese el numero de puntos visados: "))
    c = int(input("Ingrese cota inicial: "))

    # solicitar los puntos visados de la vista atras
    puntos1 = []

    for i in range(n):
        p1 = int(input("Ingrese vista atras: "))
        puntos1.append(p1)
    
    print(puntos1)

    # solicitar los puntos visados de la vista adelante
    puntos2 = []

    for i in range(n):
        p2 = int(input("Ingrese vista adelante: "))
        puntos2.append(p2)
    
    print(puntos2)

    # calcular las alturas del nivel topografico
    alturas = []

    for j in range(n):
        alturas.append(c + puntos1[j])

    print(alturas)

    # calcular las cotas
    #cotas = []

    #for j in range(n):
        #cotas.append(alturas - puntos2)

    #print(cotas)

elif x == 3 or y == 2:
    print("Hasta la proxima.")