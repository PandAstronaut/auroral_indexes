# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:05:11 2021
@author: Bastien Longeon

For everyday in september from 2011 to 2020, this code plots:

    · A 4-pannels comparison of the following quotients:
        Graph 1: Auroral index 1.2: Z/H
        Graph 2: Auroral index 2: Z/H
        Graph 3: (Auroral index 2 Z/H) / (Auroral index 1.2 Z/H)
        Graph 4: Auroral index 1.2 and 2: horizontal
            In function of time

    · dBDC in function of dBAC 1 & 2 for the vertical and horizontal component
"""
import pandas as pd     # pandas is for reading file
import numpy as np      # instead of math to convert X,Y <--> H,D
import time

###              Define the file to read              ####
path = "maggraphs/"

colnumber = [(31, 40),   # X [nT]
             (41, 50),   # Y [nT]
             (51, 60)]   # Z [nT]

#Creation of the column names for the DataFrame
station = 'KIR'
columnx = station + '_X'
columny = station + '_Y'
columnz = station + '_Z'
columnh = station + '_H'
colnames = [columnx, columny, columnz]

startTime = time.time()
magdata = pd.read_fwf('maggraphs/kir201709dsec.sec', colspecs=colnumber, names=colnames)
magdata.to_hdf(path +'test', 'test1', mode='w')
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))

startTime = time.time()
new_data = pd.read_hdf(path + 'test')
new_data[columnh] = np.sqrt(new_data[columnx]*new_data[columnx] + new_data[columny]*new_data[columny])
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
