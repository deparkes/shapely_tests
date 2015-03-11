# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:51:08 2015

@author: Duncan

A simplified version of linearring.py, one of the shapely examples
"""

from matplotlib import pyplot
from shapely.geometry.polygon import LinearRing, Polygon

fig = pyplot.figure(1, figsize=(5,5), dpi=90)

# 1: valid ring
ax = fig.add_subplot(111)
#poly = Polygon([(0, 0), (0, 2), (1, 1), 
#                (2, 2), (2, 0), (1, 0.8), (0, 0)])
#x,y = poly.exterior.xy

ring = LinearRing([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (1, 0.8), (0, 0)])
x, y = ring.xy
ax.plot(x, y, color='#6699cc', alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)

ax.set_title('Polygon')

xrange = [-1, 3]
yrange = [-1, 3]
ax.set_xlim(*xrange)
ax.set_xticks(range(*xrange) + [xrange[-1]])
ax.set_ylim(*yrange)
ax.set_yticks(range(*yrange) + [yrange[-1]])
ax.set_aspect(1)

pyplot.show()

