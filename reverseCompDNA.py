from sys import argv
from os.path import exists
from string import maketrans

script, from_file, to_file = argv

indata = open(from_file)
dna = indata.read().upper()

print "The input file is %d long" %(len(dna))

reverse = dna[::-1]
revString = str(reverse)
print revString


intab = 'ATCG'
outtab ='TAGC'
trantab = maketrans(intab, outtab)

revComp = revString.translate(trantab)
print revComp

out_file = open(to_file, 'w')
out_file.write(revComp)

indata.close()
out_file.close()
