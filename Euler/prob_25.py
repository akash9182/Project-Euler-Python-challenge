def fibo (num):
	series = [1, 1]
	for i in xrange(2,int(num)):
		fn = series[i-1] + series [i-2]
		series.append(fn) 
		count = 0
		for j in str(series[i]) :
			# print j 
			count += 1
		if count == 1000:
			print (i+1)
			break

fibo(10000)