import math
l = []
sum_ = 0
largest = []
for num in xrange(2,1000):
	if all(num%i!=0 for i in xrange(2,int(math.sqrt(num))+1)):
		l.append(num)

def check_if_prime (num):
	if all(num%i!=0 for i in xrange(2,int(math.sqrt(num))+1)):
		if num < 1000:
			print num

for num in sum_ :
	sum_ = num + sum_
	# print(sum_)
	check_if_prime(sum_)



# check_if_prime(953)
# print (l)