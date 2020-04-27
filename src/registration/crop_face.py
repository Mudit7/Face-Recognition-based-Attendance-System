

# Improting Image class from PIL module 
from PIL import Image 
  

# Opens a image in RGB mode 
  
import os
for filename in os.listdir('Working'):
	im = Image.open(r"Working/"+filename) 
	# Size of the image in pixels (size of orginal image) 
	# (This is not mandatory) 
	width, height = im.size 
	  
	# Setting the points for cropped image 
	left = 47
	top = height / 4 + 50
	right = 198
	bottom = 3 * height / 4 - 3

	# Setting the points for cropped image 
	#left = 155
	#top = 65
	#right = 360
	#bottom = 270
	  
	# Cropped image of above dimension 
	# (It will not change orginal image) 
	im1 = im.crop((left, top, right, bottom)) 
	  
	# Shows the image in image viewer 
	#im1.show() 
	im1.save('Faces/'+filename)

