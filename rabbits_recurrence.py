#from sys import argv
#script, from_file, to_file = argv

# This program takes 2 input variables: n,k
# n is number of iterations or months, k is the number of breeding pairs produced by each breeding pair
# This is essentially a Fibanocci sequence, except with a multiplier of k
# so the default case, normal Fib is just k =1

n = int(raw_input("How many months will our rabbits be fucking? >" ))
k = int(raw_input("How many baby pairs will each breeding pair make per month? >"))


def fibIter(n):

    
    fibSuperPrev = 1 # The n-2 condition
    fibPrev = 1
    
    for num in xrange(3, n+1):
    	fib = k*fibSuperPrev + fibPrev
        
        print "num is %d" % num
        print "fibSuperPrev is %d" % fibSuperPrev
        print " fibPrev is %d" % fibPrev
        print "fib is %d" %fib
        print "I'm fucking up %d " % (3 * fibSuperPrev)
        fibSuperPrev,fibPrev = fibPrev, fib
    return fib

print fibIter(n)

#fibSuperPrev, fibPrev, fib = fibPrev, fib, fib + (3*fibSuperPrev)