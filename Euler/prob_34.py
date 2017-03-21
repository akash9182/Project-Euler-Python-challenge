# fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
# 10
# 11 def sum_of_digits_factorial(n):
# 12     s = 0
# 13     while n > 0:
# 14         d = n % 10
# 15         s = s + fact[d]
# 16         n = n / 10
# 17     return s
# 18
# 19 print sum(n for n in xrange(10, 100000) if n == sum_of_digits_factorial(n))

fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)

# def fact(num):
# 	n = 1
# 	for i in xrange(1,num+1) : n = n*i

# 	return (n)

# print fact (5)

def sum_of_factorials(num):
	sum_ = 0
	while num > 0:
		a = num % 10
		sum_ = sum_ + fact[a]
		num = num/10
	return sum_

l = []
for i in xrange(10, 1000000):
	if i == sum_of_factorials(i):
		l.append(i)

print (sum(l))
