# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 18:48:38 2015

@author: Duncan
"""

from shapely.geometry import Polygon

coords = [(0, 0), (10, 10), (1, 0), (0,0)]
#Create polygon from lists of points
polygon = Polygon(coords)
#print(list(polygon.exterior.coords))

# Print coords
for pair in range(len(coords)):
    print "x = "+str(coords[pair][0])+", y = "+str(coords[pair][0])
    
