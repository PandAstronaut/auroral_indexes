# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:37:49 2021
@author: Bastien Longeon

This code is used to convert the .sec data in .hdf5.
The .hdf5 is read aproximately 150 times faster by panda than a standard .txt
file (.sec is equivalent to txt).
"""
import pandas as pd     # pandas is for reading file
import numpy as np      # instead of math to convert X,Y <--> H,D
import modules.auroral_index_functions as aur
# import os.path
import time
startTime = time.time()

colnumber = [(31, 40),   # X [nT]
              (41, 50),   # Y [nT]
              (51, 60)]   # Z [nT]

station = 'brw'
columnx = station.upper() + '_X'
columny = station.upper() + '_Y'
columnz = station.upper() + '_Z'
columnh = station.upper() + '_H'
colnames = [columnx, columny, columnz]
folder = 'maggraphs/'
subfolder ='sec files/'
extension_sec = '.sec'
# extension_sec2 = 'qsec.sec'
extension_hdf = '09sec.hdf5'
auroral_index = pd.DataFrame()

iterations = 0
for year in range(2011,2012): # Year: 2011 to 2021
    magdata_month = pd.DataFrame() # These two DF will be the ones used to create the HDF5 file
    auroral_index_month = pd.DataFrame()
    filename = folder + station + str(year) + extension_hdf # Corresponds to the path + filename
    for i in range(0,30):
        if i < 9: day = '0' + str(i+1)
        else : day = str(i+1)
        date = str(year) + '.09.' + day
        print('Processing data for the {}'.format(date))
        filePath = folder + subfolder + station + str(year) + '09' + day + extension_sec
        # if os.path.exists(filePath) == False : filePath = folder + subfolder + station + str(year) + '09' +  day + extension_sec2
        with open(filePath, 'r') as file: #Determination of the number of rows to skip before the datas
            comments_size = 0
            for row in file:
                comments_size += 1
                if "DATE" in row: #the >50 is here to avoid reading the whole documents
                    break
                if comments_size > 50:
                    print("The end of the header has not been found.")
                    break
            file.close()
        magdata = pd.read_fwf(filePath, skiprows=comments_size ,colspecs=colnumber, names=colnames)
        magdata[columnx].replace(to_replace= 99999.0, value=np.nan, inplace=True)
        magdata[columny].replace(to_replace= 99999.0, value=np.nan, inplace=True)
        magdata[columnz].replace(to_replace= 99999.0, value=np.nan, inplace=True)
        for j in range(0,86400):
            if magdata[columnx].iloc[j] > 20000:
                magdata[columnx].iloc[j] = np.nan
            if abs(magdata[columny].iloc[j]) > 5000:
                magdata[columny].iloc[j] = np.nan
            if magdata[columnz].iloc[j] > 150000:
                magdata[columnz].iloc[j] = np.nan
        magdata[columnh] = np.sqrt(magdata[columnx]*magdata[columnx] + magdata[columny]*magdata[columny])
        magdata_month = magdata_month.append(magdata)
        # magdata.to_hdf(filename, 'data', mode='w')
        ####              Auroral Index 1              ####
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
        auroral_index['Auroral_Index_1_2_X'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_2_Y'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_1_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_2_X'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_2_Y'].replace(to_replace=0, value=np.nan, inplace=True)
        auroral_index['Auroral_Index_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)

                        ###              Auroral Index 1.2: Z/X Z/Y              ####
        auroral_index['Auroral_Index_1_2_Z/X'] = np.sign(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_X'])*np.log10(abs(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_X']))
        auroral_index['Auroral_Index_1_2_Z/Y'] = np.sign(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_Y'])*np.log10(abs(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_Y']))

        ###              (Auroral Index 2: Z/X and Z/Y)             ####
        auroral_index['DC_ratio_X'] = np.sign(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_X'])*np.log10(abs(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_X']))
        auroral_index['DC_ratio_Y'] = np.sign(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_Y'])*np.log10(abs(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_Y']))

        ###              (dB/dt)/(<dB_1sec>_1min)             ####
        auroral_index['AC_ratio'] = abs(auroral_index['Auroral_Index_1_1_H'])/auroral_index['Auroral_Index_1_2_H']
        # auroral_index.to_hdf(filename, 'index', mode='a')
        auroral_index_month = auroral_index_month.append(auroral_index)

    iterations += 1
    executionTime = (time.time() - startTime)
    if year != 2020:    print('----    Estimated remaining time: {0:.0f}s   ----'.format((executionTime/iterations)*(2020-year)))

    magdata_month.to_hdf(filename, 'data', mode='w')
    auroral_index_month.to_hdf(filename, 'index', mode='a')
                ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
