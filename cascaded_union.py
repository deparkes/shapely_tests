# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:17:48 2015

@author: Duncan

How to merge two polygons in python
"""
from matplotlib import pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import Polygon, LinearRing
from shapely.ops import cascaded_union

from figures import SIZE, BLUE




# define the two polygons to merge
polygon1 = Polygon([(0, 0), (10, 3), (5, 0)])
polygon2 = Polygon([(0, 0), (3, 7), (3, 0)])
polygons = [polygon1, polygon2]


# plot these two polygons separately
fig = plt.figure(1, figsize=(10,10), dpi=90)
ax = fig.add_subplot(111)
poly1patch = PolygonPatch(polygon1, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
poly2patch = PolygonPatch(polygon2, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(poly1patch)
ax.add_patch(poly2patch)
xrange = [-2, 12]
yrange = [-2, 8]
ax.set_xlim(*xrange)
ax.set_xticks(range(*xrange) + [xrange[-1]])
ax.set_ylim(*yrange)
ax.set_yticks(range(*yrange) + [yrange[-1]])
ax.set_aspect(1)

#my_ring = LinearRing(u.exterior.coords)
#print(my_ring.is_ccw)

# Make the merged polygons
u = cascaded_union(polygons)

# Make new figure for the merged polygon
fig2 = plt.figure(2, figsize=(10,10), dpi=90)
ax2 = fig2.add_subplot(111)
patch2b = PolygonPatch(u, fc=BLUE, ec=BLUE, alpha=1, zorder=2)
ax2.add_patch(patch2b)

xrange = [-2, 12]
yrange = [-2, 8]
ax2.set_xlim(*xrange)
ax2.set_xticks(range(*xrange) + [xrange[-1]])
ax2.set_ylim(*yrange)
ax2.set_yticks(range(*yrange) + [yrange[-1]])
ax2.set_aspect(1)

fig2.show(2)