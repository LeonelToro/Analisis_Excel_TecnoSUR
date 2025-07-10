import random
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# Configuraciones básicas
num_ventas = 4000
fecha_inicio = datetime(2024, 1, 1)
fecha_fin = datetime(2024, 12, 31)
dias_totales = (fecha_fin - fecha_inicio).days + 1
tiendas = [1, 2, 3, 4, 5]

# Rutas archivos
ruta_empleados = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\TecnoSUR\empleados_tecno_sur.csv"
ruta_inventario = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\TecnoSUR\inventario_tecno_sur.csv"
ruta_productos = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\TecnoSUR\productos_tecno_sur.csv"

# Leer empleados y filtrar vendedores activos
df_empleados = pd.read_csv(ruta_empleados)
df_vendedores = df_empleados[(df_empleados['Rol'] == 'Vendedor') & (df_empleados['FechaEgreso'].isnull())]
empleados_vendedores = df_vendedores.groupby('TiendaID')['EmpleadoID'].apply(list).to_dict()

# Leer inventario y filtrar productos con stock > 0
df_inventario = pd.read_csv(ruta_inventario)
df_inventario_disponible = df_inventario[df_inventario['StockActual'] > 0]
productos_disponibles_por_tienda = df_inventario_disponible.groupby('TiendaID')['ProductoID'].apply(set).to_dict()

# Leer productos reales con PrecioUnitario
df_productos = pd.read_csv(ruta_productos)

# Asegurarse de que ProductoID sea numérico por las dudas
df_productos['ProductoID'] = pd.to_numeric(df_productos['ProductoID'], errors='coerce')
df_productos.dropna(subset=['ProductoID', 'PrecioUnitario'], inplace=True)
df_productos['ProductoID'] = df_productos['ProductoID'].astype(int)

# Distribuciones ponderadas
productos_por_venta_opts = [1, 2, 3, 4, 5]
productos_por_venta_weights = [30, 30, 10, 15, 15]

cantidad_por_producto_opts = [1, 2, 3, 4, 5]
cantidad_por_producto_weights = [50, 35, 5, 5, 5]

# Generación de ventas
ventas = []

for venta_id in range(1, num_ventas + 1):
    dia_offset = random.randint(0, dias_totales - 1)
    fecha_venta = fecha_inicio + timedelta(days=dia_offset)
    fecha_id = fecha_venta.strftime('%Y%m%d')
    
    tienda_id = random.choice(tiendas)
    
    posibles_vendedores = empleados_vendedores.get(tienda_id, [])
    if not posibles_vendedores:
        continue
    empleado_id = random.choice(posibles_vendedores)
    
    cant_productos = random.choices(productos_por_venta_opts, weights=productos_por_venta_weights)[0]
    
    productos_disponibles = productos_disponibles_por_tienda.get(tienda_id, set())
    productos_disponibles = list(productos_disponibles)
    
    if len(productos_disponibles) == 0:
        continue
    
    cant_productos = min(cant_productos, len(productos_disponibles))
    productos_venta = random.sample(productos_disponibles, cant_productos)
    
    for producto_id in productos_venta:
        cantidad = random.choices(cantidad_por_producto_opts, weights=cantidad_por_producto_weights)[0]
        
        fila_producto = df_productos[df_productos['ProductoID'] == producto_id]
        if fila_producto.empty:
            continue  # producto no encontrado, evitar error
        
        precio_unitario = fila_producto['PrecioUnitario'].values[0]
        precio_total = cantidad * precio_unitario
        
        ventas.append({
            'VentaID': venta_id,
            'FechaID': int(fecha_id),
            'TiendaID': tienda_id,
            'EmpleadoID': empleado_id,
            'ProductoID': producto_id,
            'Cantidad': cantidad,
            'PrecioUnitario': precio_unitario,
            'PrecioTotal': precio_total
        })

df_ventas = pd.DataFrame(ventas)
df_ventas = df_ventas.sort_values(by=['VentaID', 'ProductoID']).reset_index(drop=True)

# Guardar el DataFrame en un archivo CSV
output_path = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\TecnoSUR"
os.makedirs(output_path, exist_ok=True)
file_path = os.path.join(output_path, "ventas_tecno_sur.csv")
df_ventas.to_csv(file_path, index=False, encoding='utf-8-sig')

print(f"Archivo guardado en: {file_path}")
print(df_ventas.head(10))
print(f"Total de ventas generadas: {len(df_ventas)}")
