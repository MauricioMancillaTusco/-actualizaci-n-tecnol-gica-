# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def emitir_sonido(self):
        print("Este animal hace un sonido")


# Clases hijas
class Perro(Animal):
    def emitir_sonido(self):
        print("Guau Guau")


class Gato(Animal):
    def emitir_sonido(self):
        print("Miau")


class Pajaro(Animal):
    def emitir_sonido(self):
        print("Pío pío")


# Función que aplica polimorfismo
def hacer_emitir_sonido(animales: list):
    for animal in animales:
        animal.emitir_sonido()


# Ejemplo de uso
animales = [
    Perro("Fido", 3),
    Gato("Michi", 2),
    Pajaro("Piolín", 1),
    Animal("Genérico", 5)
]

hacer_emitir_sonido(animales)