

peso = float (input ("Cuál es tu peso terrestre? "))
planeta = int (input ("Cuál es el número de tu planeta?(1-7)"))
gravedad = float  (input (0.38 , 0.91 , 0.38 , 2.53 , 1.07 , 0.89))

if planeta == 1:
    print  ("Mercurio")
elif  (planeta == 2):
    print ("Venus")
elif  (planeta == 3):
    print ("Marte")
elif (planeta == 4):
    print ("Júpiter")
elif (planeta == 5):
    print ("Saturno")
elif (planeta == 6):
    print ("Urano ")
elif (planeta == 7):
    print("Neptuno")
else:
    print("Número de planeta no válido")