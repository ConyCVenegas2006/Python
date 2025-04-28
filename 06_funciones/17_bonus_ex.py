#Constanza Concha
#28/04/2025
#Objetivo: Repetir hasta que lo haga bien, podemos usar bucles junto con un try.

def pedir_numero_repetido():
    
    while True: 
        try:
            numero = int(input("Escribe un número entero:"))
            print("¡Gracias! Tu número es:", numero)
            break
        except ValueError:
            print("Eso no es un número válido")

pedir_numero_repetido()