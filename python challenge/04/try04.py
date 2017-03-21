from urllib import *
page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')

f = open("test.txt", "w")
content = page.read()
f.write(content)
f.close()

print(content)