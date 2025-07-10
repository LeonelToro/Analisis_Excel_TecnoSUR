import random
import pandas as pd
import os

# IDs de tiendas (según estructura definida)
tiendas = [1, 2, 3, 4, 5]  # Flores, Belgrano, Rosario, La Plata, Mar del Plata
productos = list(range(1, 101))  # ProductoID del 1 al 100

inventario = []

for tienda_id in tiendas:
    # Selecciona entre 50 y 80 productos únicos para esta tienda
    productos_tienda = random.sample(productos, random.randint(50, 80))
    
    for producto_id in productos_tienda:
        stock = random.randint(0, 35)  # Stock entre 0 y 35
        inventario.append({
            "TiendaID": tienda_id,
            "ProductoID": producto_id,
            "StockActual": stock
        })

# Crear DataFrame
df_inventario = pd.DataFrame(inventario)

# Ordenar por TiendaID y ProductoID ascendente
df_inventario = df_inventario.sort_values(by=['TiendaID', 'ProductoID']).reset_index(drop=True)

# Guardar CSV
output_path = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\TecnoSUR"
os.makedirs(output_path, exist_ok=True)
file_path = os.path.join(output_path, "inventario_tecno_sur.csv")

df_inventario.to_csv(file_path, index=False, encoding='utf-8-sig')

print(f"Archivo guardado en: {file_path}")
print(df_inventario.head())
