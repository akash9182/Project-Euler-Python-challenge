import pickle
# from urllib.request import urlopen
# import os

# working_directory_array = __file__.split('\\')[:-1]
# working_directory = ''
# for element in working_directory_array : 
# 	working_directory += element
# 	working_directory += '\\'
# os.chdir(working_directory)

# pickled_file = urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read().decode('utf-8')

# with open('pickled_file.p','w') as p : 
	# p.write(pickled_file)

x = pickle.load(open('pickled_file.p'))
# print x

for every_list in x:
	for every_item in every_list:
		for x in range(every_item[1]):
			print (every_item[0]),
	print ""

