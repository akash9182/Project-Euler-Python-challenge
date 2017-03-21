'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

for m in range(1,1000):
	for n in range(1,m):
		a = m*m - n*n
		b = 2*m*n
		c = m*m + n*n
		if ((a*a) + (b*b) == (c*c)):
			if (a + b + c == 1000):
				print (a, b, c)
				print(a*b*c)


# for n in range (1,1):
# 	print(n)