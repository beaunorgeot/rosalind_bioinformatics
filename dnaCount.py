from sys import argv
from os.path import exists

script, from_file = argv

dna = open(from_file)
dnaString= dna.read()
print "The input file is %d long" %(len(dnaString))

a = []
c = []
g = []
t = []
weirdShit = []

for item in dnaString.upper():
	if item == 'A':
		a.append(item)
	elif item == 'C':
		c.append(item)
	elif item == 'G':
		g.append(item)
	elif item == 'T':
		t.append(item)
	else:
		weirdShit.append(item)


print len(a),len(c), len(g), len(t)



