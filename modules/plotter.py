# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:58:50 2021
@author: Bastien Longeon

This code plots 1, 2 and 3D plots with the color changing each time a graph has
been made. It takes data coming from pandas DataFrame.
"""
import matplotlib.pyplot as plt
import modules.global_graph as gb
import numpy as np
from matplotlib.ticker import AutoMinorLocator
# from scipy import stats

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

# The location is in best by default but it can happen that the location chosen
# by matplotlib is not optimal. That's why location is kept as a parameter to
# be able to change it in case of bad choice from matplotlib.
def plot_1D(magdata, column, title, xlab, ylab, location='best'):
    plt.figure(dpi=200)
    a = plt.subplot()
    plt.plot(magdata['hour'], magdata[column], linewidth=.4, color=plot_color[gb.color%12],
    linestyle='-', label=column)
    plt.title(title, fontsize=14)
    plt.grid(b=True)
    plt.legend(loc=location, fontsize= 8)
    if xlab == 'Time in hours':
            plt.xlim([0, 24])
            plt.xticks(np.arange(0,25,4)) # Show the last tick of the x-axes to see the 24-hours mark
            a.xaxis.set_minor_locator(AutoMinorLocator(4))
            plt.tick_params('x', which='minor', length=6)
            plt.tick_params('x', which='major', length=8)
    plt.xlabel(xlab, fontsize=12)
    plt.ylabel(ylab, fontsize=12)
    plt.show()   # This is to display the plot
    gb.color += 1


def plot_2D(magdata, horizontal1, vertical1, horizontal2, vertical2, title,
            xlab, ylab, location='best', mark = False):
    plt.figure(dpi=200)
    a = plt.subplot()
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
    if xlab == 'Time in hours':
            plt.xlim([0, 24])
            plt.xticks(np.arange(0,25,4)) # Show the last tick of the x-axes to see the 24-hours mark
            a.xaxis.set_minor_locator(AutoMinorLocator(4))
            plt.tick_params('x', which='minor', length=6)
            plt.tick_params('x', which='major', length=8)
    plt.legend(loc=location, fontsize= 8)
    plt.xlabel(xlab, fontsize=12)
    plt.ylabel(ylab, fontsize=12)
    plt.show()

def plot_2D_scatter(magdata, horizontal1, vertical1, horizontal2, vertical2, title,
            xlab, ylab, location='best'):
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(1,1,1)
    x_axis = magdata[horizontal1]
    # x_axis = np.log10(abs(magdata[horizontal1]))
    y_marker = np.sign(magdata[vertical1])*np.log10(abs(magdata[vertical1]))
    x_axis2 = np.sign(magdata[horizontal1])*magdata[horizontal2]
    # x_axis2 = np.log10(abs(magdata[horizontal2]))
    y_marker2 = np.sign(magdata[vertical2])*np.log10(abs(magdata[vertical2]))
    ax.scatter(x_axis, y_marker, s=.5, facecolors=plot_color[gb.color%12],
               edgecolors=plot_color[gb.color%12], label = 'dB/dt_1min')
    gb.color += 1
    ax.scatter(x_axis2, y_marker2, s=.5, facecolors=plot_color[gb.color%12],
               edgecolors=plot_color[gb.color%12], label = '<dB/dt>_1min')
    gb.color += 1
    plt.title(title, fontsize=14)
    plt.grid(b=True)
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.xlabel(xlab, fontsize=12)
    plt.ylabel(ylab, fontsize=12)
    # return (distribution(x_axis, y_marker), distribution(x_axis2, y_marker2))


def plot_3D(magdata, horizontal1, vertical1, horizontal2, vertical2, horizontal3,
            vertical3, title, xlab, ylab, location='best'):
    plt.figure(dpi=200)
    a = plt.subplot()
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
    if xlab == 'Time in hours':
            plt.xlim([0, 24])
            plt.xticks(np.arange(0,25,4)) # Show the last tick of the x-axes to see the 24-hours mark
            a.xaxis.set_minor_locator(AutoMinorLocator(4))
            plt.tick_params('x', which='minor', length=6)
            plt.tick_params('x', which='major', length=8)
    plt.legend(loc=location, fontsize= 8)
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


# def distribution(x, y):
#     binx = np.arange(min(x),max(x), 0.1)
#     biny = np.arange(min(y),max(y), 0.5)
#     ret = stats.binned_statistic_2d(x, y, None, 'count', bins=[binx, biny])
#     return ret.statistic
