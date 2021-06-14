# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:16:00 2021
@author: Bastien Longeon
"""
import pandas as pd     # pandas is for reading file
import numpy as np      # instead of math to convert X,Y <--> H,D
import modules.plotter as plotter
import modules.auroral_index_functions as aur
import modules.global_graph as gb
import time
startTime = time.time()
gb.initialize()

###              Define the filenames to read              ####
folder = "maggraphs/"
filename = "kir20170908dsec.sec" # d = definitive
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
             (31, 40),   # X [nT] or H [minutes of arc]
             (41, 50),   # Y [nT] or D [minutes of arc]
             (51, 60),   # Z [nT] or I [minutes of arc]
             (61, 70)]   # F [nT]


#Creation of the column names for the DataFrame
station_code = filename[0:3].upper()
columnx = station_code + '_X'
columny = station_code + '_Y'
columnz = station_code + '_Z'
columnf = station_code + '_F'
columnh = station_code + '_H'
columnd = station_code + '_D'
columni = station_code + '_I'
colnames = ['year', 'month', 'day', 'hr', 'min', 'sec', 'DOY', columnx, columny, columnz, columnf]

"""
DOY: day of year from 1 to 365
Bt = B total (absolute value)
HDI:
H = horizontal
D = angle east-west
I = anglel toward -z
"""

                    ###              BH vs Bz              ####
magdata = pd.read_fwf(filePath, colspecs=colnumber, names=colnames)
magdata[columnh] = np.sqrt(magdata[columnx]*magdata[columnx] + magdata[columny]*magdata[columny])

# This new list is necessary to plot the data properly with one value in 'hour'
# corresponding to one value of B
magdata['hour'] = (magdata['hr']*3600 + magdata['min']*60 + magdata['sec'])/3600

plotter.plot_1D(magdata, columnh, 'Horizontal component of the magnetic field - 2017/09/08', 'Time in hours', '[nT]')
plotter.plot_1D(magdata, columnz, 'Vertical component of the magnetic field - 2017/09/08', 'Time in hours', '[nT]')

                ###              Auroral Indexes              ####
auroral_index = pd.DataFrame() #Creation of the DataFrame that will store the auroral indexes
# This new list is necessary to plot the data properly with one value in 'hour'
# corresponding to one value of B
auroral_index['hour'] = np.linspace(0, 24, 1440)

                ###              Auroral Index 1              ####
auroral_index['Auroral_Index_1_1_H'] = aur.auroral_index1_1(magdata, 'KIR_H')
auroral_index['Auroral_Index_1_2_H'] = aur.auroral_index1_2(magdata, 'KIR_H')
auroral_index['Auroral_Index_1_1_Z'] = aur.auroral_index1_1(magdata, 'KIR_Z')
auroral_index['Auroral_Index_1_2_Z'] = aur.auroral_index1_2(magdata, 'KIR_Z')

plotter.plot_1D(auroral_index,'Auroral_Index_1_1_H', 'Horizontal Auroral Index 1(1) - 2017/09/08', 'Time in hours', '[nT]')
plotter.plot_1D(auroral_index,'Auroral_Index_1_1_Z', 'Vertical Auroral Index 1(1) - 2017/09/08', 'Time in hours', '[nT]')
plotter.plot_1D(auroral_index,'Auroral_Index_1_2_H', 'Horizontal Auroral Index 1(2) - 2017/09/08', 'Time in hours', '[nT]', 'upper right')
plotter.plot_1D(auroral_index,'Auroral_Index_1_2_Z', 'Vertical Auroral Index 1(2) - 2017/09/08', 'Time in hours','[nT]')

                ###              Auroral Index 2              ####
auroral_index['Auroral_Index_2_H'] = aur.auroral_index2(magdata, 'KIR_H', 2017)
auroral_index['Auroral_Index_2_Z'] = aur.auroral_index2(magdata, 'KIR_Z', 2017)

plotter.plot_1D(auroral_index,'Auroral_Index_2_H' , 'Horizontal Auroral Index 2 - 2017/09/08', 'Time in hours','[nT]')
plotter.plot_1D(auroral_index,'Auroral_Index_2_Z' , 'Vertical Auroral Index 2 - 2017/09/08', 'Time in hours','[nT]')

                ###              2D Plot              ####
plotter.plot_2D(auroral_index, 'Auroral_Index_1_1_H', 'Auroral_Index_2_H', 'Auroral_Index_1_2_H',
                'Auroral_Index_2_H', 'Horizontal Auroral index 2 = f(Auroral index 1(1) & 1(2))',
                '[nT]','[nT]', mark = True)
plotter.plot_2D(auroral_index, 'Auroral_Index_1_1_Z', 'Auroral_Index_2_Z', 'Auroral_Index_1_2_Z',
                'Auroral_Index_2_Z', 'Vertical Auroral index 2 = f(Auroral index 1(1) & 1(2))',
                '[nT]','[nT]', location = 'lower left', mark = True)

distribution1 = plotter.plot_2D_scatter(auroral_index, 'Auroral_Index_1_1_H', 'Auroral_Index_2_H', 'Auroral_Index_1_2_H',
                'Auroral_Index_2_H', 'Horizontal Auroral index 2 = f(Auroral index 1(1) & 1(2))',
                '[nT]','log(dB) [nT]')
distribution2 = plotter.plot_2D_scatter(auroral_index, 'Auroral_Index_1_1_Z', 'Auroral_Index_2_Z', 'Auroral_Index_1_2_Z',
                'Auroral_Index_2_Z', 'Vertical Auroral index 2 = f(Auroral index 1(1) & 1(2))',
                '[nT]','log(dB) [nT]', location = 'lower left')

plotter.plot_2D(auroral_index, 'hour', 'Auroral_Index_1_1_H', 'hour', 'Auroral_Index_1_2_H',
                'Horizontal Auroral Index 1(1) & 1(2)', 'Time in hours','[nT]')
plotter.plot_2D(auroral_index, 'hour', 'Auroral_Index_1_1_Z', 'hour', 'Auroral_Index_1_2_Z',
                'Vertical Auroral Index 1(1) & 1(2)', 'Time in hours','[nT]')

                ###              3D Plot              ####
plotter.plot_3D(auroral_index, 'hour', 'Auroral_Index_1_1_H', 'hour',
                'Auroral_Index_1_2_H','hour', 'Auroral_Index_2_H',
                'Horizontal Auroral index 1(1), 1(2) and 2 in function of time',
                'Time in hours','[nT]')

plotter.plot_3D(auroral_index, 'hour', 'Auroral_Index_1_1_Z', 'hour',
                'Auroral_Index_1_2_Z','hour', 'Auroral_Index_2_Z',
                'Vertical Auroral index 1(1), 1(2) and 2 in function of time',
                'Time in hours','[nT]')

                ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
