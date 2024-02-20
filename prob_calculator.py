import copy
import random
# Consider using the modules imported above.


############
# Hat, Init
############
class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  
  ############
  # Draw Balls Method
  ############
  def draw (self, number):
    if number >= len(self.contents):
      return self.contents

    removed = []
    for _ in range(number):
      removed.append(self.contents.pop(random.randint(0, len(self.contents)-1)))

    return removed
    


############
# Computing Probability with Experiment
############
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  expect_output = []
  
  for _ in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors_gotten = hat_copy.draw(num_balls_drawn)

    for color in colors_gotten:
      if color in expected_copy:
        expected_copy[color] -= 1

        if expected_copy[color] == 0:
          expected_copy.pop(color)

      if len(expected_copy) == 0:
        count += 1
        break

  return count / num_experiments