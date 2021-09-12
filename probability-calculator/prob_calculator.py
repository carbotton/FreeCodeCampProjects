import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for x in range(value):
        self.contents.append(key)

  
  def draw(self, num_balls):
    if num_balls > len(self.contents):
      return self.contents
    else:
      drawed_balls = []
      if self.contents:
        for x in range(num_balls):
          random_ball = random.choice(self.contents)
          self.contents.remove(random_ball)
          drawed_balls.append(random_ball)      
      return drawed_balls

#end class Hat

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #results = []
  m = 0
  #draw balls num_experiments times
  for x in range(num_experiments):  
    hat_copy = copy.deepcopy(hat) 
    expected_balls_copy = copy.deepcopy(expected_balls) 
    drawed_balls = hat_copy.draw(num_balls_drawn)
    for ball in drawed_balls:
      if (ball in expected_balls_copy):
        expected_balls_copy[ball] -= 1
    
    #check experiment
    if(all(x <= 0 for x in expected_balls_copy.values())):
      m += 1
  
  return m/num_experiments
