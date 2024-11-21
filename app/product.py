class Product:
    def __init__(self, name, description, price, stock, category=None):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category  # Relación con categoría

    def update_stock(self, quantity):
        """Actualizar el stock del producto."""
        if self.stock + quantity < 0:
            raise ValueError("No hay suficiente stock disponible.")
        self.stock += quantity

    def __str__(self):
        """Representación del producto como texto."""
        return f"{self.name} - {self.stock} unidades - ${self.price:.2f}"
