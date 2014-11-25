import numpy as np

n = int(raw_input("What number would you like to find the factorial of Dr. Einstein? > "))

facList = []
for value in xrange(1, n+1):
	facList.append(value)

answer = np.product(facList)
print "The answer you're looking for is %d" %(answer)
