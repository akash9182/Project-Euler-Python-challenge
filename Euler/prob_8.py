with open("numbers.txt") as f:
	line = f.readlines()
	new_line = ''.join(line)
	new_line = new_line.replace("\n", "")
# print(new_line)

largest_product = 0

for i in range(0, len(new_line) - 13):

    product = 1

    for j in range(i, i + 13):
        product *= int(new_line[j])
    
    if product > largest_product:
        largest_product = product

print (largest_product)    
