# Ejercicio 2: Crear una clase Estudiante que contenga los atributos nombre, edad y calificacion.
# La clase debe tener un método que evalúe si el estudiante ha aprobado o reprobado según su calificación.

class Estudiante(): #clase estudiante
    def __init__(self, nombre, edad, calificacion): #metodo constructor
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion
    def Evaluar(self): #metodo para evaluar la calificacion del estudiante
        if self.calificacion >= 5: #condicionales
            return(f"el estudiante {self.nombre} con calificacion {self.calificacion} ha aprobado.")
        else: #condicionales
            return(f"la estudiante {self.nombre} con calificacion {self.calificacion} ha reprobado.")

estudiante1 = Estudiante("Juan", 20, 8) #instancia de la clase estudiante
estudiante2 = Estudiante("Maria", 19, 4) #instancia de la clase estudiante

print(estudiante1.Evaluar())
print(estudiante2.Evaluar())

