#Constanza Concha
#28/04/2025
#Objetivo: Mostrar un elemento de una lista por su posición, manejando si la posición no existe.

def mostrar_elemento():
    
    frutas = ["Manzana", "Banana", "Naranja", "Palta"]
    try:
        indice = int(input("Elige una posición (0 a 3):"))
        print("Fruta elegida:", frutas[indice])
    except IndexError:
        print("Esta posición no existe en la lista")
    except ValueError:
        print("Debes ingresar números")

mostrar_elemento()