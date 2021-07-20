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
stations = ['nur','ups','lyc','kir','abk','brw','blc', 'cbb', 'hrn']
extension_hdf = '09sec.hdf5'

standard_deviation = pd.DataFrame()
standard_deviation_dict1 = dict()
standard_deviation_dict2 = dict()
for station in stations:
    filename = folder + station +  '2020' + extension_hdf
    auroral_index = pd.read_hdf(filename, 'index')
    standard_deviation1 = list()
    standard_deviation2 = list()
    std = list()
    for i in range(0,43200, 180):
        std .append(np.nanstd(auroral_index['Auroral_Index_1_2_Z/H'].iloc[i:i+179]))
        standard_deviation1.append(np.nanstd(auroral_index['Auroral_Index_1_2_Z/X'].iloc[i:i+179]))
        standard_deviation2.append(np.nanstd(auroral_index['Auroral_Index_1_2_Z/Y'].iloc[i:i+179]))
    standard_deviation_dict1[station] = standard_deviation1
    standard_deviation_dict2[station] = standard_deviation2
    standard_deviation[station] = std

# =============================================================================
# Standard deviation comparison for every station
# =============================================================================

plt.figure(dpi=300, figsize=(5*len(stations), 3*len(stations)))
days = np.linspace(1, 30, 240)
iteration = 0
gs = gridspec.GridSpec(len(stations), 1)
for station in stations:
    if station =='nur': 
        station_name = 'Nurmijärvi'
        latitude = 58.06
    elif station =='ups': 
        station_name = 'Uppsala'
        latitude = 58.53
    elif station =='lyc': 
        station_name = 'Lycksele'
        latitude = 62.82
    elif station == 'kir': 
        station_name = 'Kiruna'
        latitude = 65.58
    elif station =='abk': 
        station_name = 'Abisko'
        latitude = 66.28
    elif station =='brw': 
        station_name = 'Barrow'
        latitude = 70.07
    elif station =='blc': 
        station_name = 'Baker Lake'
        latitude = 72.55
    elif station =='cbb': 
        station_name = 'Cambridge Bay'
        latitude = 76.13
    elif station =='hrn': 
        station_name = 'Hornsund'
        latitude = 74.28
    
    # Plot
    a = plt.subplot(gs[iteration])
    # (line1, line2) = a.plot(days, standard_deviation_dict1[station], days, standard_deviation_dict2[station], linewidth=1)
    a.plot(days, standard_deviation[station], linewidth=1)
    # Plot setup
    if iteration == 0:
        # plt.title('3-hours standard deviation of Z/X and Z/Y comparison for northern stations\n\n' + station_name, fontsize=25)
        plt.title('3-hours standard deviation of Z/H comparison for northern stations\n\n' + station_name, fontsize=25)

    else: plt.title(station_name, fontsize=25)
    plt.xlim([1, 30])
    plt.ylim([0, 0.45])
    a.grid()
    if station != stations[-1]:
        plt.setp(a.get_xticklabels(), visible=False)

    # Study of the standard deviation    
    # a.text(1.5, .305, 'Values < 0.1:\nZ/X: {0:.2f}%'.format(sum(k < 0.1 for k in standard_deviation_dict1[station])*100/240) + '\nZ/Y: {0:.2f}%'.format(sum(k < 0.1 for k in standard_deviation_dict2[station])*100/240), fontsize=12, bbox=box)
    # a.text(7, .38, 'latitude = ' + str(latitude) + '°', fontsize=16, bbox=box)
    # a.text(15, .35, 'Z/X Average: {0:.3f}'.format(np.nanmean(standard_deviation_dict1[station])) + '\nZ/Y Average: {0:.3f}'.format(np.nanmean(standard_deviation_dict2[station])), fontsize=12, bbox=box)
    # a.text(28.5, .305, 'Values < 0.05:\nZ/X: {0:.2f}%'.format(sum(k < 0.05 for k in standard_deviation_dict1[station])*100/240) + '\nZ/Y: {0:.2f}%'.format(sum(k < 0.05 for k in standard_deviation_dict2[station])*100/240), fontsize=12, bbox=box)   
   
    a.text(1.5, .36, 'Values < 0.1:\nZ/H: {0:.2f}%'.format(sum(k < 0.1 for k in standard_deviation[station])*100/240), fontsize=12, bbox=box)
    a.text(7, .39, 'latitude = ' + str(latitude) + '°', fontsize=16, bbox=box)
    a.text(15, .4, 'Z/H Average: {0:.3f}'.format(np.nanmean(standard_deviation[station])), fontsize=12, bbox=box)
    a.text(28.5, .36, 'Values < 0.05:\nZ/H: {0:.2f}%'.format(sum(k < 0.05 for k in standard_deviation[station])*100/240), fontsize=12, bbox=box)   
    
    
    iteration += 1
plt.subplots_adjust(hspace=0.25) # Vertical gap between subplots
plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/Standard Deviation Comparison for Z.H.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# Points count comparison in pie charts
# =============================================================================

