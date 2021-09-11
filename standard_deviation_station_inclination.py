# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:23:20 2021
@author: Bastien Longeon
"""
import pandas as pd # pandas is for reading file
import numpy as np
import matplotlib.pyplot as plt

save = True

folder = "maggraphs/"
year = '2020'
month = '09'
if year == '2021':
    month = '03'
extension_hdf = month + 'sec.hdf5'

stations = ['ups','lyc','kir','abk']

inclination_nur = {'2020':73.5}

inclination_ups = {'2017':72.82,
                   '2020':72.89,
                   '2021':72.89}

inclination_lyc = {'2017':75.51,
                   '2020':75.59,
                   '2021':75.59}

inclination_kir = {'2017':78.46,
                   '2020':78.53,
                   '2021':78.53}

inclination_abk = {'2017':77.59,
                   '2020':77.68,
                   '2021':77.84}

inclination_brw = {'2017':80.81,
                   '2020':80.81}

inclination_blc = {'2017':83.27,
                   '2020':83.05}

inclination_cbb = {'2017':85.22,
                   '2020':84.94}

inclination_hrn = {'2020':81.74}

max_y = 0
plt.figure(dpi=300)
plt.title('Average Standard Deviation of dB/dt(Z) in function of the inclination\n' + month + ' - ' + year, fontsize=10)
plt.xlabel('Inclination (°)')
for station in stations:
    filename = folder + station +  year + extension_hdf
    auroral_index = pd.read_hdf(filename, 'index')
    std_Z = list()
    for i in range(0, 43200, 180):
        std_Z.append(np.nanstd(auroral_index['Auroral_Index_1_2_Z'].iloc[i:i+180]))
    if station =='nur':
        inclination =  inclination_nur[year]
    elif station =='ups':
        inclination =  inclination_ups[year]
    elif station =='lyc':
        inclination = inclination_lyc[year]
    elif station == 'kir':
        inclination = inclination_kir[year]
    elif station =='abk':
        inclination = inclination_abk[year]
    elif station =='brw':
        inclination = inclination_brw[year]
    elif station == 'blc':
        inclination = inclination_blc[year]
    elif station =='cbb':
        inclination = inclination_cbb[year]
    elif station =='hrn':
        inclination = inclination_hrn[year]

    plt.scatter(inclination, np.nanmean(std_Z))
    if np.nanmean(std_Z) > max_y: max_y = np.nanmean(std_Z)
    plt.annotate(station.upper(), # Text
                  (inclination, np.nanmean(std_Z)), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center') # horizontal alignment can be left, right or center
    plt.ylim([0, max_y + 0.02])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/Average Standard Deviation of dB.dt(Z) in function of the inclination.png', dpi=300, bbox_inches='tight')
plt.show()

max_y = 0
plt.figure(dpi=300)
plt.title('Average Standard Deviation of dB/dt(H) in function of the inclination\n' + month + ' - ' + year, fontsize=10)
plt.xlabel('Inclination (°)')
for station in stations:
    filename = folder + station +  year + extension_hdf
    auroral_index = pd.read_hdf(filename, 'index')
    std_H = list()
    for i in range(0, 43200, 180):
        std_H.append(np.nanstd(auroral_index['Auroral_Index_1_2_H'].iloc[i:i+180]))
    if station =='ups':
        inclination =  inclination_ups[year]
    elif station =='lyc':
        inclination = inclination_lyc[year]
    elif station == 'kir':
        inclination = inclination_kir[year]
    elif station =='abk':
        inclination = inclination_abk[year]

    plt.scatter(inclination, np.nanmean(std_H))
    if np.nanmean(std_H) > max_y: max_y = np.nanmean(std_H)
    plt.annotate(station.upper(), # Text
                  (inclination, np.nanmean(std_H)), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center') # horizontal alignment can be left, right or center
    plt.ylim([0, max_y + 0.02])
    if max_y > 0.2:
        plt.ylim([0, max_y + 0.1])

if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/Average Standard Deviation of dB.dt(H) in function of the inclination.png', dpi=300, bbox_inches='tight')
plt.show()

max_y = 0
plt.figure(dpi=300)
plt.title('Average Standard Deviation of dB/dt(Z/H) in function of the inclination\n' + month + ' - ' + year, fontsize=10)
plt.xlabel('Inclination (°)')
for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station =='ups':
        inclination =  inclination_ups[year]
    elif station =='lyc':
        inclination = inclination_lyc[year]
    elif station == 'kir':
        inclination = inclination_kir[year]
    elif station =='abk':
        inclination = inclination_abk[year]

    plt.scatter(inclination, np.nanmean(standard_deviation['Z/H']))
    if np.nanmean(standard_deviation['Z/H']) > max_y: max_y = np.nanmean(standard_deviation['Z/H'])
    plt.annotate(station.upper(), # Text
                  (inclination, np.nanmean(standard_deviation['Z/H'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center') # horizontal alignment can be left, right or center
    plt.ylim([0, max_y + 0.02])
    if max_y > 0.2:
        plt.ylim([0, max_y + 0.1])

if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/Average Standard Deviation of dB.dt(Z.H) in function of the inclination.png', dpi=300, bbox_inches='tight')
plt.show()


if year == '2020':
    stations = ['nur','ups','lyc','kir','abk','brw','blc', 'cbb', 'hrn']

    max_y = 0
    plt.figure(dpi=300)
    plt.title('Average Standard Deviation of dB/dt(Z) in function of the inclination\n' + month + ' - ' + year, fontsize=10)
    plt.xlabel('Inclination (°)')
    for station in stations:
        filename = folder + station +  year + extension_hdf
        auroral_index = pd.read_hdf(filename, 'index')
        std_Z = list()
        for i in range(0, 43200, 180):
            std_Z.append(np.nanstd(auroral_index['Auroral_Index_1_2_Z'].iloc[i:i+180]))
        if station =='nur':
            inclination =  inclination_nur[year]
        elif station =='ups':
            inclination =  inclination_ups[year]
        elif station =='lyc':
            inclination = inclination_lyc[year]
        elif station == 'kir':
            inclination = inclination_kir[year]
        elif station =='abk':
            inclination = inclination_abk[year]
        elif station =='brw':
            inclination = inclination_brw[year]
        elif station == 'blc':
            inclination = inclination_blc[year]
        elif station =='cbb':
            inclination = inclination_cbb[year]
        elif station =='hrn':
            inclination = inclination_hrn[year]

        plt.scatter(inclination, np.nanmean(std_Z))
        if np.nanmean(std_Z) > max_y: max_y = np.nanmean(std_Z)
        plt.annotate(station.upper(), # Text
                      (inclination, np.nanmean(std_Z)), # these are the coordinates to position the label
                      textcoords="offset points", # how to position the text
                      xytext=(0,5), # distance from text to points (x,y)
                      ha='center') # horizontal alignment can be left, right or center
        plt.ylim([0, max_y + 0.02])
    if save:
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/9 stations/Average Standard Deviation of dB.dt(Z) in function of the inclination.png', dpi=300, bbox_inches='tight')
    plt.show()

    max_y = 0
    plt.figure(dpi=300)
    plt.title('Average Standard Deviation of dB/dt(H) in function of the inclination\n' + month + ' - ' + year, fontsize=10)
    plt.xlabel('Inclination (°)')
    for station in stations:
        filename = folder + station +  year + extension_hdf
        auroral_index = pd.read_hdf(filename, 'index')
        std_H = list()
        for i in range(0, 43200, 180):
            std_H.append(np.nanstd(auroral_index['Auroral_Index_1_2_H'].iloc[i:i+180]))
        if station =='nur':
            inclination =  inclination_nur[year]
        elif station =='ups':
            inclination =  inclination_ups[year]
        elif station =='lyc':
            inclination = inclination_lyc[year]
        elif station == 'kir':
            inclination = inclination_kir[year]
        elif station =='abk':
            inclination = inclination_abk[year]
        elif station =='brw':
            inclination = inclination_brw[year]
        elif station == 'blc':
            inclination = inclination_blc[year]
        elif station =='cbb':
            inclination = inclination_cbb[year]
        elif station =='hrn':
            inclination = inclination_hrn[year]

        plt.scatter(inclination, np.nanmean(std_H))
        if np.nanmean(std_H) > max_y: max_y = np.nanmean(std_H)
        plt.annotate(station.upper(), # Text
                      (inclination, np.nanmean(std_H)), # these are the coordinates to position the label
                      textcoords="offset points", # how to position the text
                      xytext=(0,5), # distance from text to points (x,y)
                      ha='center') # horizontal alignment can be left, right or center
        plt.ylim([0, max_y + 0.02])
        if max_y > 0.2:
            plt.ylim([0, max_y + 0.1])

    if save:
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/9 stations/Average Standard Deviation of dB.dt(H) in function of the inclination.png', dpi=300, bbox_inches='tight')
    plt.show()

    max_y = 0
    plt.figure(dpi=300)
    plt.title('Average Standard Deviation of dB/dt(Z/H) in function of the inclination\n' + month + ' - ' + year, fontsize=10)
    plt.xlabel('Inclination (°)')
    for station in stations:
        filename = folder + station +  year + extension_hdf
        standard_deviation = pd.read_hdf(filename, 'std')
        if station =='nur':
            inclination =  inclination_nur[year]
        elif station =='ups':
            inclination =  inclination_ups[year]
        elif station =='lyc':
            inclination = inclination_lyc[year]
        elif station == 'kir':
            inclination = inclination_kir[year]
        elif station =='abk':
            inclination = inclination_abk[year]
        elif station =='brw':
            inclination = inclination_brw[year]
        elif station == 'blc':
            inclination = inclination_blc[year]
        elif station =='cbb':
            inclination = inclination_cbb[year]
        elif station =='hrn':
            inclination = inclination_hrn[year]

        plt.scatter(inclination, np.nanmean(standard_deviation['Z/H']))
        if np.nanmean(standard_deviation['Z/H']) > max_y: max_y = np.nanmean(standard_deviation['Z/H'])
        plt.annotate(station.upper(), # Text
                      (inclination, np.nanmean(standard_deviation['Z/H'])), # these are the coordinates to position the label
                      textcoords="offset points", # how to position the text
                      xytext=(0,5), # distance from text to points (x,y)
                      ha='center') # horizontal alignment can be left, right or center
        plt.ylim([0, max_y + 0.02])
        if max_y > 0.2:
            plt.ylim([0, max_y + 0.1])

    if save:
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Standard Deviation/' + year + '/9 stations/Average Standard Deviation of dB.dt(Z.H) in function of the inclination.png', dpi=300, bbox_inches='tight')
    plt.show()
