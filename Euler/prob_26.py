from prob_10 import prime_sieve 

# L = 1000
# s = prime_sieve(L)
# for d in xrange(len(s)):
# 	if s[d] == 1:
# 		print d

prime_sieve_1 = []
for x in xrange(0,1000):
	prime_sieve_1.append(x)

# print prime_sieve_1
# print prime_sieve_1(L)
for d in prime_sieve_1[2::-1]:
    period = 1
    while pow(10, period)-1 % d != 1:
        period += 1
    if d-1 == period: break
 
print "longest recurring cycle for 1/d, d =", d
