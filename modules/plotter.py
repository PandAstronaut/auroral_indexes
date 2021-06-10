# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:58:50 2021
@author: Bastien Longeon

This code plots the magnetogram of one magdata column.
It was created to facilitate plotting of graphics.
"""
import matplotlib.pyplot as plt
import modules.global_graph as gb

plot_color = [
        '#000000',   # 0: black
        '#cc66cc',   # 1: red-purple
        '#0000cc',   # 2: blue
        '#00ccff',   # 3: light blue
        '#9a32cd',   # 4: Dark Orchid 3
        '#ff0000',   # 5: red
        '#ff9900',   # 6: orange
        '#330000',   # 7: dark brown
        '#339900',   # 8: green
        '#a74fff',   # 9: purple
        '#f6a400',   # 10: yellow
        '#cd1076']   # 11: Deep Pink 3

markers = ['o', '+', 'x', 'X', 'D', '>', '<', '^', 'v' '.', 'v']

# In the magdata used, it's important to have a vector 'hour' for this code to work
def plot_1D(magdata, column, title, xlab, ylab, position='lower left'):
    plt.figure(dpi=600)
    plt.plot(magdata['hour'], magdata[column], linewidth=.4, color=plot_color[gb.color%12],
    linestyle='-', label=column)
    plt.title(title, fontsize=14)
    plt.grid(b=True)
    plt.legend(loc=position, fontsize= 8)
    if xlab == 'Time in hours': plt.xlim([0, 24])
    plt.xlabel(xlab, fontsize=12)
    plt.ylabel(ylab, fontsize=12)
    plt.show()   # This is to display the plot
    gb.color += 1


def plot_2D(magdata, horizontal1, vertical1, horizontal2, vertical2, title,
            xlab, ylab, position='lower left', mark = False):
    plt.figure(dpi=600)
    plt.plot(magdata[horizontal1], magdata[vertical1], linewidth=.4, color=plot_color[gb.color%12],
    linestyle='-', label=vertical1)
    if mark: marker_plot(magdata, horizontal1, vertical1)
    gb.color += 1
    plt.plot(magdata[horizontal2], magdata[vertical2], linewidth=.4, color=plot_color[gb.color%12],
    linestyle='-', label=vertical2)
    if mark: marker_plot(magdata, horizontal2, vertical2)
    gb.color += 1
    plt.title(title, fontsize=14)
    plt.grid(b=True)
    if xlab == 'Time in hours': plt.xlim([0, 24])
    plt.legend(loc=position, fontsize= 8)
    plt.xlabel(xlab, fontsize=12)
    plt.ylabel(ylab, fontsize=12)
    plt.show()

def plot_3D(magdata, horizontal1, vertical1, horizontal2, vertical2, horizontal3,
            vertical3, title, xlab, ylab, position='lower left'):
    plt.figure(dpi=600)
    plt.plot(magdata[horizontal1], magdata[vertical1], linewidth=.4, color=plot_color[gb.color%12],
    linestyle='-', label=vertical1)
    gb.color += 1
    plt.plot(magdata[horizontal2], magdata[vertical2], linewidth=.4, color=plot_color[gb.color%12],
    linestyle='-', label=vertical2)
    gb.color += 1
    plt.plot(magdata[horizontal3], magdata[vertical3], linewidth=.4, color=plot_color[gb.color%12],
    linestyle='-', label=vertical3)
    gb.color += 1
    plt.title(title, fontsize=14)
    plt.grid(b=True)
    if xlab == 'Time in hours': plt.xlim([0, 24])
    plt.legend(loc=position, fontsize= 8)
    plt.xlabel(xlab, fontsize=12)
    plt.ylabel(ylab, fontsize=12)
    plt.show()

def marker_plot(magdata, horizontal, vertical):
    x_axis = list()
    y_marker = list()
    for i in range(60,1440,60):
        x_axis.append(magdata[horizontal].iloc[i])
        y_marker.append(magdata[vertical].iloc[i])
    plt.plot(x_axis, y_marker, marker = 'o', markersize = 2,
             linestyle = 'None', markerfacecolor = plot_color[gb.color%12],
             markeredgecolor = plot_color[gb.color%12])
