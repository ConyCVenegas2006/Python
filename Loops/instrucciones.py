#Constanza Concha
#Tengo sueño
#07/04/2025

#Instrucción else

contador = 0
while contador < 10:
    print ("contador")
    contador +=1

else:
    print ("dejo de contar")

#Instrucción Break

contador = 0
while contador <5:
    contador +=1

    if (contador==4):
        print('se rompio el bucle')
        break
    print("contador")

#Instrucción continue

contador = 0
while contador <5:
    contador +=1
    if  (contador ==3):
        continue
    print (contador)