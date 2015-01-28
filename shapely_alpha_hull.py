# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:03:09 2015

@author: Duncan
"""

import math
import json
import numpy as np
from scipy.spatial import Delaunay
from descartes import PolygonPatch
from shapely.geometry import MultiLineString
from shapely.ops import cascaded_union, polygonize


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


