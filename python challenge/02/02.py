from urllib import *
page = urlopen("view-source:http://www.pythonchallenge.com/pc/def/ocr.html")
contents = page.read()
page.close()
print contents
