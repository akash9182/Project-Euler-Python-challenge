# import urllib2

# response = urllib2.urlopen('https://projecteuler.net/progress')
# html = response.read()

# print(html)
# with open("euler_page.txt") as f:
# 	file = f.readline()
	# count = 0

count = 0

with open('euler_page.txt')as f:
	text = f.read()
	print(len(text))
	
	count = text.find("members", beg=0 , end=len(text))
		# for word in line:

print(count)