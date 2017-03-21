count = 0
terms = {}

for i in xrange(2,101):
	for j in xrange(2,101):
		a = pow(i,j)
		if terms.has_key(a):
			pass
		else:
			terms[a] = 1
			count += 1 	 
# gives count as 9801
 	 

# for i in xrange(2,101):
# 	for j in xrange(2,101):
# 		a = pow(i,j)
# 		if terms.get(a) != 0:
# 			terms[a] = 1
# 			count += 1

#gives count as 9801

# for i in xrange(2,101):
# 	for j in xrange(2,101):
# 		a = pow(i,j)
# 		if not terms.get(a):
# 			terms[a] = 1
# 			count += 1

print count
# print terms