textprops = {"fontsize":5} # Font size of text in pie chart
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','green']
plt.figure(dpi=300)
plt.suptitle('Standard deviation distribution of dB/dt_Z/H', fontsize=10, x=0.5, y=0.82)
gs = gridspec.GridSpec(2,6)
i = 0
row = 0
labels=["0-0.05","0.05-0.1","0.1-0.15","0.15-0.2","0.2+"]
for station in stations:
    if station =='nur': 
        station_name = 'Nurmijärvi'
        latitude = 58.06
    elif station =='ups': 
        station_name = 'Uppsala'
        latitude = 58.53
    elif station =='lyc': 
        station_name = 'Lycksele'
        latitude = 62.82
    elif station == 'kir': 
        station_name = 'Kiruna'
        latitude = 65.58
    elif station =='abk': 
        station_name = 'Abisko'
        latitude = 66.28
    elif station =='brw': 
        station_name = 'Barrow'
        latitude = 70.07
    elif station =='blc': 
        station_name = 'Baker Lake'
        latitude = 72.55
    elif station =='cbb': 
        station_name = 'Cambridge Bay'
        latitude = 76.13
    elif station =='hrn': 
        station_name = 'Hornsund'
        latitude = 74.28
    standard_deviation[station+'_bins'] = pd.cut(standard_deviation[station],bins=[0,0.05,0.1,0.15,0.2,1], labels=labels)
    i += 1
    if i < 4: column = i+1
    elif i == 4: column = 5
    elif i > 5: column = i-4
    if i == 6:
        row = 1
    if station == 'kir':
        plt.subplot(gs[:,0:2])
        plt.pie(standard_deviation[station+'_bins'].value_counts(sort=False), colors = colors)
        plt.legend(labels, fontsize=4, loc='upper left')
        plt.text(-0.25, -1.3, str(latitude) + '°', fontsize=7)
        plt.title(station_name, fontsize=7)
    else:
        plt.subplot(gs[row,column])
        plt.pie(standard_deviation[station+'_bins'].value_counts(sort=False), colors = colors)
        plt.text(-0.6, -1.5, str(latitude) + '°', fontsize=7)
        plt.title(station_name, fontsize=7)
plt.subplots_adjust(hspace=-0.5)
plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/Pie charts.png', dpi=300, bbox_inches='tight')
plt.show()  

# =============================================================================
# Average standard deviation in function of the geomagnetic latitude
# =============================================================================

plt.figure(dpi=300)
plt.title('Average Standard Deviation of dB/dt_Z/X in function of the geomagnetic latitude', fontsize=9)
plt.xlabel('Latitude (°)')
for station in stations:
    # Geomagnetic coordinates
    if station =='nur': latitude = 58.06
    elif station =='ups': latitude = 58.53
    elif station =='lyc': latitude = 62.82
    elif station == 'kir': latitude = 65.58
    elif station =='abk': latitude = 66.28
    elif station =='brw': latitude = 70.07
    elif station =='blc': latitude = 72.55
    elif station =='cbb': latitude = 76.13
    elif station =='hrn': latitude = 74.28

    plt.scatter(latitude, np.nanmean(standard_deviation_dict1[station]))
    plt.annotate(station.upper(), # Text
                  (latitude, np.nanmean(standard_deviation_dict1[station])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center') # horizontal alignment can be left, right or center
    plt.xlim([57,78])
    plt.ylim([0.05,0.29])
plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/Average Standard Deviation of dB.dt_Z.X in function of the geomagnetic latitude.png', dpi=300, bbox_inches='tight') 
plt.show()

plt.figure(dpi=300)
plt.title('Average Standard Deviation of dB/dt_Z/Y in function of the geomagnetic latitude', fontsize=9)
plt.xlabel('Latitude (°)')
for station in stations:
    # Geomagnetic coordinates
    if station =='nur': latitude = 58.06
    elif station =='ups': latitude = 58.53
    elif station =='lyc': latitude = 62.82
    elif station == 'kir': latitude = 65.58
    elif station =='abk': latitude = 66.28
    elif station =='brw': latitude = 70.07
    elif station =='blc': latitude = 72.55
    elif station =='cbb': latitude = 76.13
    elif station =='hrn': latitude = 74.28

    plt.scatter(latitude, np.nanmean(standard_deviation_dict2[station]))
    plt.annotate(station.upper(), # Text
                  (latitude, np.nanmean(standard_deviation_dict2[station])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center') # horizontal alignment can be left, right or center
    plt.xlim([57,78])
    plt.ylim([0.065,0.275])
plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/Average Standard Deviation of dB.dt_Z.Y in function of the geomagnetic latitude.png', dpi=300, bbox_inches='tight') 
plt.show()

plt.figure(dpi=300)
plt.title('Average Standard Deviation of dB/dt_Z/H in function of the geomagnetic latitude', fontsize=9)
plt.xlabel('Latitude (°)')
for station in stations:
    # Geomagnetic coordinates
    if station =='nur': latitude = 58.06
    elif station =='ups': latitude = 58.53
    elif station =='lyc': latitude = 62.82
    elif station == 'kir': latitude = 65.58
    elif station =='abk': latitude = 66.28
    elif station =='brw': latitude = 70.07
    elif station =='blc': latitude = 72.55
    elif station =='cbb': latitude = 76.13
    elif station =='hrn': latitude = 74.28

    plt.scatter(latitude, np.nanmean(standard_deviation[station]))
    plt.annotate(station.upper(), # Text
                  (latitude, np.nanmean(standard_deviation[station])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center') # horizontal alignment can be left, right or center
    plt.xlim([57,78])
    plt.ylim([0.05,0.29])
plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/Average Standard Deviation of dB.dt_Z.H in function of the geomagnetic latitude.png', dpi=300, bbox_inches='tight') 
plt.show()


###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
