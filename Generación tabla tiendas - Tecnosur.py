import pandas as pd
import os

# Definición de datos de tiendas
data_tiendas = {
    'TiendaID': [1, 2, 3, 4, 5],
    'Nombre': [
        'TecnoSur Flores',
        'TecnoSur Belgrano',
        'TecnoSur La Plata',
        'TecnoSur Mar del Plata',
        'TecnoSur Rosario'
    ],
    'Ciudad': [
        'CABA',
        'CABA',
        'La Plata',
        'Mar del Plata',
        'Rosario'
    ],
    'Provincia': [
        'CABA',
        'CABA',
        'Buenos Aires',
        'Buenos Aires',
        'Santa Fe'
    ],
    'FechaApertura': [
        '2019-05-15',
        '2021-08-01',
        '2020-03-10',
        '2022-02-20',
        '2018-11-30'
    ],
    'TipoTienda': [
        'Local grande',
        'Local mediano',
        'Local grande',
        'Local chico',
        'Local grande'
    ],
    'MetrosCuadrados': [320, 250, 300, 200, 350],
    'ManagerID': [None, None, None, None, None]  # Puedes modificar si querés asignar managers
}

# Crear DataFrame
df_tiendas = pd.DataFrame(data_tiendas)

# Convertir FechaApertura a datetime
df_tiendas['FechaApertura'] = pd.to_datetime(df_tiendas['FechaApertura'])

# Definir ruta de guardado
output_path = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\TecnoSUR"
os.makedirs(output_path, exist_ok=True)
file_path = os.path.join(output_path, "tiendas_tecno_sur.csv")

# Guardar CSV
df_tiendas.to_csv(file_path, index=False, encoding='utf-8-sig')

print(f"Archivo guardado en: {file_path}")
print(df_tiendas)
