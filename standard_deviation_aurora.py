# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:14:37 2021
@author: Bastien Longeon
"""
import pandas as pd # pandas is for reading file
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import time
import warnings
warnings.filterwarnings('ignore')
startTime = time.time()

month = '09'
year = '2021'
if year == '2021':
    month = '03'
extension_hdf = month + 'sec.hdf5'

for i in range(0,30): # Day in september: 0 to 30
    if i < 9: day = '0' + str(i+1)
    else : day = str(i+1)
    date = str(year) + '.'+ month +'.' + day

    plt.figure(dpi=300, figsize=(15, 8))
    gs = gridspec.GridSpec(5, 1)
    auroral_index_kir = pd.read_hdf('maggraphs/kir'+ year + extension_hdf, 'index', start=i*1440, stop=(i+1)*1440)
    auroral_index_abk = pd.read_hdf('maggraphs/abk'+ year + extension_hdf, 'index', start=i*1440, stop=(i+1)*1440)
    hour = np.linspace(0, 24, 1440)

    # for k in range(0, 1440):
    #     if abs(auroral_index_kir['Auroral_Index_2_H'].iloc[k]) < 75:
    #         auroral_index_kir['Auroral_Index_1_2_Z/H'].iloc[k] = np.nan
    #     if abs(auroral_index_abk['Auroral_Index_2_H'].iloc[k]) < 75:
    #         auroral_index_abk['Auroral_Index_1_2_Z/H'].iloc[k] = np.nan


    # Subplot 1
    a1 = plt.subplot(gs[0])
    line1 = a1.scatter(hour, auroral_index_abk['Auroral_Index_1_2_Z/H'], s=.5, color='blue')
    plt.title('Auroral indexes quotients and hourly standard deviation difference during Auroral Activity\nAbisko vs Kiruna - ' + date, fontsize=15)
    # Subplot 2
    a2 = plt.subplot(gs[1], sharex = a1)
    (line2,) = a2.plot(hour, auroral_index_abk['Auroral_Index_2_H'], linewidth=.8)

    # Subplot 3
    a3 = plt.subplot(gs[2], sharex = a1)
    line3 = a3.scatter(hour, auroral_index_kir['Auroral_Index_1_2_Z/H'], s=.5, color='orange')
    # Subplot 4
    a4 = plt.subplot(gs[3], sharex = a1)
    (line4,) = a4.plot(hour, auroral_index_kir['Auroral_Index_2_H'], color='orange', linewidth=.8)

    # Plot setup
    plt.setp(a1.get_xticklabels(), visible=False)
    plt.setp(a2.get_xticklabels(), visible=False)
    plt.setp(a3.get_xticklabels(), visible=False)
    plt.setp(a4.get_xticklabels(), visible=False)
    a1.grid()
    a2.grid()
    a3.grid()
    a4.grid()
    a1.legend([line1], ['log10(dBAC_Z/dBAC_H)_ABK'])
    a2.legend([line2], ['dBDC_H_ABK'])
    a3.legend([line3], ['log10(dBAC_Z/dBAC_H)_KIR'])
    a4.legend([line4], ['dBDC_H_KIR'])
    a1.set_ylim([-0.7, 0.7])
    a3.set_ylim([-0.7, 0.7])
    plt.xlim([0, 24])
    plt.xticks(np.arange(0,25,4)) # Show the last tick of the x-axes to see the 24-hours mark

    # Standard deviation study
    a = plt.subplot(gs[4])
    std_kir = list()
    std_abk = list()
    std = list()
    for k in range(0, 1440, 60):
        std_kir.append(np.nanstd(auroral_index_kir['Auroral_Index_1_2_Z/H'].iloc[k:k+60]))
        std_abk.append(np.nanstd(auroral_index_abk['Auroral_Index_1_2_Z/H'].iloc[k:k+60]))
    # for k in range(0,24):
    #     std.append(std_abk[k] - std_kir[k])

    color = list()
    for k in range(0,1440,60):
        if np.nanmean(auroral_index_kir['Auroral_Index_2_H'].iloc[k:k+60]) > 50:
            color.append('r')
        elif np.nanmean(auroral_index_kir['Auroral_Index_2_H'].iloc[k:k+60]) < -50:
            color.append('y')
        else:
            color.append('b')
    hours = np.linspace(.5, 23.5, 24)
    scatter = a.scatter(hours, std_kir, c = color)
    a.grid()
    plt.xlim([0, 24])
    plt.ylim([-0.15, 0.35])
    # plt.legend(['std_abk - std_kir'])
    names = ['dBDC_kir < -50', 'dBDC_kir > 50', '-50 < dBDC_kir < 50']
    plt.legend(['std_kir'])
    plt.xticks(np.arange(0,25,4))

    plt.subplots_adjust(hspace=0.12) # Vertical gap between subplots
    plt.show()


###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
