def fibo(n):
	a = 0
	b = 1
	sum = 0
	sum2 = 0
	while ( sum < n ):
		sum = b + a
		if (sum < n and sum % 2 == 0):
			sum2 = sum2 + sum
		a = b
		b = sum
		# print sum
	print sum2

fibo(4000000)
