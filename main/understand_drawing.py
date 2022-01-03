import numpy as np
from PIL import Image
#for better understanding of drawing shapes

# first we'll create 3d numpy array of zero's (black canvas) 
# we're using RGB that's way the arrays should be 3d 
#red #red #red
#green #green #green  #This is one row
#blue #blue #green
#we're going to need 3 of the above under each others to make one column.


data = np.zeros((5, 4, 3), dtype=np.uint8) #10 rows, 7 columns, 3 depth
#    = np.zeros((horizontal, vertical, depth) changing type to int (0) instead of float(0.0))
# because we used np.ZEROS the code above represents = array([[[0,0,0], [0,0,0], [0,0,0]]]) in rgb 000 means simply black
#now lets change the color to yellow

data[:] = [255, 255, 0] #--> array([[[255,255,0], [255,255,0], [255,255,0]]]) 255 255 0 is yellow

#lets draw a rectangle in hte yellow canvas

#we are simply modifying parts of the canvas and that why we use the variable of the canvas 'data'

data[0:3, 0:2] = [255, 0, 0] #[1:9, 2:4] 1:9 will push the red rectangle 1 row to the bottom and make it 9 rows long 2:4 will push the rectangle 2 columns to the right and make it 4 columns long


#now lets make the image

img = Image.fromarray(data, 'RGB')



img.save("test.png") #with this line we'll save the image 