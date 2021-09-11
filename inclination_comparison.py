# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:28:52 2021
@author: Bastien Longeon
"""

import pandas as pd # pandas is for reading file
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import time
startTime = time.time()

save = False

box = {'boxstyle': 'square',
        'facecolor': 'none'}

folder = "maggraphs/"

month = '09'
year = '2021'
if year == '2021':
    month = '03'
extension_hdf = month + 'sec.hdf5'

stations = ['ups','lyc','kir','abk'] 
# stations = ['nur','ups','lyc','kir','abk','blc','cbb','hrn']
    

plt.figure(dpi=300, figsize=(5*len(stations), 3*len(stations)))
if year == '2021':
    days = np.linspace(1, 31, 248)
else:
    days = np.linspace(1, 30, 240)
iteration = 0
gs = gridspec.GridSpec(len(stations), 1)
for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
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
    a.plot(days, standard_deviation['angle'], linewidth=1)
    # Plot setup
    if iteration == 0:
        plt.title('3-hours standard deviation comparison of the inclination for northern stations\n' + month + ' - ' + year + '\n' + station_name, fontsize=30)
    else: plt.title(station_name, fontsize=25)
    plt.xlim([1, 30])
    
    
    if year == '2017':
        plt.ylim([0, 0.8])
        a.text(1.5, .65, 'Values < 0.05:\n: {0:.2f}%'.format(sum(k < 0.05 for k in standard_deviation['angle'])*100/len(days)), fontsize=12, bbox=box)
        a.text(7, .7, 'latitude = ' + str(latitude) + '°', fontsize=16, bbox=box)
        a.text(15, .7, 'Average: {0:.3f}'.format(np.nanmean(standard_deviation['angle'])), fontsize=16, bbox=box)   
        a.text(27, .65, 'Values < 0.01:\n: {0:.2f}%'.format(sum(k < 0.01 for k in standard_deviation['angle'])*100/len(days)), fontsize=12, bbox=box)   
    
    elif year == '2020':
        plt.ylim([0, 0.4])
        a.text(1.5, .3, 'Values < 5e-2:\n: {0:.2f}%'.format(sum(k < 5e-2 for k in standard_deviation['angle'])*100/len(days)), fontsize=12, bbox=box)
        a.text(7, .35, 'latitude = ' + str(latitude) + '°', fontsize=16, bbox=box)
        a.text(15, .35, 'Average: {}'.format(str(np.format_float_scientific(np.nanmean(standard_deviation['angle']), precision = 2, exp_digits=2))), fontsize=16,bbox=box)
        a.text(28.5, .3, 'Values < 1e-2:\n: {0:.2f}%'.format(sum(k < 1e-2 for k in standard_deviation['angle'])*100/len(days)), fontsize=12, bbox=box)
    
    elif year == '2021':
        plt.xlim([1, 31])
        plt.ylim([0,0.23])
        a.text(1.5, .18, 'Values < 5e-2:\n: {0:.2f}%'.format(sum(k < 5e-2 for k in standard_deviation['angle'])*100/len(days)), fontsize=12, bbox=box)
        a.text(7, .19, 'latitude = ' + str(latitude) + '°', fontsize=16, bbox=box)
        a.text(15, .195, 'Average: {}'.format(str(np.format_float_scientific(np.nanmean(standard_deviation['angle']), precision = 2, exp_digits=2))), fontsize=16, bbox=box) 
        a.text(28, .18, 'Values < 1e-2:\n: {0:.2f}%'.format(sum(k < 1e-2 for k in standard_deviation['angle'])*100/len(days)), fontsize=12, bbox=box)
    
    a.grid()
    if station != stations[-1]:
        plt.setp(a.get_xticklabels(), visible=False)
        
    iteration += 1
plt.subplots_adjust(hspace=0.25) # Vertical gap between subplots
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/Inclination/Standard Deviation Comparison of the inclination.png', dpi=300, bbox_inches='tight')
plt.show()


plt.figure(dpi=300, figsize=(5*len(stations), 3*len(stations)))
iteration = 0
gs = gridspec.GridSpec(len(stations), 1)
for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
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
    a.plot(days, standard_deviation['dI/dt'], linewidth=1)
    # Plot setup
    if iteration == 0:
        plt.title('3-hours standard deviation comparison of dI/dt for northern stations\n' + month + ' - ' + year + '\n' + station_name, fontsize=30)
    else: plt.title(station_name, fontsize=25)
    
    plt.xlim([1, 30])
    
    if year == '2017':
        plt.ylim([0, 0.0035])
        a.text(1.5, .0028, 'Values < 1e-4:\n: {0:.2f}%'.format(sum(k < 1e-4 for k in standard_deviation['dI/dt'])*100/len(days)), fontsize=12, bbox=box)
        a.text(7, .003, 'latitude = ' + str(latitude) + '°', fontsize=16, bbox=box)
        a.text(15, .003, 'Average: {}'.format(str(np.format_float_scientific(np.nanmean(standard_deviation['dI/dt']), precision = 2, exp_digits=2))), fontsize=16, bbox=box) 
        a.text(27, .0028, 'Values < 1e-5:\n: {0:.2f}%'.format(sum(k < 1e-5 for k in standard_deviation['dI/dt'])*100/len(days)), fontsize=12, bbox=box)   
    elif year == '2020':
        plt.ylim([0, 0.0015])
        a.text(1.5, .0011, 'Values < 5e-5:\n: {0:.2f}%'.format(sum(k < 5e-5 for k in standard_deviation['dI/dt'])*100/len(days)), fontsize=12, bbox=box)
        a.text(7, .00125, 'latitude = ' + str(latitude) + '°', fontsize=16, bbox=box)
        a.text(15, .00125, 'Average: {}'.format(str(np.format_float_scientific(np.nanmean(standard_deviation['dI/dt']), precision = 2, exp_digits=2))), fontsize=16, bbox=box)
        a.text(28.5, .0011, 'Values < 1e-5:\n: {0:.2f}%'.format(sum(k < 1e-5 for k in standard_deviation['dI/dt'])*100/len(days)), fontsize=12, bbox=box)
    elif year == '2021':
        plt.xlim([1, 31])
        plt.ylim([0, 0.00065])
        a.text(1.5, .0005, 'Values < 0.1e-4:\n: {0:.2f}%'.format(sum(k < 0.0001 for k in standard_deviation['dI/dt'])*100/len(days)), fontsize=12, bbox=box)
        a.text(7, .00056, 'latitude = ' + str(latitude) + '°', fontsize=16, bbox=box)
        a.text(15, .00056, 'Average: {}'.format(str(np.format_float_scientific(np.nanmean(standard_deviation['dI/dt']), precision = 2, exp_digits=2))), fontsize=16, bbox=box) 
        a.text(28, .0005, 'Values < 1e-5:\n: {0:.2f}%'.format(sum(k < 0.00001 for k in standard_deviation['dI/dt'])*100/len(days)), fontsize=12, bbox=box)   

    a.grid()
    if station != stations[-1]:
        plt.setp(a.get_xticklabels(), visible=False)
        
    iteration += 1
plt.subplots_adjust(hspace=0.25) # Vertical gap between subplots
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/Inclination/Standard Deviation Comparison of dI.dt.png', dpi=300, bbox_inches='tight')
plt.show()



# =============================================================================
# Points count comparison in pie charts
# =============================================================================
textprops = {"fontsize":5} # Font size of text in pie chart
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
plt.figure(dpi=300)
if len(stations) > 4:
    gs = gridspec.GridSpec(3,4)
    plt.suptitle('Standard deviation distribution of dI/dt\n' + month + ' - ' + year, fontsize=10, x=0.5, y=.9)
    plt.subplots_adjust(hspace=-0.5)
else:
    gs = gridspec.GridSpec(1,4)
    plt.suptitle('Standard deviation distribution of dI/dt\n' + month + ' - ' + year, fontsize=10, x=0.5, y=0.75)
i = 0
row = 0
column = 0
labels=["0 - 2e-4","2e-4 - 4e-4","4e-4 - 6e-4","+6e-4"]
for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
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
    standard_deviation['dI/dt_bins'] = pd.cut(standard_deviation['dI/dt'],bins=[0, 2e-4, 4e-4, 6e-4, 1], labels=labels)
    
    if len(stations) > 4:
        if column > 3:
            column = 0
            row = 2
        plt.subplot(gs[row,column])
        plt.pie(standard_deviation['dI/dt_bins'].value_counts(sort=False), colors = colors)
        plt.text(-0.6, -1.5, str(latitude) + '°', fontsize=7)
        plt.title(station_name, fontsize=7)
        if station == stations[0]:
            plt.legend(labels, fontsize=4, loc='upper left')
        column += 1
    else:
        plt.subplot(gs[0,i-1])
        plt.pie(standard_deviation['dI/dt_bins'].value_counts(sort=False), colors = colors)
        if i == 1:
            plt.legend(labels, fontsize=4, loc='upper left')
        plt.text(-0.6, -1.5, str(latitude) + '°', fontsize=7)
        plt.title(station_name, fontsize=7)
plt.subplots_adjust(hspace=-0.6)
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/Inclination/Pie charts.png', dpi=300, bbox_inches='tight')
plt.show()  


# =============================================================================
# Average standard deviation in function of the geomagnetic latitude
# =============================================================================

plt.figure(dpi=300)
plt.title('Average Standard Deviation of dI/dt in function of the geomagnetic latitude\n' + month + ' - ' + year, fontsize=10)
plt.xlabel('Latitude (°)')
for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
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

    plt.scatter(latitude, np.nanmean(standard_deviation['dI/dt']))
    plt.annotate(station.upper(), # Text
                  (latitude, np.nanmean(standard_deviation['dI/dt'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center') # horizontal alignment can be left, right or center

    # plt.xlim([57,67])
    # if year == '2017':
    #     plt.ylim([2.5e-5, 2e-4])
    # elif year == '2020' or year =='2021':
    #     plt.ylim([0.9e-5, 1.1e-4])
    
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/Inclination/Average Standard Deviation of dI.dt in function of the geomagnetic latitude.png', dpi=300, bbox_inches='tight') 
plt.show()

###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))