class Warehouse:
    def __init__(self, name, location, max_capacity):
        self.name = name
        self.location = location
        self.max_capacity = max_capacity
        self.stored_products = {}  # Diccionario: {producto: cantidad}

    def add_product(self, product, quantity):
        """Agregar stock de un producto."""
        if quantity <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        
        total_stock = sum(self.stored_products.values())
        if total_stock + quantity > self.max_capacity:
            raise ValueError("Capacidad máxima excedida.")
        
        if product in self.stored_products:
            self.stored_products[product] += quantity
        else:
            self.stored_products[product] = quantity

    def remove_product(self, product, quantity):
        """Retirar stock de un producto."""
        if product not in self.stored_products or self.stored_products[product] < quantity:
            raise ValueError("Cantidad insuficiente en el almacén.")
        
        self.stored_products[product] -= quantity
        if self.stored_products[product] == 0:
            del self.stored_products[product]

    def get_product_quantity(self, product):
        """Consultar cantidad de un producto en el almacén."""
        return self.stored_products.get(product, 0)

    def list_products(self):
        """Devolver una lista de productos almacenados."""
        return {product.name: quantity for product, quantity in self.stored_products.items()}

    def __str__(self):
        """Representación de la bodega como texto."""
        return f"{self.name} - Capacidad utilizada: {sum(self.stored_products.values())}/{self.max_capacity}"
