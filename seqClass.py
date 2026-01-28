#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:          # to check if the script was run without any arguments
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 # to convert the input string to uppercase
if re.search('^[ACGTU]+$', args.seq):         check if the seq contains ony the A,C,G,T or U
    if re.search('T', args.seq):
        print ('The sequence is DNA')            # if seq is valid and it has T it's DNA, if contains U it's RNA
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

if args.motif:                                        #this is to search for a specific motif
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")



