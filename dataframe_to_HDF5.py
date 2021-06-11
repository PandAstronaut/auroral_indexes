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
station_dec = 'kir20'
extension_sec = '09dsec.sec'
extension_hdf = '09sec.hdf5'

for i in range(11,21):
    print('---- Processing data for september 20{} ----'.format(i))
    filePath = folder + station_dec + str(i) + extension_sec
    filename = folder + station_dec + str(i) + extension_hdf # Corresponds to the path + filename
    magdata = pd.read_fwf(filePath, colspecs=colnumber, names=colnames)
    magdata[columnh] = np.sqrt(magdata[columnx]*magdata[columnx] + magdata[columny]*magdata[columny])
    for i in range(0,2592000):
        if magdata[columnx].iloc[i] > 50000:
            magdata[columnx].iloc[i] = np.nan
        if magdata[columny].iloc[i] > 10000:
            magdata[columny].iloc[i] = np.na
        if magdata[columnz].iloc[i] > 80000:
            magdata[columnz].iloc[i] = np.nan
        if magdata[columnh].iloc[i] > 30000:
            magdata[columnh].iloc[i] = np.nan
    magdata.to_hdf(filename, 'data', mode='w') # 'data' is the key used to access the data in the .hdf5


                ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
