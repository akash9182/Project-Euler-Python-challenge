import math
import itertools

def prime_sieve(limit):
    # Mark everything prime in start
    primes = [1 for x in xrange(limit)]
    primes[0] = 0
    primes[1] = 0

    # Only need to sieve up to sqrt(limit)
    imax = int(math.sqrt(limit) + 1)

    i = 2
    while (i < imax):
        j = i + i
        while j < limit:
            primes[j] = 0
            j += i

        # Move i to next prime
        while True:
           i += 1
           if primes[i] == 1:
               break

    return primes

def is_prime(a):
    if all(a % i for i in xrange(2, a)):
        return True
    else :
        return False

def rotate(l,n):
    return l[n:] + l[:n]

s = prime_sieve(10000000)
count = 0
for i in xrange(100000):
    l = [] 
    prime = []
    if s[i] == 1:
        # print i
        while i > 0:
            l.append(str(i % 10))
            i = i / 10
        # prime = list(set(itertools.permutations(l)))
        # print l
        # print len(l)
        for j in xrange(len(l)):
            prime.append(rotate(l,j)) 

        # print prime
        # print len(prime)
        num_of_iterations = len(prime)
        count_ = 0
        for i in xrange(len(prime)):
            num = int("".join(prime[i]))
            if is_prime(num) == False:
                break
            else:
                count_ +=1
        if num_of_iterations == count_ :
            count += 1

print count