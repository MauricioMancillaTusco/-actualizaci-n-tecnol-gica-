class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {self.promedio():.2f}")

e1 = Estudiante("Carlos")
e1.agregar_nota(80)
e1.agregar_nota(95)
print("Promedio:", e1.promedio())  
e1.mostrar_informacion()
 