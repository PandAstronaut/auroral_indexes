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
station_dec = 'kir'
extension_hdf = '09sec.hdf5'
auroral_index = pd.DataFrame()
auroral_index['hour'] = np.linspace(0, 24, 1440)

for year in range(2011,2021): # Year: 11 to 21
    for i in range(0,30): # Day in september: 0 to 30
        gb.initialize() # The color is initialized at the begining of each day so that we have the same colors everyday
        filename = folder + station_dec +  str(year) + extension_hdf
        if i < 9: day = '0' + str(i+1)
        else : day = str(i+1)
        date = str(year) + '.09.' + day
        print('Processing data for the {}'.format(date))
        magdata = pd.read_hdf(filename, start=i*86400, stop=(i+1)*86400)
                ###              Auroral Index 1              ####
        auroral_index['Auroral_Index_1_1_H'] = aur.auroral_index1_1(magdata, 'KIR_H')
        auroral_index['Auroral_Index_1_2_H'] = aur.auroral_index1_2(magdata, 'KIR_H')
        auroral_index['Auroral_Index_1_1_Z'] = aur.auroral_index1_1(magdata, 'KIR_Z')
        auroral_index['Auroral_Index_1_2_Z'] = aur.auroral_index1_2(magdata, 'KIR_Z')

                        ###              Auroral Index 2              ####
        auroral_index['Auroral_Index_2_H'] = aur.auroral_index2(magdata, 'KIR_H', year)
        auroral_index['Auroral_Index_2_Z'] = aur.auroral_index2(magdata, 'KIR_Z', year)

                        ###              Auroral Index 1.2: Z/H              ####
        auroral_index['Auroral_Index_1_2_Z/H'] = auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_H']

                        ###              Auroral Index 2: Z/H              ####
        auroral_index['Auroral_Index_2_Z/H'] = auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_H']

        ###              (Auroral Index 2: Z/H) / (Auroral Index 1.2: Z/H)             ####
        auroral_index['DC/AC'] = auroral_index['Auroral_Index_2_Z/H']/auroral_index['Auroral_Index_1_2_Z/H']

        for k in range(0,1440):
            if abs(auroral_index['Auroral_Index_2_H'].iloc[k]) < 50 and abs(auroral_index['Auroral_Index_1_2_H'].iloc[k]) < 1:
                auroral_index['Auroral_Index_1_2_Z/H'].iloc[k] = np.nan
                auroral_index['Auroral_Index_2_Z/H'].iloc[k] = np.nan
                auroral_index['DC/AC'].iloc[k] = np.nan

                        ###              Plots              ####
        plt.figure(dpi=300, figsize=(15, 8))
        gs = gridspec.GridSpec(4, 1)
        # Subplot 1
        a1 = plt.subplot(gs[0])
        line1, = a1.plot(auroral_index['hour'], auroral_index['Auroral_Index_1_2_Z/H'], label='(dBAC_Z/dBAC_H)')
        plt.title('Auroral indexes quotients during Auroral Activity\nfor abs(dB_H) > 50 nT and <dB/dt>_1min > 1 nT/s\n' + date, fontsize=15)
        # Subplot 2
        a2 = plt.subplot(gs[1], sharex = a1)
        line2, = a2.plot(auroral_index['hour'], np.sign(auroral_index['Auroral_Index_2_Z/H'])*np.log10(abs(auroral_index['Auroral_Index_2_Z/H'])), label='log10(dBDC_Z/ dBDC_H)')
        # Subplot 3
        a3 = plt.subplot(gs[2], sharex = a1)
        line3, = a3.plot(auroral_index['hour'], np.sign(auroral_index['DC/AC'])*np.log10(abs(auroral_index['DC/AC'])), label='log10((dBDC_Z/ dBDC_H)/(dBAC_Z/ dBAC_H))')
        # Subplot 4
        a4 = plt.subplot(gs[3], sharex = a1)
        (line4, line5) = a4.plot(auroral_index['hour'], auroral_index['Auroral_Index_2_H'],
                                 auroral_index['hour'], auroral_index['Auroral_Index_1_2_H'].multiply(100))
        # Plot setup
        plt.setp(a1.get_xticklabels(), visible=False)
        plt.setp(a2.get_xticklabels(), visible=False)
        plt.setp(a3.get_xticklabels(), visible=False)
        a1.grid()
        a2.grid()
        a3.grid()
        a4.grid()
        a1.legend()
        a2.legend()
        a3.legend()
        a4.legend([line4, line5],["dBDC_H", "dBAC_H"])
        a2.set_ylim([-1, 2])
        a3.set_ylim([-1, 2])
        plt.xlim([0, 24])
        plt.xticks(np.arange(0,25,4)) # Show the last tick of the x-axes to see the 24-hours mark
        a3.xaxis.set_minor_locator(AutoMinorLocator(5))
        a3.tick_params('x', which='minor', length=6)
        a3.tick_params('x', which='major', length=8)
        plt.subplots_adjust(hspace=0.1) # Vertical gap between subplots
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/4_pannels/' + str(year) + '/4 pannels' + date + '.png', dpi=300, bbox_inches='tight')
        plt.show()


        for l in range(0,1440):
            if abs(auroral_index['Auroral_Index_2_H'].iloc[l]) < 50 and abs(auroral_index['Auroral_Index_1_2_H'].iloc[l]) < 1:
                auroral_index['Auroral_Index_2_H'].iloc[l] = np.nan
                auroral_index['Auroral_Index_2_Z'].iloc[l] = np.nan
        auroral_index['Auroral_Index_1_1_H'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_2_H'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_2_H'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_1_Z'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)

        plotter.plot_2D_scatter(auroral_index, 'Auroral_Index_1_1_H', 'Auroral_Index_2_H', 'Auroral_Index_1_2_H',
            'Auroral_Index_2_H', 'Horizontal Auroral index 2 = f(Auroral index 1(1) & 1(2))\nfor abs(dB_H) > 50 nT and <dB/dt>_1min > 1 nT/s\n'+ date,
            '[nT/s]','log(dB) [nT]')
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Distribution/' + str(year) + '/Horizontal distribution - ' + date + '.png', dpi=300, bbox_inches='tight')
        plt.show()
        plotter.plot_2D_scatter(auroral_index, 'Auroral_Index_1_1_Z', 'Auroral_Index_2_Z', 'Auroral_Index_1_2_Z',
                    'Auroral_Index_2_Z', 'Vertical Auroral index 2 = f(Auroral index 1(1) & 1(2))\nfor abs(dB_H) > 50 nT and <dB/dt>_1min > 1 nT/s\n'+ date,
                    '[nT/s]','log(dB) [nT]')
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Distribution/' + str(year) + '/Vertical distribution - ' + date + '.png', dpi=300, bbox_inches='tight')
        plt.show()

            ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
