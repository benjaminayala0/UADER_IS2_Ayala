# Producto
class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar_partes(self):
        print("✈️ Avión construido con las siguientes partes:")
        for parte in self.partes:
            print(f" - {parte}")
# Builder abstracto
class AvionBuilder:
    def crear_nuevo_avion(self):
        self.avion = Avion()

    def construir_body(self):
        pass

    def construir_turbinas(self):
        pass

    def construir_alas(self):
        pass

    def construir_tren_aterrizaje(self):
        pass

    def obtener_avion(self):
        return self.avion
# Builder concreto
class AvionComercialBuilder(AvionBuilder):
    def construir_body(self):
        self.avion.agregar_parte("Fuselaje comercial")

    def construir_turbinas(self):
        self.avion.agregar_parte("Turbina izquierda")
        self.avion.agregar_parte("Turbina derecha")

    def construir_alas(self):
        self.avion.agregar_parte("Ala izquierda")
        self.avion.agregar_parte("Ala derecha")

    def construir_tren_aterrizaje(self):
        self.avion.agregar_parte("Tren de aterrizaje")
# Director
class DirectorFabricaAviones:
    def __init__(self, builder):
        self._builder = builder

    def construir_avion(self):
        self._builder.crear_nuevo_avion()
        self._builder.construir_body()
        self._builder.construir_turbinas()
        self._builder.construir_alas()
        self._builder.construir_tren_aterrizaje()

    def obtener_avion(self):
        return self._builder.obtener_avion()
if __name__ == "__main__":
    builder = AvionComercialBuilder()
    director = DirectorFabricaAviones(builder)

    director.construir_avion()
    avion = director.obtener_avion()
    avion.mostrar_partes()
