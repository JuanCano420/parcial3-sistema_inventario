from tkinter import Tk
from gui import InventoryGUI
from stock_manager import StockManager

def main():
    # Crear el gestor de inventario
    stock_manager = StockManager()

    # Configurar la interfaz gráfica
    root = Tk()
    root.title("Sistema de Gestión de Inventario")
    app = InventoryGUI(root, stock_manager)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
