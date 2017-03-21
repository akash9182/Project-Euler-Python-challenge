def prime(n):
	l = []
	for i in xrange(n):
		if (n % (i+1) == 0):
			l.append(i+1)
			trial = n/(i+1)
			if (len(l) > 5):
				break
			# if (type(trial) == int):
				# n = n / (i+1) 

	# print l
	return l

# def largest_prime(l):
# 	L = []
# 	for i in xrange(len(l)):
# 		if (len(prime(l[i])) == 2 ):
# 			L.append(l[i])
# 	print L


l = prime(600851475143)
print l
# largest_prime(l)


#----------------------------------------

# def prime_factors(n):
#     """Returns all the prime factors of a positive integer"""
#     factors = []
#     d = 2
#     while n > 1:
#         while n % d == 0:
#             factors.append(d)
#             n /= d
#         d = d + 1
#         if d*d > n:
#             if n > 1: factors.append(n)
#             break
#     return factors


# pfs = prime_factors(15469780)
# print max(pfs)