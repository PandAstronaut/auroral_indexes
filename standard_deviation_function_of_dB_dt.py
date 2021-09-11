# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 11:11:27 2021
@author: Bastien Longeon
"""
import pandas as pd # pandas is for reading file
import numpy as np
import matplotlib.pyplot as plt

save = False

folder = "maggraphs/"
month = '09'
year = '2015'
if year == '2021':
    month = '03'
extension_hdf = month + 'sec.hdf5'

stations = ['nur','ups','lyc','kir','abk','brw','blc', 'hrn', 'cbb']

for station in stations:
    if station =='nur': station_name = 'Nurmijärvi'
    elif station =='ups': station_name = 'Uppsala'
    elif station =='lyc': station_name = 'Lycksele'
    elif station == 'kir': station_name = 'Kiruna'
    elif station =='abk': station_name = 'Abisko'
    elif station =='brw': station_name = 'Barrow'
    elif station =='blc': station_name = 'Baker Lake'
    elif station =='cbb': station_name = 'Cambridge Bay'
    elif station =='hrn': station_name = 'Hornsund'

    filename = folder + station +  year + extension_hdf
    auroral_index = pd.read_hdf(filename, 'index')
    std = list()
    dB_DC = list()
    for k in range(0, 43200, 60):
        a = np.nanmean(auroral_index['Auroral_Index_2_H'].iloc[k:k+60])
        if abs(a) > 30:
            std.append(np.nanstd(auroral_index['Auroral_Index_1_2_Z/H'].iloc[k:k+60]))
            dB_DC.append(a)
    plt.figure(dpi=300)
    plt.title('Standard deviation of log((dB/dt(Z))/(dB/dt(H))) in function of dB_DC(H)\n' + station_name)
    plt.scatter(dB_DC, std, s=.5)

    plt.xlabel('dB_DC(H)')
    plt.ylabel('Std(dB/dt(Z/H))')
    plt.xlim([-250,250])
    if save:
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/Distribution/' + station_name + ' - Standard Deviation of dB.dt(Z.H) in function of dB_DC.png', dpi=300, bbox_inches='tight')
    plt.show()

stations = ['kir','abk']

for station in stations:
    if station == 'kir': station_name = 'Kiruna'
    elif station =='abk': station_name = 'Abisko'
    filename = folder + station +  year + extension_hdf
    auroral_index = pd.read_hdf(filename, 'index', start = 13560, stop = 17280)
    std = list()
    dB_DC = list()
    for k in range(0, 17280 - 13560, 60):
        a = np.nanmean(auroral_index['Auroral_Index_2_H'].iloc[k:k+60])
        if abs(a) > 50:
            std.append(np.nanstd(auroral_index['Auroral_Index_1_2_Z/H'].iloc[k:k+60]))
            dB_DC.append(a)
    plt.figure(dpi=300)
    plt.title('Standard deviation of log((dB/dt(Z))/(dB/dt(H))) in function of dB_DC(H)\n' + station_name)
    plt.scatter(dB_DC, std, s=.5)

    plt.xlabel('dB_DC(H)')
    plt.ylabel('Std(dB/dt(Z/H))')
    # plt.xlim([-250,250])
    if save:
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/Distribution/' + station_name + ' - Standard Deviation of dB.dt(Z.H) in function of dB_DC.png', dpi=300, bbox_inches='tight')
    plt.show()
