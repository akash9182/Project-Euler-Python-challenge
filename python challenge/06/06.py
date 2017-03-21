# import os
import zipfile
# working_directory_array = __file__.split('\\')[:-1]
# working_directory = working_directory.remove[:-1]
# working_directory = ''
# for element in working_directory_array : 
# 	working_directory += element
# 	working_directory += '\\'
# working_directory = working_directory.remove[:-1]
# working_directory +='\\zipped_contents' 
# os.chdir(working_directory)

the_zip = zipfile.ZipFile("channel.zip")
comments = []
def next_nothing (file_name):
	with open( file_name ,'rb') as f:
		content = f.read()
		# print content
		next_number = content.split(' ')[-1]
		# print (next_number) 
	if (next_number != 'comments.'):
		next_nothing(next_number + '.txt')
		comments.append(the_zip.getinfo( next_number + ".txt").comment)

next_nothing('90052.txt')
for comment in comments:
	print (comment),

# with open( "46145.txt" ,'rb') as f:
# 	content = f.read()
# 	print content