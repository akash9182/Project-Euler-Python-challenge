final_value = 200

sum_of_coins = 0

count = 0

coins = (1,2,5,10,20,50,100,200)

for i_200p in xrange(0,2):
	sum_of_coins_200p = (i_200p * 200)
	# print sum_of_coins 
	for i_100p in xrange(0,3):
		sum_of_coins_100p = (i_100p * 100) 
		for i_50p in xrange(0,5):
			sum_of_coins_50p = (i_50p * 50) 
			for i_2op in xrange(0,11):
				sum_of_coins_20p = (i_2op * 20)
				for i_10p in xrange(0,21):
					sum_of_coins_10p = (i_10p * 10)
					for i_5p in xrange(0,41):
						sum_of_coins_5p = (i_5p  * 5)
						for i_2p in xrange(0,101):
							sum_of_coins_2p = (i_2p * 2)
							for i_1p in xrange(0,201):
								sum_of_coins_1p = (i_1p * 1)
								
								sum_of_coins = sum_of_coins_1p + sum_of_coins_2p + sum_of_coins_5p + sum_of_coins_10p + sum_of_coins_20p + sum_of_coins_50p + sum_of_coins_100p + sum_of_coins_200p  

								if sum_of_coins == final_value:
									count += 1


print count

# for x in xrange(0,2):
# 	print x