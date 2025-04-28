#Constanza Concha
#28/04/2025
#División segura
#Objetivo: Dividir entre 2 números y evitar o alertar.
#Si el usuario quiere dividir entre 0.

def división_segura():
    try:
        num1 = int(input("Ingresa un número:"))
        num2 = int(input("Ingresa otro número:"))
        resultado= num1/num2
        print("El resultado de la división es:", resultado)
    except ZeroDivisionError:
        print("Lo sentimos no se puede realizar esta división")
    except ValueError:
        print("Error, solo debes ingresar números")
    
división_segura()
