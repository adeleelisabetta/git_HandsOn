#!/usr/bin/env python

import sys
import re
from argparse import ArgumentParser

parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# If no arguments were provided, print help
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Convert sequence to uppercase
args.seq = args.seq.upper()

# Check that the sequence contains only valid nucleotide letters
if re.fullmatch(r"[ACGTU]+", args.seq):

    has_t = "T" in args.seq
    has_u = "U" in args.seq

    if has_t and has_u:
        print("The sequence is not valid (cannot contain both T and U)")
    elif has_t:
        print("The sequence is DNA")
    elif has_u:
        print("The sequence is RNA")
    else:
        print("The sequence can be DNA or RNA")
else:
    print("The sequence is not DNA nor RNA")

# Motif search (if provided)
if args.motif:
    args.motif = args.motif.upper()
    print(
        f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ',
        end=""
    )
    if re.search(re.escape(args.motif), args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")




