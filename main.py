# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:05:11 2021
@author: Bastien Longeon

This code plots:
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

startTime = time.time()
###              Define the filenames to read              ####
folder = "maggraphs/"
filename = "kir201709dsec.sec" # d = definitive
filePath = folder + filename

###              Format of the file we read              ####
#--IAGA2002---*----2----*----3----*----4----*----5----*----6----*----7
#DATE       TIME         DOY     ***X      ***Y      ***Z      ***F   |
#YYY-MM-DD hh:mm:ss:000 DOY     *****.**  *****.**  *****.**  *****.**
#---*----1----*----2----*----3----*----4----*----5----*----6----*----7

#The tuples in colnumber are the interval in wich we can find the information
#linked in the commentary next to each
colnumber = [(0, 4),     # Year (4 digit)
             (5, 7),     # Month 01 ... 12
             (8, 10),    # Day 01 ... 31
             (11, 13),   # Hour 00 ... 23
             (14, 16),   # Minute 00 ... 59
             (17, 19),   # Second 00 ... 59
             (24, 26),   # Day 000 ... 366
             (31, 40),   # X [nT]
             (41, 50),   # Y [nT]
             (51, 60),   # Z [nT]
             (61, 70)]   # F [nT]

#Creation of the column names for the DataFrame
station_code = filename[0:3].upper()
columnx = station_code + '_X'
columny = station_code + '_Y'
columnz = station_code + '_Z'
columnh = station_code + '_H'
columnf = station_code + '_F'
colnames = ['year', 'month', 'day', 'hr', 'min', 'sec', 'DOY', columnx, columny, columnz, columnf]

"86400s in a day"

                ###              Creation of the DataFramefor the day              ####
for i in range(0,2):
    magdata = pd.read_fwf(filePath, colspecs=colnumber, names=colnames, skiprows = 86400*i, nrows = 86400*(i+1))
    magdata[columnh] = np.sqrt(magdata[columnx]*magdata[columnx] + magdata[columny]*magdata[columny])
    del magdata


                ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
