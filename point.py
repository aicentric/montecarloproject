
import math
class Point:
    def __init__(self, a, b):
        
        self.a = a
        self.b = b
        
   # calclualting distance of the point
    def distance(self):
        dist=math.sqrt(self.a**2 + self.b**2)
        return dist
        
