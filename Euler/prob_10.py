# sum_ = 0
# import math
# for num in xrange(1,2000000):
# 	if all(num%i!=0 for i in xrange(2,int(math.sqrt(num))+1)):
# 		sum_ = sum_ + num

# # print(l[10001])
# print (sum_)

import math

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

s = prime_sieve(10)
# print (s)
p = (sum(i for i in xrange(len(s)) if s[i] == 1))
print (p)

# print nth prime number

# def Prime(number):
#   l = []
#   for i in xrange(len(s)):
#     if (s[i] == 1):
#       l.append(i)

#   print(l[number])

# Prime(1)

