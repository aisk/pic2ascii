# -*- encode:utf8 -*-
# Author:aisk

import Image

class config():
	HEIGHT = 80
	PIC = 'ka.jpg'
	DEBUG = False
	chars = "   ...',;:clodxkO0KXNWMMM"

def pic2ascii():
	'''Gen the ascii
	'''
	output = ''
	image = Image.open(config.PIC)
	size = getsize(image)
	image = image.resize(size)
	image = image.convert('L')
	pixs = image.load()
	for y in range(size[1]):
		for x in range(size[0]):
			#print config.chars[pixs[x,y]/10],
			output += config.chars[pixs[x,y]/10]
		#print
		output += '\n'
	#image.show()
	print output

def getsize(image):
	'''Calculate the target picture size
	'''
	s_width = image.size[0]
	s_height = image.size[1]
	t_height = config.HEIGHT
	t_width = (t_height*s_width)/s_height
	t_width = int(t_width * 2.3)
	t_size = (t_width ,t_height)
	if config.DEBUG == True:
		print t_size
	return t_size

if __name__ == '__main__':
	pic2ascii()
