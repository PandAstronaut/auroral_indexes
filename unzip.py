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

# =============================================================================
# Unziping the folders contained in Téléchargements and sending the .gz in the
# to_unzip folder.
# =============================================================================

path = 'D:/Users/User/Downloads/'
files = os.listdir(path)
iterations = 0
for f in files:
    if f.endswith('.zip'):
        iterations += 1
        zipfile.ZipFile(path + f).extractall('D:/Documents/GitHub/auroral_indexes/to_unzip')
print('{} files extracted'.format(iterations))

colnumber = [(31, 40),   # X [nT]
             (41, 50),   # Y [nT]
             (51, 60)]   # Z [nT]
stations = ['ded','ykc','ott','stj','frd']


source_folder = 'to_unzip/'
folder = 'maggraphs/'
extension_sec = 'vsec.sec.gz'
extension_sec2 = 'psec.sec.gz'
extension_sec3 = 'qsec.sec.gz'
extension_sec4 = 'dsec.sec.gz'
extension_hdf = 'sec.hdf5'
month = '09'

# extension_hdf_min = '09min.hdf5'

# extension_min = 'qmin.min.gz'
# extension_min2 = 'vmin.min.gz'
# extension_min3 = 'pmin.min.gz'
# extension_min4 = 'dmin.min.gz'


# =============================================================================
# Unzipping the .gz contained in the to_unzip folder and directly turning them
# into hdf5 data.
# =============================================================================

for station in stations:
    columnx = station.upper() + '_X'
    columny = station.upper() + '_Y'
    columnz = station.upper() + '_Z'
    columnh = station.upper() + '_H'
    colnames = [columnx, columny, columnz]
    if station == 'blc' or station == 'cbb' or station == 'res' or station == 'fcc' or station == 'iqa' or station == 'stj'or station == 'ott' or station == 'ykc': comments_size = 21
    elif station == 'brw' or station == 'cmo' or station == 'shu' or station == 'sit' or station == 'frd' or station == 'ded': comments_size = 16
    else: comments_size = 22
    for year in range(2020,2021): # Year: 2011 to 2021
        magdata_month = pd.DataFrame() # This DF will be the ones used to create the HDF5 file
        filename = folder + station + str(year) + month + extension_hdf # Corresponds to the path + filename
        print('Processing data from {} in {}'.format(year,station))
        for i in range(0,30):
            if i < 9: day = '0' + str(i+1)
            else : day = str(i+1)
            date = str(year) + '.' + month + '.' + day
            filePath = source_folder + station + str(year) + month + day + extension_sec
            if os.path.exists(filePath) == False : filePath = source_folder + station.lower() + str(year) + month +  day + extension_sec2
            if os.path.exists(filePath) == False : filePath = source_folder + station.lower() + str(year) + month +  day + extension_sec3
            if os.path.exists(filePath) == False : filePath = source_folder + station.lower() + str(year) + month +  day + extension_sec4
            with gzip.open(filePath) as file:
                magdata = pd.read_fwf(file, skiprows=comments_size ,colspecs=colnumber, names=colnames)
                file.close()
                magdata[columnx].replace(to_replace= 99999.0, value=np.nan, inplace=True)
                magdata[columny].replace(to_replace= 99999.0, value=np.nan, inplace=True)
                magdata[columnz].replace(to_replace= 99999.0, value=np.nan, inplace=True)
                magdata[columnh] = np.sqrt(magdata[columnx]*magdata[columnx] + magdata[columny]*magdata[columny])
                magdata_month = magdata_month.append(magdata)
    magdata_month.to_hdf(filename, 'data', mode='w')

# Clears the to_unzip folder
for root, dirs, files in os.walk(source_folder):
    for file in files:
        os.remove(os.path.join(root, file))

                ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
