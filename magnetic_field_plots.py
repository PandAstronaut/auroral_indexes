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

folder = "maggraphs/"
station = 'lyc'
if station == 'kir': station_name = 'Kiruna'
elif station == 'cbb': station_name = 'Cambridge Bay'
elif station =='abk': station_name = 'Abisko'
elif station =='blc': station_name = 'Baker Lake'
elif station =='ups': station_name = 'Uppsala'
elif station =='brw': station_name = 'Barrow'
elif station =='lyc': station_name = 'Lycksele'
year = 2020
extension_hdf = '09sec.hdf5'

columnx = station.upper() + '_X'
columny = station.upper() + '_Y'
columnz = station.upper() + '_Z'
columnh = station.upper() + '_H'

for i in range(0,6):
    if i < 9: day = '0' + str(i+1)
    else : day = str(i+1)
    date = str(year) + '.09.' + day
    filename = folder + station + str(year) + extension_hdf

    magdata = pd.read_hdf(filename, 'data', start=i*86400, stop=(i+1)*86400)
    magdata['hour'] = np.linspace(0,24,86400)
    plotter.plot_1D(magdata, columnx, 'X component of the magnetic field\n' + station_name + ' - ' + date, 'Time in hours', '[nT]')
    plotter.plot_1D(magdata, columny, 'Y component of the magnetic field\n' + station_name + ' - ' + date, 'Time in hours', '[nT]')
    plotter.plot_1D(magdata, columnz, 'Z component of the magnetic field\n'+ station_name + ' - ' + date, 'Time in hours', '[nT]')
    plotter.plot_1D(magdata, columnh, 'H component of the magnetic field\n'+ station_name + ' - ' + date, 'Time in hours', '[nT]')

            ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))


