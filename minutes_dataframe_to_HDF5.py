# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:59:45 2021
@author: Bastien Longeon
"""
import pandas as pd     # pandas is for reading file
import numpy as np      # instead of math to convert X,Y <--> H,D
import modules.auroral_index_functions as aur
import time
startTime = time.time()

stations = ['kir','abk','ups','brw','cbb','blc','lyc', 'nur', 'hrn']
folder = 'maggraphs/'
extension_hdf = '09min.hdf5'
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
    filename = folder + station + str(year) + extension_hdf # Corresponds to the path + filename
    magdata = pd.read_hdf(filename, 'data')
    ###              Auroral Index 1              ###
    auroral_index['Auroral_Index_1_1_X'] = aur.auroral_index1_min(magdata, columnx)
    auroral_index['Auroral_Index_1_1_Y'] = aur.auroral_index1_min(magdata, columny)
    auroral_index['Auroral_Index_1_1_Z'] = aur.auroral_index1_min(magdata, columnz)


    # These replacements avoid log10(0) or inf errors without modifying the plots
    auroral_index['Auroral_Index_1_X'].replace(to_replace=0, value=np.nan, inplace=True)
    auroral_index['Auroral_Index_1_Y'].replace(to_replace=0, value=np.nan, inplace=True)
    auroral_index['Auroral_Index_1_Z'].replace(to_replace=0, value=np.nan, inplace=True)


    ###              Auroral Index 1.2: Z/X Z/Y              ###
    auroral_index['Auroral_Index_1_Z/X'] = np.sign(auroral_index['Auroral_Index_1_Z']/auroral_index['Auroral_Index_1_X'])*np.log10(abs(auroral_index['Auroral_Index_1_Z']/auroral_index['Auroral_Index_1_X']))
    auroral_index['Auroral_Index_1_Z/Y'] = np.sign(auroral_index['Auroral_Index_1_Z']/auroral_index['Auroral_Index_1_Y'])*np.log10(abs(auroral_index['Auroral_Index_1_Z']/auroral_index['Auroral_Index_1_Y']))
    
    auroral_index.to_hdf(filename, 'index', mode='a')

    magdata.to_hdf(filename, 'data', mode='a')

station_iteration += 1

            ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))