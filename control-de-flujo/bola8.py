#Constanza Concha
#31/03/2025

import random

def bolamágica():
    respuestas = [
        "👍 Sí, definitivamente.",
        "⭐ Con toda certeza, que sí.",
        "🔒 Sin lugar a dudas.",
        "🤔 Respuesta confusa, inténtalo de nuevo.",
        "🕛 Pregúntalo nuevamente más tarde.",
        "🤫 Mejor no decirte ahora.",
        "✖️ Mis fuentes dicen que no.",
        "🌧️ El panorama no es muy favorable.",
        "🤷‍♂️ Muy dudoso."
    ]
    
    pregunta = input("Hazme preguntas: ")
    respuesta = random.choice(respuestas)
    
    print(f"Pregunta: {pregunta}")
    print(f"Magic 8 Ball: {respuesta}")

if __name__ == "__main__":
    bolamágica()