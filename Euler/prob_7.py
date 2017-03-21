l = []
# for p in xrange(2, 1000000):
#     for i in xrange(2, p):
#         if p % i == 0:
#             break
#     else:
#     	l.append(p)
#         # print p

# print(l[10001])
# sum_ = 0

import math
for num in xrange(2,100):
	if all(num%i!=0 for i in xrange(2,int(math.sqrt(num))+1)):
       # print num
		l.append(num)
		# sum_ = sum_ + num

print(l)
# print (sum_)