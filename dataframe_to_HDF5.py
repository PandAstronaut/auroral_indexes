# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:37:49 2021
@author: Bastien Longeon

The .hdf5 is read aproximately 150 times faster by pandas than a standard .txt
file (.sec is equivalent to txt).
"""
import pandas as pd     # pandas is for reading file
import numpy as np      # instead of math to convert X,Y <--> H,D
import modules.auroral_index_functions as aur
import time
startTime = time.time()

# stations = ['kir','abk','ups','brw','cbb','blc','lyc', 'nur', 'hrn']
# stations = ['wic','clf','bdv','iqa','sit','fcc','shu','cmo','res']
stations = ['ykc','ott','stj','frd']


folder = 'maggraphs/'
month = '09'
extension_hdf = month + 'sec.hdf5'
auroral_index = pd.DataFrame()

station_iteration = 0
for station in stations:
    executionTime = (time.time() - startTime) # Just to avoid having an error for next line
    if station_iteration != 0: print('----    Estimated remaining time: {0:.0f}s   ----'.format((executionTime/station_iteration)*(len(stations)-station_iteration)))
    columnx = station.upper() + '_X'
    columny = station.upper() + '_Y'
    columnz = station.upper() + '_Z'
    columnh = station.upper() + '_H'
    colnames = [columnx, columny, columnz]
    print('Processing {} data'.format(station.upper()))
    for year in range(2020,2021): # Year: 2011 to 2022
        filename = folder + station + str(year) + extension_hdf # Corresponds to the path + filename
        magdata = pd.read_hdf(filename, 'data')
# =============================================================================
# Auroral Indexes
# =============================================================================
        ##              Auroral Index 1              ###
        auroral_index['Auroral_Index_1_1_X'] = aur.auroral_index1_1(magdata, columnx)
        auroral_index['Auroral_Index_1_1_Y'] = aur.auroral_index1_1(magdata, columny)
        auroral_index['Auroral_Index_1_1_Z'] = aur.auroral_index1_1(magdata, columnz)
        auroral_index['Auroral_Index_1_1_H'] = aur.auroral_index1_1(magdata, columnh)
        auroral_index['Auroral_Index_1_2_X'] = aur.auroral_index1_2(magdata, columnx)
        auroral_index['Auroral_Index_1_2_Y'] = aur.auroral_index1_2(magdata, columny)
        auroral_index['Auroral_Index_1_2_Z'] = aur.auroral_index1_2(magdata, columnz)
        auroral_index['Auroral_Index_1_2_H'] = aur.auroral_index1_2(magdata, columnh)

        ###              Auroral Index 2              ###
        auroral_index['Auroral_Index_2_X'] = aur.auroral_index2(magdata, columnx, year)
        auroral_index['Auroral_Index_2_Y'] = aur.auroral_index2(magdata, columny, year)
        auroral_index['Auroral_Index_2_Z'] = aur.auroral_index2(magdata, columnz, year)
        auroral_index['Auroral_Index_2_H'] = aur.auroral_index2(magdata, columnh, year)

        # These replacements avoid log10(0) or inf errors without modifying the plots
        auroral_index['Auroral_Index_1_1_X'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_1_Y'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_1_Z'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_2_X'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_2_Y'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_2_X'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_2_Y'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)

        ###              Auroral Index 1.2: Z/X Z/Y              ###
        auroral_index['Auroral_Index_1_1_Z/X'] = np.sign(auroral_index['Auroral_Index_1_1_Z']/auroral_index['Auroral_Index_1_1_X'])*np.log10(abs(auroral_index['Auroral_Index_1_1_Z']/auroral_index['Auroral_Index_1_1_X']))
        auroral_index['Auroral_Index_1_1_Z/Y'] = np.sign(auroral_index['Auroral_Index_1_1_Z']/auroral_index['Auroral_Index_1_1_Y'])*np.log10(abs(auroral_index['Auroral_Index_1_1_Z']/auroral_index['Auroral_Index_1_1_Y']))


        ###              Auroral Index 1.2: Z/X Z/Y Z/H          ###
        auroral_index['Auroral_Index_1_2_Z/X'] = np.sign(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_X'])*np.log10(abs(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_X']))
        auroral_index['Auroral_Index_1_2_Z/Y'] = np.sign(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_Y'])*np.log10(abs(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_Y']))
        auroral_index['Auroral_Index_1_2_Z/H'] = np.sign(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_H'])*np.log10(abs(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_H']))


                        ###              (Auroral Index 2: Z/X and Z/Y)             ###
        auroral_index['DC_ratio_X'] = np.sign(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_X'])*np.log10(abs(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_X']))
        auroral_index['DC_ratio_Y'] = np.sign(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_Y'])*np.log10(abs(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_Y']))

        ###              (dB/dt)/(<dB_1sec>_1min)             ###
        auroral_index['AC_ratio'] = abs(auroral_index['Auroral_Index_1_1_H'])/auroral_index['Auroral_Index_1_2_H']
        auroral_index.to_hdf(filename, 'index', mode='a')

# =============================================================================
#       Magnetic field inclination
# =============================================================================
        inclination = pd.DataFrame()
        magdata['angle'] = (np.arctan(magdata[columnz]/magdata[columnh])*180)/np.pi
        inclination['Index_1_1'] = aur.auroral_index1_1(magdata, 'angle')
        inclination['Index_1_2'] = aur.auroral_index1_2(magdata, 'angle')
        magdata.to_hdf(filename, 'data', mode='a')
        inclination.to_hdf(filename, 'angle', mode='a')

# =============================================================================
#         Standard deviation
# =============================================================================
        # magdata = pd.read_hdf(filename, 'data')
        # auroral_index = pd.read_hdf(filename, 'index')
        # inclination = pd.read_hdf(filename, 'angle')
        standard_deviation = pd.DataFrame()
        std_X = list()
        std_Y = list()
        std_H = list()
        std_angle = list()
        std_angle_derivative = list()
        max1 = 43200
        max2 = 2592000
        if year == 2021:
            max1 = 44640
            max2 = 2678400
        for i in range(0, max1, 180):
            std_X.append(np.nanstd(auroral_index['Auroral_Index_1_2_Z/X'].iloc[i:i+180]))
            std_Y.append(np.nanstd(auroral_index['Auroral_Index_1_2_Z/Y'].iloc[i:i+180]))
            std_H.append(np.nanstd(auroral_index['Auroral_Index_1_2_Z/H'].iloc[i:i+180]))
            std_angle_derivative.append(np.nanstd(inclination['Index_1_2'].iloc[i:i+180]))
        for i in range(0, max2, 10800):
            std_angle.append(np.nanstd(magdata['angle'].iloc[i:i+10799]))
        standard_deviation['Z/X'] = std_X
        standard_deviation['Z/Y'] = std_Y
        standard_deviation['Z/H'] = std_H
        standard_deviation['angle'] = std_angle
        standard_deviation['dI/dt'] = std_angle_derivative

        standard_deviation.to_hdf(filename, 'std', mode='a')

        station_iteration += 1

                ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
