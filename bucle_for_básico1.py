#Constanza Concha
#08/04/2025

# 1 al 100
print("Ejercicio 1: Básico")
for i in range(0, 101):
    print(i)

#Múltiplos de 2
print("\nEjercicio 2: Múltiplos de 2")
for i in range(2, 501, 2):
    print(i)

# Vanilla Ice
print("\nEjercicio 3: Contando Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# Wow
print("\nEjercicio 4: Suma de números pares hasta 500,000")
suma = 0
for i in range(0, 500001, 2):
    suma += i
print("Suma total:", suma)

# Regrésame al 3
print("\nEjercicio 5: Regrésame al 3")
for i in range(2024, 0, -3):
    print(i)

# Contador dinámico
print("\nEjercicio 6: Contador dinámico")
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)