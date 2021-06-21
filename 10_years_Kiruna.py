# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:05:11 2021
@author: Bastien Longeon

For everyday in september from 2011 to 2020, this code plots:

    · A 4-pannels comparison of the following quotients:
        Graph 1: Auroral index 1.2: Z/H
        Graph 2: Auroral index 2: Z/H
        Graph 3: (Auroral index 2 Z/H) / (Auroral index 1.2 Z/H)
        Graph 4: Auroral index 1.2 and 2: horizontal
            In function of time

    · dBDC in function of dBAC 1 & 2 for the vertical and horizontal component
"""
import pandas as pd     # pandas is for reading file
import numpy as np      # instead of math to convert X,Y <--> H,D
import modules.plotter as plotter
import modules.auroral_index_functions as aur
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.ticker import AutoMinorLocator
import modules.global_graph as gb
import time
startTime = time.time()
###              Define the file to read              ####
folder = "maggraphs/"
station = 'kir'
extension_hdf = '09sec.hdf5'
auroral_index = pd.DataFrame()
auroral_index['hour'] = np.linspace(0, 24, 1440)

for year in range(2017,2018): # Year: 11 to 21
    for i in range(7,8): # Day in september: 0 to 30
        gb.initialize()
        filename = folder + station +  str(year) + extension_hdf
        if i < 9: day = '0' + str(i+1)
        else : day = str(i+1)
        date = str(year) + '.09.' + day
        print('Processing data for the {}'.format(date))
        magdata = pd.read_hdf(filename, start=i*86400, stop=(i+1)*86400)

                ###              Auroral Index 1              ####
        auroral_index['Auroral_Index_1_1_H'] = aur.auroral_index1_1(magdata, 'KIR_H')
        auroral_index['Auroral_Index_1_2_H'] = aur.auroral_index1_2(magdata, 'KIR_H')
        auroral_index['Auroral_Index_1_1_Z'] = aur.auroral_index1_1(magdata, 'KIR_Z')
        auroral_index['Auroral_Index_1_2_X'] = aur.auroral_index1_2(magdata, 'KIR_X')
        auroral_index['Auroral_Index_1_2_Y'] = aur.auroral_index1_2(magdata, 'KIR_Y')
        auroral_index['Auroral_Index_1_2_Z'] = aur.auroral_index1_2(magdata, 'KIR_Z')

                        ###              Auroral Index 2              ####
        auroral_index['Auroral_Index_2_H'] = aur.auroral_index2(magdata, 'KIR_H', year)
        auroral_index['Auroral_Index_2_Z'] = aur.auroral_index2(magdata, 'KIR_Z', year)
        auroral_index['Auroral_Index_2_X'] = aur.auroral_index2(magdata, 'KIR_X', year)
        auroral_index['Auroral_Index_2_Y'] = aur.auroral_index2(magdata, 'KIR_Y', year)

                        ###              Auroral Index 1.2: Z/X Z/Y              ####
        auroral_index['Auroral_Index_1_2_Z/X'] = auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_X']
        auroral_index['Auroral_Index_1_2_Z/Y'] = auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_Y']

        ###              (Auroral Index 2: Z/X and Z/Y)             ####
        auroral_index['DC_ratio_X'] = np.sign(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_X'])*np.log10(abs(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_X']))
        auroral_index['DC_ratio_Y'] = np.sign(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_Y'])*np.log10(abs(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_Y']))

        ###              (dB/dt)/(<dB_1sec>_1min)             ####
        auroral_index['AC_ratio'] = abs(auroral_index['Auroral_Index_1_1_H'])/auroral_index['Auroral_Index_1_2_H']

        for k in range(0,1440):
            if abs(auroral_index['Auroral_Index_2_H'].iloc[k]) < 35 and abs(auroral_index['Auroral_Index_1_2_H'].iloc[k]) < 1:
                auroral_index['Auroral_Index_1_2_Z/X'].iloc[k] = np.nan
                auroral_index['Auroral_Index_1_2_Z/Y'].iloc[k] = np.nan
                auroral_index['DC_ratio_X'].iloc[k] = np.nan
                auroral_index['DC_ratio_Y'].iloc[k] = np.nan
            if auroral_index['Auroral_Index_1_2_H'].iloc[k] < 0.5:
                auroral_index['AC_ratio'].iloc[k] = np.nan

                        ###              Plots              ####
        plt.figure(dpi=300, figsize=(15, 8))
        gs = gridspec.GridSpec(5, 1)
        # Subplot 1
        a1 = plt.subplot(gs[0])
        (line1, ) = a1.plot(auroral_index['hour'], auroral_index['Auroral_Index_1_2_Z/X'], color='orange')
        line2 = a1.scatter(auroral_index['hour'], auroral_index['Auroral_Index_1_2_Z/Y'], s=.5, facecolors='blue',
               edgecolors='blue')
        plt.title('Auroral indexes quotients during Auroral Activity\nfor abs(dB_H) > 35 nT and <dB/dt>_1min > 1 nT/s\n' + date, fontsize=15)
        # Subplot 2
        a2 = plt.subplot(gs[1], sharex = a1)
        (line3, ) = a2.plot(auroral_index['hour'], auroral_index['DC_ratio_X'], color='orange')
        line4 = a2.scatter(auroral_index['hour'], auroral_index['DC_ratio_Y'], s=.5, facecolors='blue',
               edgecolors='blue')
        # Subplot 3
        a3 = plt.subplot(gs[2], sharex = a1)
        (line5, line6) = a3.plot(auroral_index['hour'], auroral_index['Auroral_Index_2_H'],
                                 auroral_index['hour'], auroral_index['Auroral_Index_1_2_H'].multiply(100))

        # Subplot 4
        a4 = plt.subplot(gs[3], sharex = a1)

        a4.scatter(auroral_index['hour'], auroral_index['AC_ratio'], s=.5, label = "abs(dB/dt)_H/<dB_1sec>_H")

        # Subplot 5
        a5 = plt.subplot(gs[4], sharex = a1)
        (line8, line9) = a5.plot(auroral_index['hour'], auroral_index['Auroral_Index_1_1_H'],
                                 auroral_index['hour'], auroral_index['Auroral_Index_1_2_H'])

        # Plot setup
        plt.setp(a1.get_xticklabels(), visible=False)
        plt.setp(a2.get_xticklabels(), visible=False)
        plt.setp(a3.get_xticklabels(), visible=False)
        a1.grid()
        a2.grid()
        a3.grid()
        a1.legend([line2, line1], ['dBAC_Z/dBAC_X', 'dBAC_Z/dBAC_Y'])
        a2.legend([line4, line3], ['log10(dBDC_Z/ dBDC_X)', 'log10(dBDC_Z/ dBDC_Y)'])
        a3.legend([line5, line6], ["dBDC_H", "dBAC_H x 100"])
        a4.legend()
        a5.legend([line8, line9],["(dB/dt)_H","<dB_1sec>_H"])
        a1.set_ylim([0, 3])
        a2.set_ylim([-2, 2])
        plt.xlim([0, 24])
        plt.xticks(np.arange(0,25,4)) # Show the last tick of the x-axes to see the 24-hours mark
        a2.yaxis.set_minor_locator(AutoMinorLocator(1))
        a5.xaxis.set_minor_locator(AutoMinorLocator(5))
        a5.tick_params('x', which='minor', length=6)
        a5.tick_params('x', which='major', length=8)
        plt.subplots_adjust(hspace=0.1) # Vertical gap between subplots
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/4_pannels/' + str(year) + '/4 pannels' + date + '.png', dpi=300, bbox_inches='tight')
        plt.show()

        for l in range(0,1440): # A criterion is applied here and not before because it would compromise the first plot
            if abs(auroral_index['Auroral_Index_2_H'].iloc[l]) < 35 and abs(auroral_index['Auroral_Index_1_2_H'].iloc[l]) < 1:
                auroral_index['Auroral_Index_2_H'].iloc[l] = np.nan
                auroral_index['Auroral_Index_2_Z'].iloc[l] = np.nan
        # These replacements avoid log10(0) errors without modifying the plots
        auroral_index['Auroral_Index_1_1_H'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_2_H'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_2_H'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_1_Z'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)

        plotter.plot_2D_scatter(auroral_index, 'Auroral_Index_1_1_H', 'Auroral_Index_2_H', 'Auroral_Index_1_2_H',
            'Auroral_Index_2_H', 'Horizontal Auroral index 2 = f(Auroral index 1(1) & 1(2))\nfor abs(dB_H) > 35 nT and <dB/dt>_1min > 1 nT/s\n'+ date,
            '[nT/s]','log(dB) [nT]')
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Distribution/' + str(year) + '/Horizontal distribution - ' + date + '.png', dpi=300, bbox_inches='tight')
        plt.show()
        plotter.plot_2D_scatter(auroral_index, 'Auroral_Index_1_1_Z', 'Auroral_Index_2_Z', 'Auroral_Index_1_2_Z',
                    'Auroral_Index_2_Z', 'Vertical Auroral index 2 = f(Auroral index 1(1) & 1(2))\nfor abs(dB_H) > 35 nT and <dB/dt>_1min > 1 nT/s\n'+ date,
                    '[nT/s]','log(dB) [nT]')
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Distribution/' + str(year) + '/Vertical distribution - ' + date + '.png', dpi=300, bbox_inches='tight')
        plt.show()

            ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
