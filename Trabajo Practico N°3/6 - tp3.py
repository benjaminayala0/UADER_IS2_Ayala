# Clase Prototype
class Note(object):

    def __init__(self, fraction):
        self.fraction = fraction

    def get(self):
        return self.fraction

    def clone(self):
        return Note(self.fraction)


# Objeto original
x = Note(10)
print("Valor almacenado en (x) fraction %d" % (x.get()))

# Primer clon
a = x.clone()
print("Valor almacenado en (a) fraction %d" % (a.get()))

# Segundo clon a partir del primero
b = a.clone()
print("Valor almacenado en (b) fraction %d" % (b.get()))

# Verificación de independencia de instancias
a.fraction = 20
print("\nLuego de modificar a.fraction = 20")
print("x.fraction =", x.get())  # Debe seguir siendo 10
print("a.fraction =", a.get())  # Debe ser 20
print("b.fraction =", b.get())  # Debe seguir siendo 10
