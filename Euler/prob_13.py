with open("13.txt") as f:
	line = f.readlines()
	# new_line = ''.join(line)
	# new_line = new_line.replace("\n", "")
	# print (len(line))
	# print (line)
# print(new_line)
	sum_ = 0	
	for each_number in line :
		sum_ += int(each_number)
	
	sum_ = str(sum_)
	j = 1
	the_digit = ''
	for i in sum_:
		if j <= 10 :
			the_digit = the_digit + i
			j += 1

print (sum_)
print (the_digit)