import numpy as np
from PIL import Image #from pillow import Image

class Canvas:
  def __init__(self, height, width, color):
    self.height = height
    self.width = width
    self.color = color

    #create the 3d numpy arrays of zeros
    self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8) 
    self.data[:] = self.color #changing the zero into new color
  def make(self, imagepath):
    img = Image.fromarray(self.data, 'RGB')
    img.save(imagepath)

