# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:27:33 2021
@author: Bastien Longeon
This code will unzip all the folders containing the .sec.gz files and extract
all the .gz files to the maggraphs/sec files/ folder. It will also convert the
raw data into a first HDF5 file to facilitate the study of the B0 offset and
the next step in dataframe_to_hdf5.py.
"""
import gzip
import pandas as pd
import numpy as np
import os
import zipfile
import time
startTime = time.time()

# path = 'D:/Téléchargements/'
# files = os.listdir(path)
# iterations = 0
# for f in files:
#     if f.endswith('.zip'):
#         iterations += 1
#         zipfile.ZipFile(path + f).extractall('D:/Documents/GitHub/auroral_indexes/to_unzip')
# print('{} files extracted'.format(iterations))

colnumber = [(31, 40),   # X [nT]
             (41, 50),   # Y [nT]
             (51, 60)]   # Z [nT]
stations = ['brw']

source_folder = 'to_unzip/'
folder = 'maggraphs/'
subfolder = 'sec files/'
extension_sec = 'vsec.sec.gz'
extension_sec2 = 'psec.sec.gz'
extension_sec3 = 'qsec.sec.gz'
extension_hdf = '09sec.hdf5'
destination = 'D:/Documents/GitHub/auroral_indexes/maggraphs/sec files/'

for station in stations:
    columnx = station.upper() + '_X'
    columny = station.upper() + '_Y'
    columnz = station.upper() + '_Z'
    columnh = station.upper() + '_H'
    colnames = [columnx, columny, columnz]
    if station == 'brw': comments=21
    for year in range(2018,2021): # Year: 2011 to 2021
        if station == 'ups' and year > 2015 : comments=22
        magdata_month = pd.DataFrame() # These two DF will be the ones used to create the HDF5 file
        filename = folder + station + str(year) + extension_hdf # Corresponds to the path + filename
        print('Processing data from {} in {}'.format(year,station))
        for i in range(0,30):
            if i < 9: day = '0' + str(i+1)
            else : day = str(i+1)
            date = str(year) + '.09.' + day
            filePath = source_folder + station + str(year) + '09' + day + extension_sec
            if os.path.exists(filePath) == False : filePath = source_folder + station.lower() + str(year) + '09' +  day + extension_sec2
            if os.path.exists(filePath) == False : filePath = source_folder + station.lower() + str(year) + '09' +  day + extension_sec3
            # try:
            #     with gzip.open(filePath) as file:
            #         with open(destination + station + str(year) + '09' + day + '.sec', 'wb') as d_file:
            #             while True:
            #                 block = file.read(65536)
            #                 if not block:
            #                     break
            #                 else:
            #                     d_file.write(block)
            #         file.close()
                # It is way faster to read the file while it is still open in the with gzip.open loop
                # This code is like this just because of missing days in BRW data
            # except Exception as e:
            #     print(str(e))
            file = folder + subfolder + station +  str(year) + '09' + day + '.sec'
            magdata = pd.read_fwf(file, skiprows=comments ,colspecs=colnumber, names=colnames)
            magdata[columnx].replace(to_replace= 99999.0, value=np.nan, inplace=True)
            magdata[columny].replace(to_replace= 99999.0, value=np.nan, inplace=True)
            magdata[columnz].replace(to_replace= 99999.0, value=np.nan, inplace=True)
            for j in range(0,86400):
                if abs(magdata[columny].iloc[j]) > 5000:
                    magdata[columny].iloc[j] = np.nan
            magdata[columnh] = np.sqrt(magdata[columnx]*magdata[columnx] + magdata[columny]*magdata[columny])
            magdata_month = magdata_month.append(magdata)
        magdata_month.to_hdf(filename, 'data', mode='w')

                ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
