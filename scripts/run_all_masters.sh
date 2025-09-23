#!/usr/bin/env bash
# Cambiar el segundo parametro con el nombre de salida deseado


set -e   # si algo falla, se detiene

# Cambiar si se quiere usar el MHC1 o MHC2
SCRIPT=../scripts/auto_netMHCIIpan.bash
ALLELES=../data/alelos/MHCII_Colombia.txt

$SCRIPT ../data/fasta/NS1_X15062_17D.fasta NS1_20all_X15062_17D_master $ALLELES
$SCRIPT ../data/fasta/NS1_PP477075_Amazonas_SAmII_onehealth.fasta NS1_20all_PP477075_Amazonas_master $ALLELES
$SCRIPT ../data/fasta/NS1_Tolima_SAmI_INS.fasta NS1_20all_Tolima_SAmI_master $ALLELES
