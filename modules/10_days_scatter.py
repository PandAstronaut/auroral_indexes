# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:47:08 2021
@author: Bastien Longeon
"""
import pandas as pd     # pandas is for reading file
import numpy as np      # instead of math to convert X,Y <--> H,D
import time
import modules.plotter as plotter
import modules.global_graph as gb
import modules.auroral_index_functions as aur
import matplotlib.pyplot as plt
startTime = time.time()

gb.initialize()

folder = 'maggraphs/'
station_dec = 'kir20'
year = '17'
extension_hdf = '09sec.hdf5'
filename = folder + station_dec + year + extension_hdf # Corresponds to the path + filename
auroral_index = pd.DataFrame()


for i in range(8,9):
    print('Processing data for the {} of september 20{}'.format(i+1, year))
    magdata = pd.read_hdf(filename, start=i*86400, stop=(i+1)*86400)
    magdata['hour'] = np.linspace(0,24,86400)
                    ###              Auroral Index 1              ####
    auroral_index['Auroral_Index_1_1_H'] = aur.auroral_index1_1(magdata, 'KIR_H')
    auroral_index['Auroral_Index_1_2_H'] = aur.auroral_index1_2(magdata, 'KIR_H')
    auroral_index['Auroral_Index_1_1_Z'] = aur.auroral_index1_1(magdata, 'KIR_Z')
    auroral_index['Auroral_Index_1_2_Z'] = aur.auroral_index1_2(magdata, 'KIR_Z')
                    ###              Auroral Index 2              ####
    auroral_index['Auroral_Index_2_H'] = aur.auroral_index2(magdata, 'KIR_H', 2017)
    auroral_index['Auroral_Index_2_Z'] = aur.auroral_index2(magdata, 'KIR_Z', 2017)
    date = '2017.09.' + str(i+1)
    for i in range(0,1440):
        if abs(auroral_index['Auroral_Index_2_H'].iloc[i]) < 50 and abs(auroral_index['Auroral_Index_1_2_H'].iloc[i]) < 1:
            auroral_index['Auroral_Index_2_H'].iloc[i] = np.nan
            auroral_index['Auroral_Index_2_Z'].iloc[i] = np.nan
    auroral_index['Auroral_Index_1_1_H'].replace(to_replace=0, value=np.nan, inplace=True)
    auroral_index['Auroral_Index_1_2_H'].replace(to_replace=0, value=np.nan, inplace=True)
    auroral_index['Auroral_Index_2_H'].replace(to_replace=0, value=np.nan, inplace=True)
    auroral_index['Auroral_Index_1_1_Z'].replace(to_replace=0, value=np.nan, inplace=True)
    auroral_index['Auroral_Index_1_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)
    auroral_index['Auroral_Index_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)
                    ###              Plot             ####
    plotter.plot_2D_scatter(auroral_index, 'Auroral_Index_1_1_H', 'Auroral_Index_2_H', 'Auroral_Index_1_2_H',
                    'Auroral_Index_2_H', 'Horizontal Auroral index 2 = f(Auroral index 1(1) & 1(2))\nabs(dB_H) > 50 nT and <dB/dt>_1min > 1 nT/s\n'+ date,
                    '[nT/s]','log(dB) [nT]')
    plt.savefig('D:/Desktop/Stage/Plots/10_days_of_scatter/' + date + ' - horizontal.png', dpi=300, bbox_inches='tight')

    plt.show()
    plotter.plot_2D_scatter(auroral_index, 'Auroral_Index_1_1_Z', 'Auroral_Index_2_Z', 'Auroral_Index_1_2_Z',
                    'Auroral_Index_2_Z', 'Vertical Auroral index 2 = f(Auroral index 1(1) & 1(2))\nabs(dB_H) > 50 nT and <dB/dt>_1min > 1 nT/s\n'+ date,
                    '[nT/s]','log(dB) [nT]', location = 'lower left')
    plt.savefig('D:/Desktop/Stage/Plots/10_days_of_scatter/' + date + ' - vertical.png', dpi=300, bbox_inches='tight')
    plt.show()

                ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))

