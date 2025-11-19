# Duckdb nos permite leer ficheros locales (CVS, parquet, etc ...)
# pyarrow nos permite soportar el formato parquet (columnar)

import random
import os, json, textwrap, duckdb, pandas as pd
import time
from pathlib import Path

# Simulamos que los datos nos llegan de una API, de logs, se van guardando en un Data Lake local en distintos formatos

# Crear carpeta donde se guardan los datos
DL = Path('ingestion_DL')
DL.mkdir(exist_ok=True)

# Simulamos datos que nos llegan en streaming de una api
pedidos = []
for i in range(5):
    registro = {
        'id_pedido': i + 1,
        'cliente': random.choice(['Rosa', 'Carmen', 'Juana', 'Pepa', 'Antonia']),
        'importe': round(random.uniform(20, 200), 2),
        'timestamp': pd.Timestamp.now().isoformat()
    }
    pedidos.append(registro)
    print(f'Nuevo pedido recibido: {registro}')
    time.sleep(0.5)

# Guardamos en formato JSON (sin tratamiento - ingestion bruta)
json_path = DL /'pedidos_brutos.json'
json.dump(pedidos, open(json_path,'w'), indent=5) # OJO con la tabulacion

# Transformación ligera (ETL: Extract - Transform - Load)
df = pd.DataFrame(pedidos)
df['iva'] = round(df['importe'] * 0.21, 2)

parquet_path = DL / 'pedidos_parquet.parquet'
df.to_parquet(parquet_path, index=False)

# Mostrar el contenido de cada archivo
print('\n Contenido JSON en bruto:')
with open(json_path, 'r') as f:
    print(f.read())

print('\n Contenido Parquet (procesados):')
df_lectura = pd.read_parquet(parquet_path)
print(df_lectura)