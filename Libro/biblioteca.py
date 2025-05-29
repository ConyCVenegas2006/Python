#Proyecto Biblioteca virtual
class Libro:

    def __init__(self, titulo,autor, pagina, genero, copias_disponible):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pagina
        self.genero = genero
        self.copias_disponible = copias_disponible

    def atributos(self):
        print(self.titulo, ":", sep=" ")
        print("Autor:", self.autor)
        print("Paginas:", self.pagina)
        print("Genero:", self.genero)
        print("Copias disponibles:", self.copias_disponible)


    def incrementar_copias(self, nuevas_copias):
        self.copias_disponible = self.copias_disponible+nuevas_copias
        pass
    def esta_disponible(self):
        return self.copias_disponible > 0
    
    def agotado(self):
            self.copias_disponible == 0
            print(self.titulo, "está agotado.")

    def prestar (self, copias = 1):
         if self.copias_disponible >= copias:
            self.copias_disponible -= copias
            print(f"Has prestado {copias} copias de '{self.titulo}'.")
         else:
              print(f"No hay suficientes copias de '{self.titulo}' disponibles para prestar.")

        
mi_Libro = Libro("Principito", "Antoine de Saint-Exupéry", 96, "Ficción", 5)
mi_Libro.agotado()
print(self.titulo, "Está agotado")

mi_Libro.atributos()
mi_Libro.incrementar_copias(3)
print("Atributos después de incrementar copias:")
mi_Libro.atributos()




