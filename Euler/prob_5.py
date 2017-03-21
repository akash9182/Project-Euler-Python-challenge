check_list = [11, 13, 14, 16, 17, 18, 19, 20]
for i in xrange(2000,1000000000,20):
	u = 0
	for j in check_list:
		if i % j != 0:
			u = 1
	if u == 0:	
		print i 
		break
