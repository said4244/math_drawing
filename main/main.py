from canvas import Canvas
from shapes import Rectangle, Square


#User input with some Error handeling
while True:
  try:
    canvas_height = int(input("Enter the canvas height: "))
    if type(canvas_height) == int:
      break
  except ValueError:
    print('canvas height should be given in numbers.... ')

while True:
  try:
    canvas_width = int(input("Enter the canvas width: "))
    if type(canvas_width) == int:
      break
  except ValueError:
    print('canvas width should be given in numbers.... ')

colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input('Enter the canvas color (black / white): ')
while True:
  if canvas_color.lower() == 'black':
    canvas_color = 'black'
    break
  elif canvas_color.lower() == 'white':
    canvas_color = 'white'
    break
  else:
    print('canvas color can only be white or black...')
    canvas_color = input('Enter the canvas color (black / white): ')

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
  shape_type = input('what do you want to draw? (rectangle / square) Or enter quit to quit: ')

  if shape_type.lower() == 'rectangle':
    while True:
      try:
        rec_y = int(input("Enter the x of the rectangle: "))
        if type(rec_y) == int:
          break
      except ValueError:
        print('x-coordinate should be given in numbers.... ') 
    
    while True:
      try:
        rec_x = int(input("Enter the y of the rectangle: "))
        if type(rec_x) == int:
          break
      except ValueError:
        print('y-coordinate should be given in numbers.... ')

    while True:
      try:
        rec_width = int(input("Enter the width of the rectangle: "))
        if type(rec_width) == int:
          break
      except ValueError:
        print('rectangle width should be given in numbers.... ')

    while True:
      try:
        rec_height = int(input("Enter the height of the rectangle: "))
        if type(rec_height) == int:
          break
      except ValueError:
        print('rectangle height should be given in numbers.... ')

    while True:
      try:
        red = int(input("how much red should the rectangle have(0 - 255)? "))
        if type(red) == int:
          if 0 <= red <= 255:
            break
          else:
            print("The number should be between 0 - 255....")
      except ValueError:
        print('red should be given in numbers between 0 - 255.... ')

    while True:
      try:
        green = int(input("how much green should the rectangle have(0 - 255)? "))
        if type(green) == int:
          if 0 <= green <= 255:
            break
          else:
            print("The number should be between 0 - 255....")
      except ValueError:
        print('green should be given in numbers between 0 - 255.... ')

    while True:
      try:
        blue = int(input("how much blue should the rectangle have(0 - 255)? "))
        if type(blue) == int:
          if 0 <= blue <= 255:
            break
          else:
            print("The number should be between 0 - 255....")
      except ValueError:
        print('blue should be given in numbers between 0 - 255.... ')

    
    rectangle1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
    rectangle1.draw(canvas)
    
  elif shape_type.lower() == 'square':

    while True:
      try:
        squ_y = int(input("Enter the x of the square: "))
        if type(squ_y) == int:
          break
      except ValueError:
        print('x-coordinate should be given in numbers.... ')

    while True:
      try:
        squ_x = int(input("Enter the y of the square: "))
        if type(squ_x) == int:
          break
      except ValueError:
        print('y-coordinate should be given in numbers.... ')

    while True:
      try:
        squ_side = int(input("Enter the side of the rectangle: "))
        if type(squ_side) == int:
          break
      except ValueError:
        print('square side should be given in numbers.... ')



    while True:
      try:
        red1 = int(input("how much red should the rectangle have(0 - 255)? "))
        if type(red1) == int:
          if 0 <= red1 <= 255:
            break
          else:
            print("The number should be between 0 - 255....")
      except ValueError:
        print('red should be given in numbers between 0 - 255.... ')

    while True:
      try:
        green1 = int(input("how much green should the rectangle have(0 - 255)? "))
        if type(green1) == int:
          if 0 <= green1 <= 255:
            break
          else:
            print("The number should be between 0 - 255....")
      except ValueError:
        print('green should be given in numbers between 0 - 255.... ')

    while True:
      try:
        blue1 = int(input("how much blue should the rectangle have(0 - 255)? "))
        if type(blue1) == int:
          if 0 <= blue1 <= 255:
            break
          else:
            print("The number should be between 0 - 255....")
      except ValueError:
        print('blue should be given in numbers between 0 - 255.... ')

    square1 = Square(x=squ_x, y=squ_y, side=squ_side, color=(red1, green1, blue1))
    square1.draw(canvas)
  elif shape_type.lower() == 'quit':
    canvas.make('newcanvas(1).png')
    break
