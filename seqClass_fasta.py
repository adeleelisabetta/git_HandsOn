#!/usr/bin/env python3

import sys
import re
from argparse import ArgumentParser
from pathlib import Path


def main():
    parser = ArgumentParser(description="Classify a sequence as DNA or RNA")

    parser.add_argument(
        "-s", "--seq",
        type=str,
        required=True,
        help="Input sequence OR path to a file containing the sequence"
    )

    parser.add_argument(
        "-m", "--motif",
        type=str,
        required=False,
        help="Motif to search for in the sequence"
    )

    # If no arguments were provided, print help and exit
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    # If --seq is a file, read sequence from file
    seq_path = Path(args.seq)
    if seq_path.is_file():
        with open(seq_path) as f:
            seq = f.read().strip()
    else:
        seq = args.seq

    # Convert sequence to uppercase
    seq = seq.upper()

    # Validate nucleotide sequence
    if re.fullmatch(r"[ACGTU]+", seq):

        has_t = "T" in seq
        has_u = "U" in seq

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
        motif = args.motif.upper()
        print(
            f'Motif search enabled: looking for motif "{motif}" in sequence "{seq}"... ',
            end=""
        )
        if re.search(re.escape(motif), seq):
            print("FOUND")
        else:
            print("NOT FOUND")


if __name__ == "__main__":
    main()

