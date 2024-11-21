class Supplier:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.supplied_products = []  # Lista de productos suministrados

    def add_product(self, product):
        """Agregar un producto a la lista de productos suministrados."""
        if product not in self.supplied_products:
            self.supplied_products.append(product)

    def remove_product(self, product):
        """Eliminar un producto de la lista de productos suministrados."""
        if product in self.supplied_products:
            self.supplied_products.remove(product)

    def list_products(self):
        """Devolver una lista de nombres de productos suministrados."""
        return [product.name for product in self.supplied_products]

    def __str__(self):
        """Representación del proveedor como texto."""
        return f"{self.name} - {len(self.supplied_products)} productos suministrados"
