import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt 

class Lane:
  
  def __init__(self, lines):
    """
    line 1: p1, p2
    line 2: p3, p4
    ...
      
      
    """ 
    x = []
    y = []
    for line in lines:
      assert line['type'] == 'line'
      x1 = line['left'] + line['x1']
      y1 = line['top'] + line['y1']
      x2 = line['left'] + line['x2']
      y2 = line['top'] + line['y2']
      x.append(x1)
      x.append(x2)
      y.append(y1)
      y.append(y2)
      
    x = np.array(x)
    y = np.array(y)
    
    self.lane = CubicSpline(x, y)
    return self.lane
  
  def get_lane(self):
    return self.lane()
  
    
    