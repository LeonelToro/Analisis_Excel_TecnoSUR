import pandas as pd

# Datos base para costos fijos
data = {
    'TiendaID': [1, 2, 3, 4, 5],
    'SueldosMensuales': [15400000, 17200000, 14300000, 15700000, 18000000],
    'Alquiler': [8000000, 7000000, 6000000, 5000000, 7000000],
    'GastosGenerales': [2400000, 2450000, 1500000, 1000000, 2800000],
}

# Crear DataFrame
costos_fijos_tecnosur = pd.DataFrame(data)

# Guardar a CSV
costos_fijos_tecnosur.to_csv(r'C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\TecnoSUR\costos_fijos_tecnosur.csv', index=False)

print("Archivo 'costos_fijos_tecnosur.csv' generado correctamente.")
