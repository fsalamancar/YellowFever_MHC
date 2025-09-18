"""
src/utils.py
Funciones auxiliares para análisis de MHCII y manejo de FASTA/Alelos.
"""

from pathlib import Path
import pandas as pd
import numpy as np

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



