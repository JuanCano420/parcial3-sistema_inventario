# Requerimientos del Sistema de Gestión de Inventario

Este documento detalla los requerimientos funcionales y no funcionales del sistema de gestión de inventarios desarrollado.

---

## **Requerimientos Funcionales**

### **Gestión de Productos**
1. Registrar un producto con:
   - Nombre.
   - Descripción.
   - Precio.
   - Stock inicial.
   - Categoría opcional.
2. Actualizar el stock de un producto:
   - Incrementar o decrementar el stock existente.
   - Validar que el stock no sea negativo.
3. Consultar información de un producto:
   - Nombre.
   - Descripción.
   - Precio.
   - Stock actual.
   - Categoría asociada.
   - Proveedor relacionado.

---

### **Gestión de Categorías**
1. Registrar una categoría con:
   - Nombre.
   - Descripción.
2. Consultar la información de una categoría, incluyendo la lista de productos asociados.
3. Asociar o eliminar un producto de una categoría existente.

---

### **Gestión de Proveedores**
1. Registrar un proveedor con:
   - Nombre.
   - Dirección.
   - Teléfono.
2. Consultar la información de un proveedor, incluyendo los productos que suministra.
3. Asociar o eliminar un producto de la lista de productos suministrados por un proveedor.

---

### **Gestión de Bodegas**
1. Registrar una bodega con:
   - Nombre.
   - Ubicación.
   - Capacidad máxima.
2. Consultar la información de una bodega, incluyendo la lista de productos almacenados.
3. Agregar productos a una bodega:
   - Validar que no se exceda la capacidad máxima.
4. Retirar productos de una bodega:
   - Validar que la cantidad a retirar no exceda el stock disponible.
5. Consultar la disponibilidad de un producto en una bodega específica.

---

### **Gestión de Stock**
1. Calcular el valor total del inventario:
   - Sumar el valor total de todos los productos en base a su stock actual y precio.
2. Generar reportes de stock:
   - Stock total.
   - Stock por categoría.
   - Stock por proveedor.
   - Stock por bodega.

---

## **Requerimientos No Funcionales**

1. **Interfaz Gráfica**:
   - El sistema debe tener una interfaz gráfica interactiva basada en `Tkinter`.
   - La interfaz debe permitir la creación, modificación y consulta de todas las entidades.
   - Los reportes deben visualizarse en ventanas emergentes.

2. **Exportación de Datos**:
   - El sistema debe permitir exportar los reportes de stock a un archivo CSV.

3. **Validación de Datos**:
   - Todos los formularios de entrada deben validar los datos antes de procesarlos (por ejemplo, números no negativos, campos obligatorios, etc.).

4. **Compatibilidad**:
   - El sistema debe ser compatible con Python 3.8 o superior.
   - El proyecto debe ser multiplataforma (Windows, macOS, Linux).

5. **Rendimiento**:
   - El sistema debe manejar eficientemente listas de productos, categorías, proveedores y bodegas, incluso para un número elevado de registros (hasta 1000 entidades).

6. **Extensibilidad**:
   - El sistema debe estar diseñado de forma modular, permitiendo la adición de nuevas funcionalidades sin modificar en exceso el código existente.

---

## **Casos de Uso**

1. **Registrar un Producto**:
   - El usuario introduce los detalles del producto en la interfaz y lo asocia opcionalmente a una categoría.

2. **Actualizar Stock**:
   - El usuario selecciona un producto de la lista y ajusta la cantidad de stock.

3. **Generar Reporte**:
   - El usuario hace clic en un botón para ver el reporte de stock, con la opción de exportarlo a un archivo CSV.

4. **Gestión de Bodegas**:
   - El usuario agrega productos a una bodega y verifica si hay espacio disponible.

---

## **Futuras Extensiones**

1. Implementar autenticación para diferentes roles de usuarios (administrador, operador, etc.).
2. Agregar soporte para bases de datos (SQLite o MySQL) para persistencia de datos.
3. Mejorar la interfaz gráfica con librerías avanzadas como `PyQt` o `Kivy`.
4. Agregar soporte para reportes en formato PDF.
