# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:12:53 2021
@author: Bastien Longeon
"""
import pandas as pd     # pandas is for reading file
import numpy as np      # instead of math to convert X,Y <--> H,D
import modules.plotter as plotter
import modules.global_graph as gb
import time
startTime = time.time()
gb.initialize()

# colnumber = [(31, 40),   # X [nT]
#               (41, 50),   # Y [nT]
#               (51, 60)]   # Z [nT]
station = 'KIR'
columnx = station + '_X'
columny = station + '_Y'
columnz = station + '_Z'
columnh = station + '_H'
# colnames = [columnx, columny, columnz]
folder = 'maggraphs/'
station_dec = 'kir20'
year = '19'
# extension_sec = '09dsec.sec'
extension_hdf = '09sec.hdf5'
filename = folder + station_dec + year + extension_hdf # Corresponds to the path + filename

for i in range(0,30,1):
    print('Processing data for the {} of september 20{}'.format(i+1, year))
    magdata = pd.read_hdf(filename, start=i*86400, stop=(i+1)*86400)
    magdata[columnh] = np.sqrt(magdata[columnx]*magdata[columnx] + magdata[columny]*magdata[columny])
    magdata['hour'] = np.linspace(0,24,86400)
    plotter.plot_1D(magdata, columnx, 'X component of the magnetic field', 'Time in hours', '[nT]')
    plotter.plot_1D(magdata, columny, 'Y component of the magnetic field', 'Time in hours', '[nT]')
    plotter.plot_1D(magdata, columnz, 'Z component of the magnetic field', 'Time in hours', '[nT]')
    plotter.plot_1D(magdata, columnh, 'H component of the magnetic field', 'Time in hours', '[nT]')

            ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))


