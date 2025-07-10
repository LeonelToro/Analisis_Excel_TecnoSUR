import random
import pandas as pd
import os

# Configuración de categorías, tipos y marcas
categorias = {
    "Climatización": {
        "tipos": ["Aire acondicionado", "Calefactor", "Ventilador", "Termotanque"],
        "marcas": ["Samsung", "LG", "Philco", "Electra", "BGH"]
    },
    "Audio/Video": {
        "tipos": ["Televisor", "Equipo de sonido", "Barra de sonido", "Monitor"],
        "marcas": ["Samsung", "LG", "Sony", "Philips", "Noblex"]
    },
    "Cocina": {
        "tipos": ["Microondas", "Heladera", "Cocina", "Anafe", "Pava eléctrica", "Tostadora"],
        "marcas": ["Whirlpool", "Liliana", "Philco", "Atma", "BGH"]
    },
    "Limpieza": {
        "tipos": ["Lavarropas", "Aspiradora", "Plancha", "Aspiradora robot", "Lavavajillas"],
        "marcas": ["Drean", "Whirlpool", "LG", "Electrolux", "Beko"]
    }
}

# Rango de precios por tipo de producto
rangos_precio = {
    "Aire acondicionado": (450000, 950000),
    "Calefactor": (60000, 150000),
    "Ventilador": (30000, 80000),
    "Termotanque": (120000, 280000),
    "Televisor": (250000, 800000),
    "Equipo de sonido": (100000, 400000),
    "Barra de sonido": (70000, 200000),
    "Monitor": (100000, 350000),
    "Microondas": (60000, 180000),
    "Heladera": (350000, 950000),
    "Cocina": (180000, 550000),
    "Anafe": (100000, 300000),
    "Pava eléctrica": (15000, 45000),
    "Tostadora": (15000, 35000),
    "Lavarropas": (280000, 650000),
    "Aspiradora": (70000, 220000),
    "Plancha": (18000, 45000),
    "Aspiradora robot": (250000, 500000),
    "Lavavajillas": (350000, 750000)
}

def generar_modelo():
    """Genera un código de modelo aleatorio tipo AB123"""
    letras = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
    numeros = ''.join(random.choices("0123456789", k=3))
    return f"{letras}{numeros}"

# Generación de productos simulados
productos = []

for i in range(1, 101):
    categoria = random.choice(list(categorias.keys()))
    tipo = random.choice(categorias[categoria]['tipos'])
    marca = random.choice(categorias[categoria]['marcas'])

    precio_min, precio_max = rangos_precio[tipo]
    precio = round(random.uniform(precio_min, precio_max), -3)
    costo = round(precio * random.uniform(0.6, 0.8), -2)

    modelo = generar_modelo()
    nombre = f"{marca} {tipo} {modelo}"

    productos.append({
        'ProductoID': i,
        'Nombre': nombre,
        'Categoria': categoria,
        'TipoProducto': tipo,
        'Marca': marca,
        'PrecioUnitario': precio,
        'CostoActual': costo
    })

# Guardar el CSV en la carpeta TecnoSUR
df_productos = pd.DataFrame(productos)

output_path = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\TecnoSUR"
os.makedirs(output_path, exist_ok=True)
file_path = os.path.join(output_path, "productos_tecno_sur.csv")

df_productos.to_csv(file_path, index=False, encoding='utf-8-sig')

print(f"Archivo guardado en: {file_path}")
print(df_productos.head())
