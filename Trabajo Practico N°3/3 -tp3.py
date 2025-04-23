class Hamburguesa:
    def __init__(self, metodo_entrega):
        """
        Inicializa una hamburguesa con un método de entrega.

        Args:
            metodo_entrega (str): 'mostrador', 'retiro', o 'delivery'
        """
        self.metodo_entrega = metodo_entrega.lower()

    def entregar(self):
        """Imprime el método de entrega de la hamburguesa."""
        if self.metodo_entrega == "mostrador":
            print("🍔 Entregar la hamburguesa en el mostrador.")
        elif self.metodo_entrega == "retiro":
            print("🍔 Cliente retirará la hamburguesa personalmente.")
        elif self.metodo_entrega == "delivery":
            print("🍔 Enviar la hamburguesa por delivery.")
        else:
            print("⚠️ Método de entrega no reconocido.")

pedido1 = Hamburguesa("mostrador")
pedido2 = Hamburguesa("retiro")
pedido3 = Hamburguesa("delivery")

pedido1.entregar()  # 🍔 Entregar la hamburguesa en el mostrador.
pedido2.entregar()  # 🍔 Cliente retirará la hamburguesa personalmente.
pedido3.entregar()  # 🍔 Enviar la hamburguesa por delivery.
