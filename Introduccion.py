username = input("Ingrese nombre:")

print("Bienvenido", username)
print("Esta app")

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