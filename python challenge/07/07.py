import Image

s = Image.open('oxygen.png')

y = 48
for x in range(0, 607, 7):
	print chr(s.getpixel((x,y))[1]),

a = [ 105 ,   110 ,   116 ,   101 ,   103 ,   114 ,   105 ,   116 ,   121 ]

for element in a:
	print chr(element),
