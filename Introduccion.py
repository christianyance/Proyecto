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
    print(".")

elif x == 3:
    print("Hasta la proxima.")

