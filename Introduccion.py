import os
os.system('cls')

username = input("Ingrese nombre:")
print(".")
print("Bienvenido", username)
print("Esta app hara los calculos para una nivelacion topografica simple.")
print("Ingrese 1 para una introduccion del tema o 2 para salir.")

while True:
     x = float(input("Ingrese opcion:"))
     if x in range(1,3):
         break

if x == 2:
    print("Hasta la proxima.")

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

if y == 2:
    print("Hasta la proxima.")  

if y == 1:
    n = int(input("Ingrese el numero de puntos visados: "))
    c = int(input("Ingrese cota inicial: "))

    while True:
        if c == 0:
            print("ERROR!")
            c = int(input("Ingrese cota inicial: "))
        else:
            break

    # solicitar los puntos visados de la vista atras
    puntos1 = []

    for i in range(n):
        p1 = float(input("Ingrese vista atras: "))
        puntos1.append(p1)
    
    print(puntos1)

    # solicitar los puntos visados de la vista adelante
    puntos2 = []

    for i in range(n):
        p2 = float(input("Ingrese vista adelante: "))
        puntos2.append(p2)
    
    print(puntos2)

    # calcular las alturas y cotas del nivel topografico
    alturas = []
    cotas = []

    if n == 2:
        h1 = c + puntos1[0]
        c2 = h1 - puntos2[0]

        h2 = c2 + puntos1[1]

        alturas = [h1, h2]
        cotas = [c, c2]
    
    if n == 3:
        h1 = c + puntos1[0]
        c2 = h1 - puntos2[0]

        h2 = c2 + puntos1[1]
        c3 = h2 - puntos2[1]

        h3 = c3 + puntos1[2]

        altura = [h1, h2, h3]
        cotas = [c, c2, c3]
    
    if n == 4:
        h1 = c + puntos1[0]
        c2 = h1 - puntos2[0]

        h2 = c2 + puntos1[1]
        c3 = h2 - puntos2[1]

        h3 = c3 + puntos1[2]
        c4 = h3 - puntos2[2]

        h4 = c4 + puntos1[3]

        alturas = [h1, h2, h3, h4]
        cotas = [c, c2, c3, c4]

    print("Las alturas son: ", alturas)
    print("Las cotas son: ", cotas)

    if cotas != 0:
        print("El terreno es trabajable")
    else:
        print("Por favor, corrija los datos")