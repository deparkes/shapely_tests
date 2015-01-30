# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 18:48:38 2015

@author: Duncan
"""

from shapely.geometry import Polygon, LineString
from matplotlib import pyplot
coords = [(0, 0), (10, 10), (0,5), (0,0)]
#Create polygon from lists of points
polygon = Polygon(coords)
#print(list(polygon.exterior.coords))

# Print coords
for pair in range(len(coords)):
    print "x = "+str(coords[pair][0])+", y = "+str(coords[pair][0])

for x,y in polygon.exterior.coords:
    print "x = " + str(x)  + ", y = "+str(y)

startx = -2.0
starty = 5.0

endx = startx+0.1
endy = starty+0.1
path = LineString([(startx,starty), (endx,endy)])


new_coords = list()
for extray in range(0,10):
    print float(extray)/10
    while not path.intersects(polygon):
        path = LineString([(startx,starty+(float(extray)/10)), (endx,endy)])
        endx = endx + 0.1
        
#        print endx
#        print(path.intersects(polygon))
    if path.intersects(polygon): 
        new_coords.append((endx,endy))
            
print(new_coords)
pyplot.plot(new_coords)