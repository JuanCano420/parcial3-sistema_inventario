import tkinter as tk
from tkinter import ttk, messagebox
from product import Product
from category import Category
from supplier import Supplier
from warehouse import Warehouse

class InventoryGUI:
    def __init__(self, root,stock_manager):
        self.root = root
        self.stock_manager = stock_manager

        # Diccionarios para almacenar las entidades
        self.categories = {}
        self.suppliers = {}
        self.warehouses = {}
        self.products = {}

        # Crear las pestañas principales
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Pestañas: Productos, Categorías, Proveedores, Bodegas
        self.create_product_tab()
        self.create_category_tab()
        self.create_supplier_tab()
        self.create_warehouse_tab()

    def create_product_tab(self):
        product_tab = ttk.Frame(self.notebook)
        self.notebook.add(product_tab, text="Productos")

        # Widgets
        ttk.Label(product_tab, text="Nombre del Producto:").grid(row=0, column=0, padx=5, pady=5)
        self.product_name_entry = ttk.Entry(product_tab)
        self.product_name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(product_tab, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.product_desc_entry = ttk.Entry(product_tab)
        self.product_desc_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(product_tab, text="Precio:").grid(row=2, column=0, padx=5, pady=5)
        self.product_price_entry = ttk.Entry(product_tab)
        self.product_price_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(product_tab, text="Stock Inicial:").grid(row=3, column=0, padx=5, pady=5)
        self.product_stock_entry = ttk.Entry(product_tab)
        self.product_stock_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(product_tab, text="Categoría:").grid(row=4, column=0, padx=5, pady=5)
        self.product_category_combobox = ttk.Combobox(product_tab, values=list(self.categories.keys()))
        self.product_category_combobox.grid(row=4, column=1, padx=5, pady=5)

        ttk.Button(product_tab, text="Crear Producto", command=self.create_product).grid(row=5, column=0, columnspan=2, pady=10)

        self.product_listbox = tk.Listbox(product_tab, width=50, height=10)
        self.product_listbox.grid(row=6, column=0, columnspan=2, pady=10)

    def create_category_tab(self):
        category_tab = ttk.Frame(self.notebook)
        self.notebook.add(category_tab, text="Categorías")

        ttk.Label(category_tab, text="Nombre de la Categoría:").grid(row=0, column=0, padx=5, pady=5)
        self.category_name_entry = ttk.Entry(category_tab)
        self.category_name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(category_tab, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.category_desc_entry = ttk.Entry(category_tab)
        self.category_desc_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(category_tab, text="Crear Categoría", command=self.create_category).grid(row=2, column=0, columnspan=2, pady=10)

        self.category_listbox = tk.Listbox(category_tab, width=50, height=10)
        self.category_listbox.grid(row=3, column=0, columnspan=2, pady=10)

    def create_supplier_tab(self):
        supplier_tab = ttk.Frame(self.notebook)
        self.notebook.add(supplier_tab, text="Proveedores")

        ttk.Label(supplier_tab, text="Nombre del Proveedor:").grid(row=0, column=0, padx=5, pady=5)
        self.supplier_name_entry = ttk.Entry(supplier_tab)
        self.supplier_name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(supplier_tab, text="Dirección:").grid(row=1, column=0, padx=5, pady=5)
        self.supplier_address_entry = ttk.Entry(supplier_tab)
        self.supplier_address_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(supplier_tab, text="Teléfono:").grid(row=2, column=0, padx=5, pady=5)
        self.supplier_phone_entry = ttk.Entry(supplier_tab)
        self.supplier_phone_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(supplier_tab, text="Crear Proveedor", command=self.create_supplier).grid(row=3, column=0, columnspan=2, pady=10)

        self.supplier_listbox = tk.Listbox(supplier_tab, width=50, height=10)
        self.supplier_listbox.grid(row=4, column=0, columnspan=2, pady=10)

    def create_warehouse_tab(self):
        warehouse_tab = ttk.Frame(self.notebook)
        self.notebook.add(warehouse_tab, text="Bodegas")

        ttk.Label(warehouse_tab, text="Nombre de la Bodega:").grid(row=0, column=0, padx=5, pady=5)
        self.warehouse_name_entry = ttk.Entry(warehouse_tab)
        self.warehouse_name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(warehouse_tab, text="Ubicación:").grid(row=1, column=0, padx=5, pady=5)
        self.warehouse_location_entry = ttk.Entry(warehouse_tab)
        self.warehouse_location_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(warehouse_tab, text="Capacidad Máxima:").grid(row=2, column=0, padx=5, pady=5)
        self.warehouse_capacity_entry = ttk.Entry(warehouse_tab)
        self.warehouse_capacity_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(warehouse_tab, text="Crear Bodega", command=self.create_warehouse).grid(row=3, column=0, columnspan=2, pady=10)

        self.warehouse_listbox = tk.Listbox(warehouse_tab, width=50, height=10)
        self.warehouse_listbox.grid(row=4, column=0, columnspan=2, pady=10)

    def create_product(self):
        name = self.product_name_entry.get()
        desc = self.product_desc_entry.get()
        price = float(self.product_price_entry.get())
        stock = int(self.product_stock_entry.get())
        category_name = self.product_category_combobox.get()

        category = self.categories.get(category_name)
        product = Product(name, desc, price, stock, category)
        self.products[name] = product

        if category:
            category.add_product(product)

        self.product_listbox.insert(tk.END, f"{name} - {stock} unidades - ${price}")

    def create_category(self):
        name = self.category_name_entry.get()
        desc = self.category_desc_entry.get()
        category = Category(name, desc)
        self.categories[name] = category
        self.category_listbox.insert(tk.END, f"{name} - {desc}")

        # Actualizar combobox de productos
        self.product_category_combobox['values'] = list(self.categories.keys())

    def create_supplier(self):
        name = self.supplier_name_entry.get()
        address = self.supplier_address_entry.get()
        phone = self.supplier_phone_entry.get()
        supplier = Supplier(name, address, phone)
        self.suppliers[name] = supplier
        self.supplier_listbox.insert(tk.END, f"{name} - {phone}")

    def create_warehouse(self):
        name = self.warehouse_name_entry.get()
        location = self.warehouse_location_entry.get()
        capacity = int(self.warehouse_capacity_entry.get())
        warehouse = Warehouse(name, location, capacity)
        self.warehouses[name] = warehouse
        self.warehouse_listbox.insert(tk.END, f"{name} - Capacidad: {capacity}")

# Ejecución
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()
