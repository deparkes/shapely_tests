# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:11:08 2015

@author: Duncan

Convert GDS Boundary type format into a shapely LinearRing

GDS Boundaries are of the format XY: x1,y1, ..., xn, yn
they must be explicitly closed

Shapely LinearRing objects are an ordered sequence of (x,y) tuples 
e.g. ring = LinearRing([(0, 0), (1, 1), (1, 0)])

In this script I'll assume you've already extracted the list of x,y values from
the gds file.

To convert from gds to LinearRing we'll need to go from a single list to a 
list of tuples.

The answers to this question allow us to pick out the coordinate pairs from
the gds boundary list:
http://stackoverflow.com/questions/4628290/pairs-from-single-list

Although not strictly necessary, we'll also plot the resulting LinearRing
to check that everything is as expected. Plotting functions taken from 
LinearRing.py shapely example.

"""

from itertools import izip
from matplotlib import pyplot as plt
from shapely.geometry import LinearRing

# Gds coordinate extraction functions
def pairwise(t):
    it = iter(t)
    return izip(it,it)

# Plotting functions taken from shapely example LinearRing.py
COLOR = {
    True:  '#6699cc',
    False: '#ff3333'
    }

def v_color(ob):
    return COLOR[ob.is_valid]

def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=v_color(ob), alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)

# Use a test gds boundary
# Assume this has been extracted from a gds file
gds_test = (0, 0, 30000, 0, 15000, 15000, 5000, 15000, 0, 0)

# Extract the coordinates pairwise from the gds boundary
ring = list(pairwise(gds_test))

# Need to convert out list into a ring for the plotting function to work
ring = LinearRing(ring)

# We don't have to plot LinearRing, but it is a handy way to check it works
fig = plt.figure(1, figsize=(10,10), dpi=90)
ax = fig.add_subplot(111)
plot_line(ax, ring)


