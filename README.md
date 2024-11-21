# Sistema de Gestión de Inventario

Este proyecto implementa un sistema de gestión de inventarios con interfaz gráfica usando `Tkinter` en Python. Permite gestionar productos, categorías, proveedores y bodegas, ofreciendo funcionalidades como manejo de stock, reportes dinámicos y exportación de datos.

---

## **Características**

### **Registro de Entidades**
1. **Productos**: Registro de productos con atributos como nombre, descripción, precio, stock inicial y categoría asociada.
2. **Categorías**: Registro de categorías con nombre y descripción.
3. **Proveedores**: Registro de proveedores con atributos como nombre, dirección, teléfono y los productos que suministran.
4. **Bodegas**: Registro de bodegas con nombre, ubicación, capacidad máxima y los productos almacenados.

### **Gestión de Stock**
- Agregar o retirar stock de productos.
- Calcular el valor total del inventario.
- Verificar disponibilidad en bodegas.

### **Relaciones Entre Entidades**
- Asociar productos a categorías, proveedores o bodegas.
- Validar límites de capacidad en bodegas.

### **Consultas y Reportes**
- Consultar información detallada de productos, categorías, proveedores y bodegas.
- Generar reportes de stock por producto y exportarlos como CSV.

---

## **Requisitos del Sistema**

### **Software**
- Python 3.8 o superior
- Librerías adicionales (ver `requirements.txt`)

### **Instalación**
1. Clona este repositorio:
   ```bash
   git clone https://github.com/JuanCano420/parcial3-sistema_inventario.git

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

3. Ejecuta el programa:
   ```bash
   python main.py