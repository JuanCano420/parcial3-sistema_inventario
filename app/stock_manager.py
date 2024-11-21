from product import Product
from category import Category
from supplier import Supplier
from warehouse import Warehouse
class StockManager:
    def __init__(self):
        self.products = {}
        self.categories = {}
        self.suppliers = {}
        self.warehouses = {}

    # Gestión de Productos
    def create_product(self, name, description, price, stock, category_name=None):
        """Crear un nuevo producto y asociarlo a una categoría, si se especifica."""
        category = self.categories.get(category_name)
        product = Product(name, description, price, stock, category)
        self.products[name] = product
        if category:
            category.add_product(product)
        return product

    def update_stock(self, product_name, quantity):
        """Actualizar el stock de un producto."""
        product = self.products.get(product_name)
        if not product:
            raise ValueError("Producto no encontrado.")
        product.update_stock(quantity)

    # Gestión de Categorías
    def create_category(self, name, description):
        """Crear una nueva categoría."""
        category = Category(name, description)
        self.categories[name] = category
        return category

    # Gestión de Proveedores
    def create_supplier(self, name, address, phone):
        """Crear un nuevo proveedor."""
        supplier = Supplier(name, address, phone)
        self.suppliers[name] = supplier
        return supplier

    def add_product_to_supplier(self, supplier_name, product_name):
        """Asociar un producto a un proveedor."""
        supplier = self.suppliers.get(supplier_name)
        product = self.products.get(product_name)
        if not supplier or not product:
            raise ValueError("Proveedor o producto no encontrado.")
        supplier.add_product(product)

    # Gestión de Bodegas
    def create_warehouse(self, name, location, max_capacity):
        """Crear una nueva bodega."""
        warehouse = Warehouse(name, location, max_capacity)
        self.warehouses[name] = warehouse
        return warehouse

    def add_stock_to_warehouse(self, warehouse_name, product_name, quantity):
        """Agregar stock de un producto a una bodega."""
        warehouse = self.warehouses.get(warehouse_name)
        product = self.products.get(product_name)
        if not warehouse or not product:
            raise ValueError("Bodega o producto no encontrado.")
        warehouse.add_product(product, quantity)

    def remove_stock_from_warehouse(self, warehouse_name, product_name, quantity):
        """Retirar stock de un producto de una bodega."""
        warehouse = self.warehouses.get(warehouse_name)
        product = self.products.get(product_name)
        if not warehouse or not product:
            raise ValueError("Bodega o producto no encontrado.")
        warehouse.remove_product(product, quantity)

    # Reportes
    def generate_stock_report(self):
        """Generar un informe general del stock."""
        report = {}
        for product_name, product in self.products.items():
            report[product_name] = {
                "Stock": product.stock,
                "Precio Total": product.price * product.stock
            }
        return report
