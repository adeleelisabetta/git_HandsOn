#!/usr/bin/env python

import sys
from argparse import ArgumentParser

parser = ArgumentParser(
    description="Compute nucleotide percentages for DNA or RNA sequences"
)
parser.add_argument("-s", "--seq", required=True, help="Input DNA or RNA sequence")

args = parser.parse_args()

seq = args.seq.upper()
length = len(seq)

# Validate sequence
valid_nucleotides = set("ACGTU")
if not set(seq).issubset(valid_nucleotides):
    print("Error: sequence contains invalid characters")
    sys.exit(1)

# Count nucleotides
counts = {nuc: seq.count(nuc) for nuc in "ACGTU"}

# Print percentages
print("Nucleotide percentages:")
for nuc, count in counts.items():
    if count > 0:
        percentage = (count / length) * 100
        print(f"{nuc}: {percentage:.2f}%")

