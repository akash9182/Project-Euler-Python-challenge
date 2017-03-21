from re import *
from string import *
data = open('/media/akash/A00CA4B10CA4843E/Users/Akash/Desktop/data2.txt','r').read()
pattern = "[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"
result = findall(pattern,data)
print str(result)
s = ''