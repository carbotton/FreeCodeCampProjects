class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height
  #

  def __str__(self):
    return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
  #

  def set_width(self, width):
    self.width = width
  #

  def set_height(self, height):
    self.height = height
  #

  def get_area(self):
    return self.width*self.height
  #

  def get_perimeter(self):
    return 2*(self.width+self.height)
  #

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5   # 2 to the power of 7 = 2 ** 7
  #

  def get_picture(self):
    shape = ""
    if self.width > 50 or self.height > 50:
      shape = "Too big for picture."
    else:
      shape = ""
      for i in range(0, self.height):
        for j in range(0, self.width):
          shape += '*'
        #endfor
        shape += "\n"
      #endfor
    #endelse
    return shape
  #

  def get_amount_inside(self, shape):
    w = self.width // shape.width #Quotient when a is divided by b, rounded to the next smallest whole number
    h = self.height // shape.height
    return w*h  
  #
#
#end class Rectangle


class Square (Rectangle):

  def __init__(self, side):
    Rectangle.__init__(self, side, side)
  #

  def __str__(self):
    return "Square(side="+str(self.width)+")"
  #

  def set_side(self, side):
     Rectangle.set_width(self, side)
     Rectangle.set_height(self, side)
  #

  def set_width(self, width):
    Rectangle.set_width(self, width)
    Rectangle.set_height(self, width)
  #

  def set_height(self, height):
    Rectangle.set_width(self, height)
    Rectangle.set_height(self, height)
  #
#
#end class Square
