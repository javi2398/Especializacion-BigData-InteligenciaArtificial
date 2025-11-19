# Duckdb nos permite leer ficheros locales (CVS, parquet, etc ...)
# pyarrow nos permite soportar el formato parquet (columnar)

import os, json, textwrap, duckdb, pandas as pd
from pathlib import Path
from IPython.display import display


# Preparamos un entorno limpio de trabajo
base_dir = Path('mi_practica_UD_1')
base_dir.mkdir(exist_ok=True) # Si existe que no nos de problemas
os.chdir(base_dir)

print(f'Directorio actual de trabajo: {Path.cwd()}')

# 1. Simular un Data Warehouse (DW)
# Creamos una tabla pefectamente estructurada
dw = pd.DataFrame({
    'cliente': ['Ana', 'Antonio', 'María'],
    'edad': [25, 26, 28],
    'ciudad': ['Madrid', 'Sevilla', 'Córdoba']
})

# Guardamos la tabla en formato CSV
dw_path = Path('data_warehouse.csv')
dw.to_csv(dw_path, index=False) # Para no guardar la columna índice

# 2. Simulamos un Data Lake (DL)
# Creamos una carpeta que contendrá distintos tipos de datos
lake_base = Path('date_lake/clientes')
lake_base.mkdir(parents=True, exist_ok=True) # parents: crea automáticamente todas las carpetas
#JSON
json.dump({'nombre': 'María', 'edad': 30},open(lake_base/'maria.json', 'w'))

# Archivo de texto sin formato
(lake_base/'antonio.txt').write_text(textwrap.dedent('nombre es Antonio y edad es 32'))

# Archivo Parquet (formato columnar comprimido)
pd.DataFrame({
    'cliente': ['Rosa', 'Carmen', 'Pedro'],
    'edad': [25, 26, 28]
}).to_parquet(lake_base/'personas.parquet', index=False)

# Mostramos la estructura de mi directorio de trabajo
print('')

def tree(path="."):
    path = Path(path)
    for root, dirs, files in os.walk(path):
        # Calcula el nivel de profundidad (para indentar)
        level = Path(root).relative_to(path).parts
        indent = "    " * len(level)
        print(f"{indent}{Path(root).name}/")
        for f in files:
            print(f"{indent}    {f}")

# Mostramos la estructura de mi directorio de trabajo
print('Arbol de la carpeta actual')
tree('.')

print('Mostramos archivo Parquet (columnar)')
display(pd.read_parquet('date_lake/clientes'))


