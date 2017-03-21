sqaures = []
numbers = []
for i in xrange(1,101):
	numbers.append(i)
	sqaures.append(i*i)
print numbers
print sqaures
sum_ = 0
sum_of_squares = 0
for i in xrange(0,100):
	sum_of_squares = sum_of_squares + sqaures[i]
	sum_ = sum_ + numbers[i]

square_of_sum = sum_ * sum_
print (square_of_sum - sum_of_squares)