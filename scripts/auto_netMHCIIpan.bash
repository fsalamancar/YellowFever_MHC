#!/usr/bin/env bash

#editar las lineas netMHCIIpan -f "$fasta" -a "$A" -length 10 <-- Poner el valor de longitud del mer


run_netmhcii() {
  local fasta="$1"     # 1er argumento: archivo fasta
  local outfile="$2"   # 2do argumento: nombre base de salida (sin .xls)
  local alleles="$3"   # 3er argumento: archivo con lista de alelos

  # borrar salida previa
  rm -f "${outfile}.xls"
  local first=1

  while IFS= read -r A; do
    if [ "$first" -eq 1 ]; then
      # primera iteración: quitar primeras 14 y las últimas 3
      netMHCIIpan -f "$fasta" -a "$A" -length 20 -xls \
        | awk 'NR>14 {buf[NR]=$0} END {for (i=15; i<=NR-3; i++) print buf[i]}' \
        > "${outfile}.xls"
      first=0
    else
      # siguientes: quitar primeras 16 y las últimas 3
      netMHCIIpan -f "$fasta" -a "$A" -length 20 -xls \
        | awk 'NR>16 {buf[NR]=$0} END {for (i=17; i<=NR-3; i++) print buf[i]}' \
        >> "${outfile}.xls"
    fi
  done < "$alleles"

  # 🔹 eliminar carpeta temporal generada por netMHCIIpan
  rm -rf NetMHCIIpan_out
}

# --- Uso ---
# $1 = archivo FASTA
# $2 = nombre base de salida
# $3 = archivo con alelos
run_netmhcii "$1" "$2" "$3"
