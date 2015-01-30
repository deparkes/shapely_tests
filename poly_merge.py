# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 18:48:38 2015

@author: Duncan
"""

from matplotlib import pyplot
from shapely.geometry import Point
from shapely.ops import cascaded_union
from descartes import PolygonPatch
from shapely.geometry import Polygon, LineString

from figures import SIZE, BLUE, GRAY

coords = [(0, 0), (0, 5), (5,5), (0,0)]
coords2 = [(-2.5, 2.5), (2.5, 7.5), (7.5,2.5), (-2.5,2.5)] 
#Create polygon from lists of points
polygon = Polygon(coords)
polygon2 = Polygon(coords2)
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





u = cascaded_union(polygons)
patch2b = PolygonPatch(u, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(patch2b)

ax.set_title('b) union')

xrange = [-2, 6]
yrange = [-2, 2]
ax.set_xlim(*xrange)
ax.set_xticks(range(*xrange) + [xrange[-1]])
ax.set_ylim(*yrange)
ax.set_yticks(range(*yrange) + [yrange[-1]])
ax.set_aspect(1)

pyplot.show()

