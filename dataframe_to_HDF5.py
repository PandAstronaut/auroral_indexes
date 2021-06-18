# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:37:49 2021
@author: Bastien Longeon

This code is used to convert the .sec data in .hdf5.
The .hdf5 is read aproximately 150 times faster by panda than a standard .txt
file (.sec is equivalent to txt).

This code can be upgraded by making it capable to convert the entirety of the
data files used for sec, min, hour and every station.
"""
import pandas as pd     # pandas is for reading file
import numpy as np      # instead of math to convert X,Y <--> H,D
import modules.auroral_index_functions as aur
import time
startTime = time.time()

colnumber = [(31, 40),   # X [nT]
              (41, 50),   # Y [nT]
              (51, 60)]   # Z [nT]

station = 'KIR'
columnx = station + '_X'
columny = station + '_Y'
columnz = station + '_Z'
columnh = station + '_H'
colnames = [columnx, columny, columnz]
folder = 'maggraphs/'
subfolder ='sec files/'
station = 'kir'
extension_sec = '09dsec.sec'
extension_hdf = '09sec.hdf5'
auroral_index = pd.DataFrame()

for year in range(2017,2018): # Year: 11 to 21
    print('----     Reading data from september {}    ----'.format(year))
    filePath = folder + subfolder + station + str(year) + extension_sec
    filename = folder + station + str(year) + extension_hdf # Corresponds to the path + filename
    magdata = pd.read_fwf(filePath, colspecs=colnumber, names=colnames)
    print('----           Removing errors               ----')
    magdata[columnx].replace(to_replace= 99999.0, value=np.nan, inplace=True)
    magdata[columny].replace(to_replace= 99999.0, value=np.nan, inplace=True)
    magdata[columnz].replace(to_replace= 99999.0, value=np.nan, inplace=True)
    magdata[columnh] = np.sqrt(magdata[columnx]*magdata[columnx] + magdata[columny]*magdata[columny])
    print('----           Correcting anomalies          ----')
    anomalies = 0
    for j in range(0,2592000):
        if magdata[columnx].iloc[j] > 30000:
            magdata[columnx].iloc[j] = np.nan
            anomalies += 1
        if magdata[columny].iloc[j] > 1000:
            magdata[columny].iloc[j] = np.nan
            anomalies += 1
        if magdata[columnz].iloc[j] > 70000:
            magdata[columnz].iloc[j] = np.nan
            anomalies += 1
        if magdata[columnh].iloc[j] > 30000:
            magdata[columnh].iloc[j] = np.nan
            anomalies += 1
    print('----   {} anomalies detected and corrected   ----'.format(anomalies))
    magdata.to_hdf(filename, 'data', mode='w')

    ###              Auroral Index 1              ####
    auroral_index['Auroral_Index_1_1_Z'] = aur.auroral_index1_1(magdata, 'KIR_Z')
    auroral_index['Auroral_Index_1_1_H'] = aur.auroral_index1_1(magdata, 'KIR_H')
    auroral_index['Auroral_Index_1_2_X'] = aur.auroral_index1_2(magdata, 'KIR_X')
    auroral_index['Auroral_Index_1_2_Y'] = aur.auroral_index1_2(magdata, 'KIR_Y')
    auroral_index['Auroral_Index_1_2_Z'] = aur.auroral_index1_2(magdata, 'KIR_Z')
    auroral_index['Auroral_Index_1_2_H'] = aur.auroral_index1_2(magdata, 'KIR_H')

                    ###              Auroral Index 2              ###
    auroral_index['Auroral_Index_2_X'] = aur.auroral_index2(magdata, 'KIR_X', year)
    auroral_index['Auroral_Index_2_Y'] = aur.auroral_index2(magdata, 'KIR_Y', year)
    auroral_index['Auroral_Index_2_Z'] = aur.auroral_index2(magdata, 'KIR_Z', year)
    auroral_index['Auroral_Index_2_H'] = aur.auroral_index2(magdata, 'KIR_H', year)

                    ###              Auroral Index 1.2: Z/X Z/Y              ####
    auroral_index['Auroral_Index_1_2_Z/X'] = auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_X']
    auroral_index['Auroral_Index_1_2_Z/Y'] = auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_Y']

    ###              (Auroral Index 2: Z/X and Z/Y)             ####
    auroral_index['DC_ratio_X'] = np.sign(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_X'])*np.log10(abs(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_X']))
    auroral_index['DC_ratio_Y'] = np.sign(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_Y'])*np.log10(abs(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_Y']))

    ###              (dB/dt)/(<dB_1sec>_1min)             ####
    auroral_index['AC_ratio'] = abs(auroral_index['Auroral_Index_1_1_H'])/auroral_index['Auroral_Index_1_2_H']

    auroral_index.to_hdf(filename, 'index', mode='a')

    executionTime = (time.time() - startTime)
    if year != 2020:    print('----    Estimated emaining time: {0:.0f}s   ----'.format((executionTime/(year-10))*(20-year)))

                ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))


