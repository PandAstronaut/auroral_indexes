# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 10:32:37 2021
@author: Bastien Longeon
"""
import pandas as pd     # pandas is for reading file
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import time
startTime = time.time()

box = {'boxstyle': 'square',
       'facecolor': 'none'}

folder = "maggraphs/"
stations = ['kir', 'abk', 'lyc']
extension_hdf = '09sec.hdf5'


plt.figure(dpi=300, figsize=(5*len(stations), 3*len(stations)))
days = np.linspace(1, 30, 120)
iteration = 0
for station in stations:
    filename = folder + station +  '2020' + extension_hdf
    auroral_index = pd.read_hdf(filename, 'index')
    if station == 'kir':
        station_name = 'Kiruna'
    elif station =='abk':
        station_name = 'Abisko'
    elif station =='lyc':
        station_name = 'Lycksele'

    gs = gridspec.GridSpec(len(stations), 1)
    standard_deviation1 = list()
    standard_deviation2 = list()
    for i in range(0,43200, 360):
        standard_deviation1.append(np.std(auroral_index['Auroral_Index_1_2_Z/X'].iloc[i:i+359]))
        standard_deviation2.append(np.std(auroral_index['Auroral_Index_1_2_Z/Y'].iloc[i:i+359]))
    # Plot
    a = plt.subplot(gs[iteration])
    (line1, line2) = a.plot(days, standard_deviation1, days, standard_deviation2, linewidth=1)
    # Plot setup
    if iteration == 0:
        plt.title('6-hours standard deviation of Z/X and Z/Y comparison for northern stations\n\n' + station_name)
    else: plt.title(station_name)
    plt.xlim([1, 30])
    plt.ylim([0, 0.45])
    a.grid()
    if station != stations[-1]:
        plt.setp(a.get_xticklabels(), visible=False)

    # Study of the standard deviation
    count1 = 0
    count1_2 = 0
    count2 = 0
    count2_2 = 0
    for value in standard_deviation1:
        if value < 0.1:
            count1 += 1
        if value < 0.05:
            count1_2 += 1
    for value in standard_deviation2:
        if value < 0.1:
            count2 += 1
        if value < 0.05:
            count2_2 += 1
    a.text(1.5, .33, 'Values < 0.1:\nZ/X: ' + str(sum(k < 0.1 for k in standard_deviation1)) + '\nZ/Y: ' + str(sum(k < 0.1 for k in standard_deviation2)), bbox=box)
    a.text(13, .37, 'Z/X Average: {0:.3f}'.format(np.average(standard_deviation1)) + '\nZ/Y Average: {0:.3f}'.format(np.average(standard_deviation2)), bbox=box)
    a.text(27, .33, 'Values < 0.05:\nZ/X: ' + str(sum(k < 0.05 for k in standard_deviation1)) + '\nZ/Y: ' + str(sum(k < 0.05 for k in standard_deviation2)), bbox=box)
    iteration += 1
plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation Comparison', dpi=300, bbox_inches='tight')
plt.show()

###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
