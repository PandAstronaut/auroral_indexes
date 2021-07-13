# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:58:50 2021
@author: Bastien Longeon

This code plots 1, 2 and 3D plots with the color changing each time a graph has
been made. It takes data coming from pandas DataFrame.
"""
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import modules.global_graph as gb
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from matplotlib import gridspec

plot_color = ['#000000',   # 0: black
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
    plt.plot(magdata['hour'], magdata[column], linewidth=.4, color='r',linestyle='-', label=column)
    plt.title(title, fontsize=14)
    plt.grid(b=True)
    # plt.legend(loc=location, fontsize= 8)
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
    plt.close()


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
    plt.legend(loc=location, fontsize=8)
    plt.xlabel(xlab, fontsize=12)
    plt.ylabel(ylab, fontsize=12)
    plt.show()

def plot_2D_scatter(magdata, horizontal1, vertical1, horizontal2, vertical2, title,
            xlab, ylab, label1, label2, location='best'):
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(1,1,1)
    x_axis = magdata[horizontal1]
    y_marker = magdata[vertical1]
    x_axis2 = magdata[horizontal2]
    y_marker2 = magdata[vertical2]
    ax.scatter(x_axis, y_marker, s=.5, facecolors=plot_color[gb.color%12],
               edgecolors=plot_color[gb.color%12], label = label1)
    gb.color += 1
    ax.scatter(x_axis2, y_marker2, s=.5, facecolors=plot_color[gb.color%12],
               edgecolors=plot_color[gb.color%12], label = label2)
    gb.color += 1
    plt.title(title, fontsize=14)
    plt.grid(b=True)
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.xlabel(xlab, fontsize=12)
    plt.ylabel(ylab, fontsize=12)

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

def plot_3D_scatter(magdata, station_name, date, horizontal1, vertical1, horizontal2, vertical2, horizontal3,
                    vertical3, title, xlab, ylab, label1, label2, label3, location='best'):
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(1,1,1)
    x_axis = magdata[horizontal1]
    y_marker = magdata[vertical1]
    x_axis2 = magdata[horizontal2]
    y_marker2 = magdata[vertical2]
    x_axis3 = magdata[horizontal3]
    y_marker3 = magdata[vertical3]
    ax.scatter(x_axis, y_marker, s=.4, facecolors=plot_color[gb.color%12],
               edgecolors=plot_color[gb.color%12], label = label1)
    gb.color += 1
    ax.scatter(x_axis2, y_marker2, s=.4, facecolors=plot_color[gb.color%12],
               edgecolors=plot_color[gb.color%12], label = label2)
    gb.color += 1
    ax.scatter(x_axis3, y_marker3, marker='x' ,s=.4, facecolors=plot_color[gb.color%12],
               edgecolors=plot_color[gb.color%12], label = label3)
    gb.color += 1
    plt.title(title, fontsize=14)
    plt.grid(b=True)
    plt.xlim([-0.2, 0.6])
    plt.ylim([-0.2, 0.6])
    if station_name == 'Lycksele':
        plt.xlim([-3, 0])
        plt.ylim([-3, 0])
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.xlabel(xlab, fontsize=12)
    plt.ylabel(ylab, fontsize=12)
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/' + station_name + '/Distribution/' + date[0:4] + '/' + station_name +  ' - Horizontal and Vertical distribution - ' + date + '.png', dpi=300, bbox_inches='tight')
    plt.savefig('D:/Desktop/Stage/Plots/New distribution plots/' + station_name + '/' + station_name +  ' - Horizontal and Vertical distribution - ' + date + '.png', dpi=300, bbox_inches='tight')
    plt.show()
    distribution(station_name, date, x_axis, y_marker, x_axis2, y_marker2, x_axis3, y_marker3)

def distribution(station_name, date, x, y, x2, y2, x3, y3):
    try:
        binx = np.arange(-0.2, 0.61, 0.05)
        biny = np.arange(-0.2, 0.61, 0.05)
        if station_name == 'Lycksele':
            binx = np.arange(-3, 0.1, 0.05)
            biny = np.arange(-3, 0.1, 0.05)
        fig = plt.figure(dpi=300)
        gs = gridspec.GridSpec(3, 1)
        ttl = plt.suptitle(station_name + ' - ' + date, fontsize=10)
        ttl.set_position([0.7, .98])
        H, binx, biny = np.histogram2d(x, y, bins=(binx, biny))
        H = H.T  # Histogram does not follow Cartesian convention (see Notes), therefore transpose H for visualization purposes.
        ax1 = fig.add_subplot(gs[0], aspect='equal')
        X, Y = np.meshgrid(binx, biny)
        f1 = ax1.pcolormesh(X, Y, H, norm=colors.LogNorm(vmin=1, vmax=H.max()))
        # plt.xticks(np.arange(-0.2, 0.61, 0.2))
        if station_name == 'Lycksele':
            plt.xticks(np.arange(-3, 0.01, 1))
        H2, binx, biny = np.histogram2d(x2, y2, bins=(binx, biny))
        H2 = H2.T
        ax2 = fig.add_subplot(gs[1], aspect='equal')
        X2, Y2 = np.meshgrid(binx, biny)
        f2 = ax2.pcolormesh(X2, Y2, H2, norm=colors.LogNorm(vmin=1, vmax=H.max()))
        # plt.xticks(np.arange(-0.2, 0.61, 0.2))
        if station_name == 'Lycksele':
            plt.xticks(np.arange(-3, 0.01, 1))
        H3, binx, biny = np.histogram2d(x3, y3, bins=(binx, biny))
        H3 = H3.T
        ax3 = fig.add_subplot(gs[2], aspect='equal')
        X3, Y3 = np.meshgrid(binx, biny)
        f3 = ax3.pcolormesh(X3, Y3, H3, norm=colors.LogNorm(vmin=1, vmax=H.max()))
        # plt.xticks(np.arange(-0.2, 0.61, 0.2))
        if station_name == 'Lycksele':
            plt.xticks(np.arange(-3, 0.01, 1))
        ax1.set_title(label='X', fontsize=7)
        ax2.set_title(label='Y', fontsize=7)
        ax3.set_title(label='Z', fontsize=7)
        ax1.tick_params(labelsize=5)
        ax2.tick_params(labelsize=5)
        ax3.tick_params(labelsize=5)
        cb = fig.colorbar(f1, ax = ax1)
        # cb.locator = ticker.MaxNLocator(nbins=6)
        cb.ax.tick_params(labelsize=8)
        cb.update_ticks()
        cb = fig.colorbar(f2, ax = ax2)
        cb.ax.tick_params(labelsize=8)
        cb.update_ticks()
        cb = fig.colorbar(f3, ax = ax3)
        cb.ax.tick_params(labelsize=8)
        cb.update_ticks()
        plt.subplots_adjust(hspace=.5) # Horizontal gap between subplots
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/' + station_name + '/Distribution/' + date[0:4] + '/' + station_name +  ' - points distribution - ' + date + '.png', dpi=300, bbox_inches='tight')
        plt.savefig('D:/Desktop/Stage/Plots/New distribution plots/' + station_name + '/' + station_name +  ' - points distribution - ' + date + '.png', dpi=300, bbox_inches='tight')
        plt.show()
    except: plt.close('all')
