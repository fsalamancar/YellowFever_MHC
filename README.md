# YellowFever MHC

Este proyecto analiza la afinidad de unión entre péptidos de las proteínas de Fiebre Amarilla y diversos alelos MHC, generando un mapa de calor que muestra las regiones con mayor o menor probabilidad de unión.

---

## Descripción del proyecto

La Fiebre Amarilla posee dos proteínas clave en la respuesta inmune: **Proteína E** y **Proteína NS1**.  
El objetivo del programa es medir el nivel de unión entre péptidos derivados de estas proteínas y distintos alelos MHC, proporcionando una visión integral de las posibles interacciones inmunes.

El flujo de trabajo es el siguiente:

1. **Entrada:**  
   - Archivos FASTA con las secuencias de aminoácidos de las proteínas de interés (E y NS1).  
   - Archivo TXT con la lista de alelos MHC (un alelo por línea).

2. **Procesamiento:**  
   - Se ejecuta `auto_netMHCIIpan`, que utiliza los archivos FASTA y la lista de alelos para generar predicciones de unión de péptidos.  
   - Los resultados se combinan en un **archivo master** que contiene las predicciones para todos los alelos.

3. **Análisis y visualización:**  
   - Con el archivo master, se ejecuta el script `mhcMaker.py`, que pedirá las rutas de:
     ```python
     fasta_path   # Ruta al archivo FASTA
     alelos_path  # Ruta al archivo TXT con la lista de alelos
     netmhc_path  # Ruta al archivo master generado por auto_netMHCIIpan
     salida_csv   # Ruta y nombre del archivo CSV de salida
     ```
   - El script genera un archivo Excel con un diagrama de color que muestra las zonas de mayor afinidad de unión para cada alelo MHC.
  
  
---

## Requisitos

- Python 3.9+  
- netMHCIIpan instalado y en el `PATH`  
- Bibliotecas de Python (instalar con `pip install -r requirements.txt`):
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`

---

## Instrucciones de uso

1. **Preparar archivos de entrada:**
   - `proteinas.fasta` — Secuencia de aminoácidos de las proteínas de Fiebre Amarilla.
   - `alelos.txt` — Lista de alelos MHC, cada uno en una línea.

2. **Ejecutar predicciones:**
   ```bash
   ./auto_netMHCIIpan proteinas.fasta alelos.txt


3. **Generar el análisis y visualización::**

  python mhcMaker.py

El programa pedirá las rutas de:

- fasta_path

- alelos_path

- netmhc_path

- salida_csv

Ejemplo de ingreso en la terminal:

```python
fasta_path = "/ruta/a/proteinas.fasta"
alelos_path = "/ruta/a/alelos.txt"
netmhc_path = "/ruta/a/master_resultados.txt"
salida_csv = "/ruta/de/salida/resultado_final.csv"
```

4. **Resultados:**

Se generará un archivo Excel con un mapa de calor que indica la afinidad de unión entre los péptidos y cada alelo MHC.

---

## Estructura del proyecto

```bash
YellowFever_MHC/
│
├── data/
│ ├── alelos/ # Archivos de texto con la lista de alelos (uno por línea)
│ └── fasta/ # Secuencias FASTA de las proteínas de Fiebre Amarilla
│
├── notebooks/
│ └── main.ipynb # Notebook de análisis/ejemplos
│
├── outputs/ # Resultados generados (master y CSV finales)
│
├── scripts/
│ ├── auto_netMHCIIpan.bash # Script para ejecutar netMHCIIpan en todos los alelos
│ └── run_all_masters.sh # Script de automatización de resultados master
│
├── src/
│ └── utils.py # Funciones auxiliares (crear_matriz, netMHC2df, marcar_peptidos)
│
├── requirements.txt # Dependencias de Python
├── mhcMarker.py # Programa principal que genera la matriz marcada
└── README.md # Este documento
```

---
## 👤 Author

**Francisco Salamanca**  
Bioinformatician | MSc in Bioinformatics  
Universidad Nacinal de Colombia | Institute of Clinical Molecular Biology
[GitHub](https://github.com/fsalamancar) • [Website](https://fsalamancar.github.io/) • [LinkedIn](https://www.linkedin.com/in/fjosesala/) • [IKMB](https://www.ikmb.uni-kiel.de/people/francisco-salamanca/)





