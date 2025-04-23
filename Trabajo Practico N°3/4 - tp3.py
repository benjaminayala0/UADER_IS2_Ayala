class Factura:
    def __init__(self, importe_total, condicion_iva):
        """
        Inicializa una factura con importe total y condición impositiva del cliente.

        Args:
            importe_total (float): Importe total de la factura.
            condicion_iva (str): Condición impositiva del cliente. Puede ser:
                                 - 'Responsable Inscripto'
                                 - 'No Inscripto'
                                 - 'Exento'
        """
        self.importe_total = importe_total
        self.condicion_iva = condicion_iva

    def mostrar_factura(self):
        """Imprime los datos de la factura con la condición impositiva."""
        print("🧾 --- FACTURA ---")
        print(f"Importe total: ${self.importe_total:.2f}")
        print(f"Condición IVA: {self.condicion_iva}")
        print("-------------------\n")
factura1 = Factura(15000, "Responsable Inscripto")
factura2 = Factura(8200, "No Inscripto")
factura3 = Factura(4200, "Exento")

factura1.mostrar_factura()
factura2.mostrar_factura()
factura3.mostrar_factura()
