#Constanza Concha
#tengo sueño
#02/04/2025

respuesta = input("Estás cansado?(si/no):").strip().lower()
cansado = respuesta == "si"
if not cansado:
    print("¡Es hora de programar!")
else:
    print("Tómate un descanso, lo necesitas")
