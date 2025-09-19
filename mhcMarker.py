#master function

#!/usr/bin/env python3
import pandas as pd
import warnings
import sys
from pathlib import Path

# Evitar warnings innecesarios
warnings.filterwarnings("ignore")

# Importa las funciones personalizadas
sys.path.append('src/')
from utils import crear_matriz, netMHC2df, marcar_peptidos


def generar_matriz_marcada(
    fasta_path: str,
    alelos_path: str,
    netmhc_path: str,
    salida_csv: str
) -> pd.DataFrame:
    """
    Crea una matriz secuencia vs MHC, filtra resultados de netMHCIIpan
    y marca péptidos de alta/baja afinidad.

    Parámetros
    ----------
    fasta_path : str
        Ruta al archivo FASTA con las secuencias.
    alelos_path : str
        Ruta al archivo de alelos MHCII.
    netmhc_path : str
        Ruta al archivo XLS de salida de netMHCIIpan.
    salida_csv : str
        Ruta donde guardar el CSV final.

    Retorna
    -------
    pd.DataFrame
        Matriz final con péptidos marcados.
    """
    matriz = crear_matriz(fasta_path, alelos_path)
    matriz.index.name = 'MHC'

    mhc_master = netMHC2df(netmhc_path)

    mhc_filt = mhc_master[
        mhc_master["BindLevel"].notna() &
        (mhc_master["BindLevel"].str.strip() != "NA")
    ]

    matriz_final = marcar_peptidos(matriz, mhc_filt)
    matriz_final.to_csv(salida_csv, index=True)
    return matriz_final


if __name__ == "__main__":
    # === Inputs interactivos para el usuario ===
    fasta_path  = input("Ruta al archivo FASTA: ").strip()
    alelos_path = input("Ruta al archivo de alelos: ").strip()
    netmhc_path = input("Ruta al archivo XLS de netMHCIIpan: ").strip()
    salida_csv  = input("Ruta para guardar el CSV final: ").strip()

    # Ejecuta la función principal
    resultado = generar_matriz_marcada(
        fasta_path=fasta_path,
        alelos_path=alelos_path,
        netmhc_path=netmhc_path,
        salida_csv=salida_csv
    )

    print(f"\nProceso finalizado. Matriz guardada en: {salida_csv}")

    
