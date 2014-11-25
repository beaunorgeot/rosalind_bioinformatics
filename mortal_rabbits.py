#from sys import argv
#script, from_file, to_file = argv
from collections import defaultdict

# This program takes 3 input variables: n,k, m
# n is number of iterations or months, k is the number of breeding pairs produced by each breeding pair, m is how many months rabbits live for
# This is essentially a Fibanocci sequence, except with a multiplier of k and a modifier of m that subtracts breeding pairs after a certain amount of time
# so the default case, normal Fib is just k =1
#babies become adults (capable of breeding) after 1 month

n = int(raw_input("How many months will our rabbits be fucking? > " ))
k = int(raw_input("How many baby pairs will each breeding pair make per month? > "))
m = int(raw_input("How long, in months, will rabbits live for? > "))

#arabbits = adultRabbits, brabbits = babyRabbits. These dicts hold the month as the key, and the number of rabbits as the value
# all values are pairs; 1 doesn't mean 1 rabbit, it means 1 pair of rabbits
arabbits = {1:0,2:1,3:1} #changing initials to match prompt
brabbits = {1:1,2:0, 3:1} #The base case is essentially the case where brabbits never goes back to 0 which happens after month 2

def fibIter(n):
	for num in xrange(4, n+1): #pattern only cares about months were rabbits die. So start at m?
		oldNum = (num - 1) #oldNum is just the previous num, it's the dictKey for the month prior to the current iteration. The first month is just weird
		
		if num - m < 1:
			death = 2 # Changed to deal with immortal rabbits. when death = 2, brabbits[death]= 0 
		else:
			death = num - m
		arabbits[num] = arabbits[oldNum] + brabbits[oldNum] - brabbits[death]
		brabbits[num] = arabbits[oldNum] * k
		pairs = arabbits[num] + brabbits[num]
	print "There are %d pairs" %(pairs)
        
"""
Description of fibIter():
$death: If a rabbit lives for 3 months, and we're in the 4th month of the experiment, then the rabbits born in month 1 have died.
So, death = (month you're on) - (# months that rabbits live for)
$$ a/brabbits[death] gives you the # of rabbits that have died and need to be removed from the adult population

$$$ adult rabbits are found by starting with the number of adults last month, and adding the number of babies that were born last month, then subtracting the rabbits that have died
$$$ baby rabbits are found by multiplying the number of adult rabbits the previous month, by the number of babies that each pair has (k)
"""


fibIter(n)
# If you would like to hide the values for adult and baby rabbits after n-months, block the code below
print "The are %r adult rabbits" % (arabbits[n])
print "There are %r baby rabbits" %(brabbits[n])




