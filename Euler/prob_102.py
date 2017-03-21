def area(x0,y0, x1,y1, x2,y2):
	total_area = 0.5 * abs((x0 * y1 - x0 * y2 + x1 * y2 - x1 * y0 + x2 * y0 - x2 * y1))
	# print total_area 
	return total_area



# print (t1+t2+t3)
with open("p102_triangles.txt") as f:
    count = 0
    line = f.readline()
    while line :
		x0,y0, x1,y1, x2,y2 = line.split(",")
		T = area(int(x0),int(y0), int(x1),int(y1), int(x2),int(y2))
		t1 = area(int(x0),int(y0),int(x1),int(y1),0,0)
		t2 = area(int(x1),int(y1),int(x2),int(y2),0,0)
		t3 = area(int(x0),int(y0),int(x2), int(y2),0,0)
		sum_of_tri = t1 + t2 + t3

		if T == sum_of_tri:
			# print T
			# print sum_of_tri			
			count = count + 1
		line = f.readline()

print count