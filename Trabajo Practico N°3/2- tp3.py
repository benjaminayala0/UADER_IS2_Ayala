class CalculadoraImpuestos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instancia

    def calcular_total(self, base_imponible):
        """
        Calcula el total de impuestos sobre una base imponible.
        
        Impuestos:
        - IVA: 21%
        - IIBB: 5%
        - Contribuciones municipales: 1.2%

        Retorna:
            float: suma total de impuestos calculados.
        """
        if base_imponible < 0:
            raise ValueError("La base imponible debe ser no negativa")

        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012

        return iva + iibb + contribuciones
    
impuestos = CalculadoraImpuestos()

total = impuestos.calcular_total(10000)
print(f"Total de impuestos sobre $10.000: ${total:.2f}")
