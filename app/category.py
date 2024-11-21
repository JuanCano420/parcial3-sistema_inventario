class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []  # Lista de productos asociados

    def add_product(self, product):
        """Agregar un producto a la categoría."""
        if product not in self.products:
            self.products.append(product)
            product.category = self

    def remove_product(self, product):
        """Eliminar un producto de la categoría."""
        if product in self.products:
            self.products.remove(product)
            product.category = None

    def list_products(self):
        """Devolver una lista de nombres de productos."""
        return [product.name for product in self.products]

    def __str__(self):
        """Representación de la categoría como texto."""
        return f"{self.name} - {len(self.products)} productos"
