username = input("Ingrese nombre:")

print("Bienvenido", username)
print("Esta app hara los calculos para una nivelacion topografica.")
print("Ingrese 1 para una introduccion del tema, 2 para hacer los calculos o 3 para salir.")

while True:
     x = float(input("Ingrese opcion:"))
     if x in range(1,4):
         break

if x == 1:
    #Cambiar la intro a uno mas "entendible" y corta
    print("La nivelación en topografía es un proceso de medición de elevaciones o altitudes de puntos sobre la superficie de la Tierra.")
    print("Entendiéndose por elevación o altitud a la distancia vertical medida desde una superficie de referencia hasta el punto considerado.")
    print("De entre los tipos de nivelacion que hay, en esta app se usara la nivelacion compuesta que se usa cuando los puntos están separados")
    print("a una distancia mayor que el límite del campo topográfico donde es necesaria la colocación de estaciones intermedias.")
    
elif x == 2:
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

    print("Las alturas son: ", alturas)

    # calcular las cotas
    cotas = []

    for k in range(n):
        cotas.append(alturas[k] - puntos2[k])

    print("Las cotas son: ", cotas)

    if cotas != 0:
        print("El terreno es trabajable")
    else:
        print("Por favor, corrija los datos")   

elif x == 3:
    print("Hasta la proxima.")