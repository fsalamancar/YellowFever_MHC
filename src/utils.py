"""
src/utils.py
Funciones auxiliares para análisis de MHCII y manejo de FASTA/Alelos.
"""

from pathlib import Path
import pandas as pd
import numpy as np
from pathlib import Path
import re
import pandas as pd
from io import StringIO

def crear_matriz(fasta_path: str, alleles_path: str) -> 'pd.DataFrame':
    """
    Crea un DataFrame vacío (NaN) para mapear las uniones
    entre una secuencia de aminoácidos y una lista de alelos DRB1.

    Parámetros
    ----------
    fasta_path : str
        Ruta al archivo FASTA con una sola secuencia.
        Ejemplo: "../data/fasta/NS1_Brasil_PV454340_SAmI.fasta"
    alleles_path : str
        Ruta al archivo de texto con alelos.
        Ejemplo: "../data/alelos/MHCII_Colombia.txt"

    Retorna
    -------
    pd.DataFrame
        DataFrame con:
        - Filas: alelos DRB1 únicos (ordenados).
        - Columnas: aminoácidos de la secuencia.
        - Celdas: NaN (listas para mapear uniones).
    """
    import pandas as pd
    import numpy as np
    from pathlib import Path

    # --- Leer la secuencia del FASTA ---
    with open(fasta_path) as f:
        lines = f.read().splitlines()
    # omite la cabecera (línea 0) y toma la secuencia (línea 1)
    sequence = lines[1].strip()

    # --- Extraer alelos DRB1 ---
    alleles_txt = Path(alleles_path).read_text().splitlines()
    drb1 = [
        token.replace("=", "")
        for line in alleles_txt
        for token in line.split()
        if "DRB1" in token.upper()
    ]
    drb1_unique = sorted(set(drb1))

    # --- Construir DataFrame vacío ---
    df = pd.DataFrame(
        np.nan,
        index=drb1_unique,      # filas: alelos
        columns=list(sequence)  # columnas: aminoácidos
    )

    return df




def netMHC2df(filepath: str | Path) -> pd.DataFrame:
    """
    Convierte la salida cruda de NetMHCIIpan en un DataFrame de pandas.

    - Quita comentarios (#) y separadores de guiones.
    - Une valores como "<= WB" en una sola celda ("<=WB") para que no rompan el parseo.
    - Devuelve un DataFrame con las columnas originales.

    Parameters
    ----------
    filepath : str or Path
        Ruta al archivo de salida .xls (en realidad texto con separadores por espacio).

    Returns
    -------
    pd.DataFrame
        DataFrame con todas las filas, incluyendo las que contienen '<= WB'
        en la columna BindLevel.
    """
    filepath = Path(filepath)
    cleaned_lines = []

    with filepath.open() as f:
        for line in f:
            # Saltar líneas vacías, comentarios o separadores de guiones
            if not line.strip() or line.startswith("#") or line.startswith("-"):
                continue
            # Unir "<= WB" -> "<=WB" para que pandas lo trate como un solo campo
            line = re.sub(r"<=\s+([A-Za-z0-9]+)", r"<=\1", line)
            cleaned_lines.append(line)

    # Crear DataFrame
    df = pd.read_csv(
        StringIO("".join(cleaned_lines)),
        sep=r"\s+",
        engine="python"
    )

    # Si prefieres volver a mostrar "<= WB" en lugar de "<=WB":
    if "BindLevel" in df.columns:
        df["BindLevel"] = df["BindLevel"].str.replace("<=WB", "<= WB", regex=False)

    return df
