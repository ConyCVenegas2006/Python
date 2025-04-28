#Constanza Concha 
#28/04/2025
#Ejercicio 1 Converción segura a número.
#Objetivo: Pedir un número al usuario y evitar errores si escribe letras.

def pedir_numero ():
    try: 
      numero = int(input("Escribe un número entero:"))
      print ("¡Gracias! Tú número es:", numero )
    except ValueError:
       print("Eso no es un número válido. Intenta otra vez:")

pedir_numero ()