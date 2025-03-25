pistas = ("Puerta Roja", 221, "Londres", 314, "Watson", 7, "Moriarty")


#Cuál es la primera pista?

print(pistas[0])


#Cuál es la última pista?

print(pistas[6])


#Cuántas pistas hay en total?

print(len(pistas))


#Está la palabra "Londres" en las pistas?

print("Londres" in pistas)


 #Desempaqueta las primeras tres pistas


tuplas= ("Puerta Roja", 221, "Londres")

a,b,c =tuplas

print(a,b,c)

#Crea una nueva tupla con pistas adicionales
pistas = ("Puerta Roja", 221, "Londres", 314, "Watson", 7, "Moriarty")
pistas2 = ("Planta","platanos")
nueva_pistas = pistas + pistas2
print(nueva_pistas)


#Encuentra la posición de "Watson"

print(pistas.index("Watson"))


#Cuántas veces aparece el número 7 en las pistas
print(pistas.count (7))