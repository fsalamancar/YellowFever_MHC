#!/usr/bin/env bash
# Cambiar el segundo parametro con el nombre de salida deseado


set -e   # si algo falla, se detiene

SCRIPT=../scripts/auto_netMHCIIpan.bash
ALLELES=../data/alelos/MHCII_Colombia.txt

$SCRIPT ../data/fasta/PE_X15062_17D.fasta PE_15all_X15062_17D_master $ALLELES
$SCRIPT ../data/fasta/PE_PP477075_Amazonas_SAmII_onehealth.fasta PE_15all_PP477075_Amazonas_master $ALLELES
$SCRIPT ../data/fasta/PE_Tolima_SAmI_INS.fasta PE_15all_Tolima_SAmI_master $ALLELES
