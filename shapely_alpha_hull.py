# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:03:09 2015

@author: Duncan
"""

import math
import numpy as np
from scipy.spatial import Delaunay
from descartes import PolygonPatch
from shapely.geometry import MultiLineString, LinearRing
from shapely.ops import cascaded_union, polygonize
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from figures import SIZE, BLUE, GRAY

def add_edge(i, j):
    """Add a line between the i-th and j-th points, if not in the list already"""
    if (i, j) in edges or (j, i) in edges:
        # already added
        return
    edges.add( (i, j) )
    edge_points.append(points[ [i, j] ])

# JSON data from the gist above.
points = np.random.rand(30, 2) # 30 points in 2-d
tri = Delaunay(np.array(points))

edges = set()
edge_points = []
alpha = 3

# loop over triangles:
# ia, ib, ic = indices of corner points of the triangle
for ia, ib, ic in tri.vertices:
    pa = points[ia]
    pb = points[ib]
    pc = points[ic]

    # Lengths of sides of triangle
    a = math.sqrt((pa[0]-pb[0])**2 + (pa[1]-pb[1])**2)
    b = math.sqrt((pb[0]-pc[0])**2 + (pb[1]-pc[1])**2)
    c = math.sqrt((pc[0]-pa[0])**2 + (pc[1]-pa[1])**2)

    # Semiperimeter of triangle
    s = (a + b + c)/2.0

    # Area of triangle by Heron's formula
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    circum_r = a*b*c/(4.0*area)

    # Here's the radius filter.
    if circum_r < 1.0/alpha:
        add_edge(ia, ib)
        add_edge(ib, ic)
        add_edge(ic, ia)

lines = LineCollection(edge_points)
ring = LinearRing(list(edges))

plt.figure()
plt.title('Alpha=2.0 Delaunay triangulation')
plt.gca().add_collection(lines)
plt.plot(points[:,0], points[:,1], 'o', hold=1)

m = MultiLineString(edge_points)
triangles = list(polygonize(m))

plt.figure()
plt.title("Alpha=2.0 Hull")
plt.gca().add_patch(PolygonPatch(cascaded_union(triangles), alpha=0.5))
plt.gca().autoscale(tight=False)
plt.plot(points[:,0], points[:,1], 'o', hold=1)
plt.show()


COLOR = {
    True:  '#6699cc',
    False: '#ff3333'
    }

def v_color(ob):
    return COLOR[ob.is_valid]

def plot_coords(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, 'o', color='#999999', zorder=1)

def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=v_color(ob), alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)

fig = plt.figure(1, figsize=SIZE, dpi=90)

# 1: valid ring
ax = fig.add_subplot(121)


plot_coords(ax, ring)
plot_line(ax, ring)

ax.set_title('a) valid')

xrange = [-5, 20]
yrange = [-5, 20]
ax.set_xlim(*xrange)
ax.set_xticks(range(*xrange) + [xrange[-1]])
ax.set_ylim(*yrange)
ax.set_yticks(range(*yrange) + [yrange[-1]])
ax.set_aspect(1)


plt.show()
