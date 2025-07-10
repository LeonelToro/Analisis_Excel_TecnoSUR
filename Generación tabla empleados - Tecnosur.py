import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker('es_AR')

# Parámetros
tiendas = {
    1: {'Nombre': 'TecnoSur Flores', 'Apertura': datetime(2018, 11, 30)},
    2: {'Nombre': 'TecnoSur Rosario', 'Apertura': datetime(2019, 5, 15)},
    3: {'Nombre': 'TecnoSur La Plata', 'Apertura': datetime(2020, 3, 10)},
    4: {'Nombre': 'TecnoSur Belgrano', 'Apertura': datetime(2021, 8, 1)},
    5: {'Nombre': 'TecnoSur Mar del Plata', 'Apertura': datetime(2022, 2, 20)},
}

turnos = ['Mañana', 'Tarde']

empleados = []

def random_date(start, end):
    """Genera fecha aleatoria entre start y end."""
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

def generar_nombre_rol(rol):
    if rol == 'Deposito':
        genero = 'M' if random.random() < 0.8 else 'F'
        nombre = fake.first_name_male() if genero == 'M' else fake.first_name_female()
        apellido = fake.last_name()
        nombre_completo = f"{nombre} {apellido}"
    else:
        nombre = fake.first_name()
        apellido = fake.last_name()
        nombre_completo = f"{nombre} {apellido}"
    return nombre_completo

# Generar empleados activos
for tienda_id, info in tiendas.items():
    apertura = info['Apertura']
    # Encargado - asignado siempre a turno Mañana
    fecha_ingreso = random_date(apertura, datetime(2024, 1, 1))
    empleados.append({
        'NombreEmpleado': generar_nombre_rol('Encargado'),
        'Rol': 'Encargado',
        'Turno': 'Mañana',
        'TiendaID': tienda_id,
        'FechaIngreso': fecha_ingreso,
        'FechaEgreso': None,
    })

    # Deposito 4 empleados (2 Mañana, 2 Tarde)
    for turno in turnos:
        for _ in range(2):
            fecha_ingreso = random_date(apertura, datetime(2024, 1, 1))
            empleados.append({
                'NombreEmpleado': generar_nombre_rol('Deposito'),
                'Rol': 'Deposito',
                'Turno': turno,
                'TiendaID': tienda_id,
                'FechaIngreso': fecha_ingreso,
                'FechaEgreso': None,
            })

    # Vendedor 4 empleados (2 Mañana, 2 Tarde)
    for turno in turnos:
        for _ in range(2):
            fecha_ingreso = random_date(apertura, datetime(2024, 1, 1))
            empleados.append({
                'NombreEmpleado': generar_nombre_rol('Vendedor'),
                'Rol': 'Vendedor',
                'Turno': turno,
                'TiendaID': tienda_id,
                'FechaIngreso': fecha_ingreso,
                'FechaEgreso': None,
            })

    # Cajero 2 empleados (1 Mañana, 1 Tarde)
    for turno in turnos:
        fecha_ingreso = random_date(apertura, datetime(2024, 1, 1))
        empleados.append({
            'NombreEmpleado': generar_nombre_rol('Cajero'),
            'Rol': 'Cajero',
            'Turno': turno,
            'TiendaID': tienda_id,
            'FechaIngreso': fecha_ingreso,
            'FechaEgreso': None,
        })

# Empleados inactivos (~30% adicionales)
num_inactivos = int(len(empleados) * 0.3)
for _ in range(num_inactivos):
    tienda_id, info = random.choice(list(tiendas.items()))
    apertura = info['Apertura']

    fecha_ingreso = random_date(apertura, datetime(2023, 12, 31))
    fecha_egreso = random_date(fecha_ingreso, datetime(2024, 12, 31))

    rol = random.choice(['Deposito', 'Vendedor', 'Cajero'])
    turno = random.choice(turnos)

    empleados.append({
        'NombreEmpleado': generar_nombre_rol(rol),
        'Rol': rol,
        'Turno': turno,
        'TiendaID': tienda_id,
        'FechaIngreso': fecha_ingreso,
        'FechaEgreso': fecha_egreso,
    })

# Crear DataFrame
df_empleados = pd.DataFrame(empleados)

# Convertir fechas a datetime
df_empleados['FechaIngreso'] = pd.to_datetime(df_empleados['FechaIngreso'])
df_empleados['FechaEgreso'] = pd.to_datetime(df_empleados['FechaEgreso'])

# Ordenar por fecha ingreso y reasignar EmpleadoID
df_empleados = df_empleados.sort_values(by='FechaIngreso').reset_index(drop=True)
df_empleados['EmpleadoID'] = df_empleados.index + 1

# Ordenar columnas
column_order = ['EmpleadoID', 'NombreEmpleado', 'Rol', 'Turno', 'TiendaID', 'FechaIngreso', 'FechaEgreso']
df_empleados = df_empleados[column_order]

# Convertir fechas a date para evitar timestamp
df_empleados['FechaIngreso'] = df_empleados['FechaIngreso'].dt.date
df_empleados['FechaEgreso'] = df_empleados['FechaEgreso'].dt.date

# Ruta de guardado
output_path = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\TecnoSUR"
os.makedirs(output_path, exist_ok=True)
file_path = os.path.join(output_path, "empleados_tecno_sur.csv")

# Guardar CSV
df_empleados.to_csv(file_path, index=False, encoding='utf-8-sig')

print(f"Archivo guardado en: {file_path}")
print(df_empleados.head())
print(f"Total empleados generados: {len(df_empleados)}")
