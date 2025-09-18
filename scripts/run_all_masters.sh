#!/usr/bin/env bash
set -e   # si algo falla, se detiene

SCRIPT=../scripts/auto_netMHCIIpan.bash
ALLELES=../data/alelos/MHCII_Colombia.txt

$SCRIPT ../data/fasta/PE_X15062_17D.fasta PE_X15062_17D_master $ALLELES
$SCRIPT ../data/fasta/PE_PP477075_Amazonas_SAmII_onehealth.fasta PE_PP477075_Amazonas_master $ALLELES
$SCRIPT ../data/fasta/PE_Tolima_SAmI_INS.fasta PE_Tolima_SAmI_master $ALLELES
