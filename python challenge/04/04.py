from urllib import *
from string import *
from re import *
b = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=55565')
s =  b.read()
print(s)
a = s.split(' ')[-1]
print(a)
# # a = a.split('=','http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=')[0]+ '=' +   
# b = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + a
# print b
i = 1
while (a.isdigit() or len(a) ==9):
	i = i+1
	print (i)
	b = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + a
	b = urlopen (b)
	s = b.read()
	print s
	a = s.split(' ')[-1]
	print a