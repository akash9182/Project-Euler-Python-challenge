l = []
for i in range(1000):
	for j in range(1000):
		prod = str(i*j)
		reverse = prod [::-1]
		if (prod == reverse):
			l.append(int(prod))

# print l
# for i in range(len(l)):
# 	a = l[i-1]
# 	b = l[i]
# 	if a > b:
# 		b = a

print (len(l))
print (max(l))