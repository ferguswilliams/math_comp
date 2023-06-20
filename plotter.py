#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:07:06 2023

@author: ferguswilliams
"""
from numpy import *
from matplotlib.pylab import *

def plotter(F,min,max,points):
    x=linspace(min,max,points)
    f=zeros(points)
    for i in range(points):
        f[i]=F(x[i])
    figure(figsize=(8,6))
    title('Graph of f as a function of x')
    xlabel('x')
    ylabel('dx/dt')
    #can add gridlines to make identification of roots easier
    plt.grid(True)
    plt.show()
    return plot(x,f)

