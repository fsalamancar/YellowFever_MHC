#!/usr/bin/env python3
import pandas as pd
import warnings
import sys
from pathlib import Path

warnings.filterwarnings("ignore")

# Importa funciones
sys.path.append('src/')
from utils import crear_matriz, netMHC2df, marcar_peptidos


def generar_matriz_marcada(
    fasta_path: str,
    alelos_path: str,
    netmhc_path: str,
    salida_csv: str
) -> pd.DataFrame:
    """
    Crea la matriz secuencia vs MHC, filtra resultados de netMHCIIpan
    y marca péptidos de alta/baja afinidad.
    """
    matriz = crear_matriz(fasta_path, alelos_path)
    matriz.index.name = 'MHC'

    mhc_master = netMHC2df(netmhc_path)

    mhc_filt = mhc_master[
        mhc_master["BindLevel"].notna() &
        (mhc_master["BindLevel"].str.strip() != "NA")
    ]

    matriz_final = marcar_peptidos(matriz, mhc_filt)

    # Guarda en CSV
    Path(salida_csv).parent.mkdir(parents=True, exist_ok=True)
    matriz_final.to_csv(salida_csv, index=True)
    return matriz_final


if __name__ == "__main__":
    fasta_path  = input("Ruta al archivo FASTA: ").strip()
    alelos_path = input("Ruta al archivo de alelos: ").strip()
    netmhc_path = input("Ruta al archivo XLS de netMHCIIpan: ").strip()

    # Carpeta de salida por defecto
    default_dir = Path("outputs")
    default_dir.mkdir(exist_ok=True)

    nombre_archivo = input(
        f"Nombre del archivo de salida:"
    ).strip()

    if not nombre_archivo:
        nombre_archivo = "matriz_marcada.csv"
    elif not nombre_archivo.lower().endswith(".csv"):
        nombre_archivo += ".csv"

    salida_csv = default_dir / nombre_archivo

    resultado = generar_matriz_marcada(
        fasta_path=fasta_path,
        alelos_path=alelos_path,
        netmhc_path=netmhc_path,
        salida_csv=str(salida_csv)
    )

    print(f"\nProceso finalizado. Matriz guardada en: {salida_csv}")