# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:17:48 2015

@author: Duncan
"""
from matplotlib import pyplot
from descartes import PolygonPatch
from shapely.geometry import Polygon
from shapely.ops import cascaded_union

from figures import SIZE, BLUE, GRAY

fig = pyplot.figure(1, figsize=SIZE, dpi=90)
polygon1 = Polygon([(0, 0), (5, 3), (5, 0)])
polygon2 = Polygon([(0, 0), (3, 10), (3, 0)])
ax = fig.add_subplot(121)

polygons = [polygon1, polygon2]

u = cascaded_union(polygons)
patch2b = PolygonPatch(u, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(patch2b)

ax.set_title('b) union')

xrange = [-2, 6]
yrange = [-2, 12]
ax.set_xlim(*xrange)
ax.set_xticks(range(*xrange) + [xrange[-1]])
ax.set_ylim(*yrange)
ax.set_yticks(range(*yrange) + [yrange[-1]])
ax.set_aspect(1)

pyplot.show()

