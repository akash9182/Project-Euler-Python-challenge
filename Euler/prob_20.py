# # def digits(n):
# #      s = 0
# #      while n > 0:
# #          s = s + (n % 10)
# #          n = n / 10
# #      return s
def sum_of_fact (num):
	n = 1
	s = 0
	for i in xrange(1,num): n = n*i
	
	print (n) 
	while n > 0 :
		s = s + (n % 10)
		n = n / 10 

	return s

a = sum_of_fact(100)
print(a)