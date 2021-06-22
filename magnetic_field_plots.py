# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:12:53 2021
@author: Bastien Longeon
"""
import pandas as pd     # pandas is for reading file
import numpy as np      # instead of math to convert X,Y <--> H,D
import modules.plotter as plotter
import modules.global_graph as gb
import os.path
import time
startTime = time.time()
gb.initialize()

colnumber = [(31, 40),   # X [nT]
              (41, 50),   # Y [nT]
              (51, 60)]   # Z [nT]
station = 'CBB'
columnx = station + '_X'
columny = station + '_Y'
columnz = station + '_Z'
columnh = station + '_H'
colnames = [columnx, columny, columnz]
folder = 'maggraphs/sec files/'
station_dec = 'kir20'
year = '2009'
extension_sec = 'psec.sec'
extension_sec2 = 'qsec.sec'
# extension_hdf = '09sec.hdf5'
for i in range(0,30):
    if i < 9: day = '0' + str(i+1)
    else : day = str(i+1)
    filename = folder + station_dec + year + day + extension_sec # Corresponds to the path + filename
    if os.path.exists(filename) == False : filename = folder + station_dec + year + day + extension_sec2
    with open(filename, 'r') as file: #Determination of the number of rows to skip before the datas
        comments_size = 0
        for row in file:
            comments_size += 1
            if "DATE" in row: #the >50 is here to avoid reading the whole documents
                break
            if comments_size > 50:
                print("The end of the header has not been found.")
                break

    # print('Processing data for the {} of september 20{}'.format(i+1, year))

    magdata = pd.read_fwf(filename, skiprows=comments_size, colspecs=colnumber, names=colnames)
    magdata[columnh] = np.sqrt(magdata[columnx]*magdata[columnx] + magdata[columny]*magdata[columny])
    magdata['hour'] = np.linspace(0,24,86400)
    plotter.plot_1D(magdata, columnx, 'X component of the magnetic field\n' + day, 'Time in hours', '[nT]')
    plotter.plot_1D(magdata, columny, 'Y component of the magnetic field\n' + day, 'Time in hours', '[nT]')
    plotter.plot_1D(magdata, columnz, 'Z component of the magnetic field\n' + day, 'Time in hours', '[nT]')
    plotter.plot_1D(magdata, columnh, 'H component of the magnetic field\n' + day, 'Time in hours', '[nT]')

            ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))


