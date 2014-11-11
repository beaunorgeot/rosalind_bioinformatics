from sys import argv
from os.path import exists

script, from_file = argv

in_file = open(from_file)
dna = in_file.read().upper()

rna = dna.replace("T", "U")
print rna