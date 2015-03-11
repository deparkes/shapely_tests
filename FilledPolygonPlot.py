# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:51:08 2015

@author: Duncan

A simplified version of linearring.py, one of the shapely examples
"""

from matplotlib import pyplot as plt
from shapely.geometry.polygon import Polygon
from descartes import PolygonPatch

fig = plt.figure(1, figsize=(5,5), dpi=90)
ring_mixed = Polygon([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (1, 0.8), (0, 0)])
ax = fig.add_subplot(111)
ring_patch = PolygonPatch(ring_mixed)
ax.add_patch(ring_patch)

ax.set_title('Filled Polygon')
xrange = [-1, 3]
yrange = [-1, 3]
ax.set_xlim(*xrange)
ax.set_xticks(range(*xrange) + [xrange[-1]])
ax.set_ylim(*yrange)
ax.set_yticks(range(*yrange) + [yrange[-1]])
ax.set_aspect(1)

