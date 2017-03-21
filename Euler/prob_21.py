def divisors (num):
	l = []
	for i in xrange(1, num/2 + 1):
		if num % i == 0:
			l.append(i)

	return (l)

# a = (divisors (220))
# print a
# print sum(a)

pair = dict( ((i, sum(divisors(i))) for i in xrange(1,10000)))

print sum(i for i in xrange(1,10000) if pair.get(pair[i], 0) == i and pair[i] != i)

# # print (pair.get(pair[220],0))
# # print (pair[7])

# for i in range(200,290,2):
# 	print (i, pair.get(pair[i]) ,pair[i])

# for i in range(1,300):
# 	da = sum(divisors(i))
# 	db = sum(divisors(da))
# 	if i == db :
# 		print da , db

# square = dict((i, i*i) for i in range(1,15))

# for i in range(1,15):
# 	print (i, square.get(square[i]) ,square[i])