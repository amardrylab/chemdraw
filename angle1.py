import numpy as np

p0 = [3.5, 6.7]
p1 = [7.9, 8.4]
p2 = [10.8, 4.8]

''' 
compute angle (in degrees) for p0p1p2 corner
Inputs:
    p0,p1,p2 - points in the form of [x,y]
'''

v0 = np.array(p0) - np.array(p1)
v1 = np.array(p2) - np.array(p1)

angle = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))
print(np.degrees(angle))
