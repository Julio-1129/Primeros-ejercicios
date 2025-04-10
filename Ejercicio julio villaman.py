# Ejercicio 1: Crear una clase Libro con atributos título, autor y número de páginas.
# La clase debe tener un método para mostrar la información del libro y otro para actualizar el número de páginas.
class Libro: #clase libro
    def __init__(self, titulo, autor, num_paginas): #metodo constructor
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacion(self): #metodo para mostrar la informacion del libro
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")

    def actualizar_paginas(self, new_paginas): #metodo para actualizar el numero de paginas
        self.num_paginas = new_paginas
        print(f"El número de páginas ha sido actualizado a {self.num_paginas}.")

libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 600) #instancia de la clase libro
libro1.mostrar_informacion() 
libro1.actualizar_paginas(1100) 
libro1.mostrar_informacion() 


libro2 = Libro("El amor en los tiempos del colera", "Gabriel Garcia Marquez", 400)
libro2.mostrar_informacion()
libro2.actualizar_paginas(500)
libro2.mostrar_informacion()