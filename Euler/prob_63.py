import math

s = 0
for i in xrange(1,10):
	s += int(1/ (1- math.log10(i)))

print s