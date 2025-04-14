
import random

print('Este es un bucle que imprime 5 veces')
for num in range(0,5):
    print(f'num es: {num}')

datos = [0,1,2,3,4,5,]
aleatorio = random.choice(datos)

print(f'Sorpresa {aleatorio}')

if aleatorio == 0:
    print('Los flamencos se vuelven rosados por comer camarones')
elif(aleatorio == 1):
    print('El único alimento que no se descompone es la miel')
elif (aleatorio == 2):
    print ("Los camarones solo pueden nadar hacia atrás")
elif (aleatorio == 3):
    print("La vida útil de una papila gustativa es de aproximadamente 10 días")
elif (aleatorio == 4):
     print ("Es imposilble estordunar mientras se duerme")
else:
    print('Es ilegal cantar desafinado en Carolina del Norte')