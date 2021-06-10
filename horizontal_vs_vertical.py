# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:16:41 2021
@author: Bastien Longeon
"""
import pandas as pd     # pandas is for reading file
import numpy as np      # instead of math to convert X,Y <--> H,D
import modules.auroral_index_functions as aur
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import gridspec
import time
startTime = time.time()

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


"""
Graph 1: Auroral index 1.2: Z/H
Graph 2: Auroral index 2: Z/H
Graph 3: (Auroral index 2 Z/H) / (Auroral index 1.2 Z/H)
Graph 4: Auroral index 1.2 and 2: horizontal
In function of time
"""
                ###              Auroral Indexes              ####
auroral_index = pd.DataFrame() #Creation of the DataFrame that will store the auroral indexes
# This new list is necessary to plot the data properly with one value in 'hour'
# corresponding to one value of B
auroral_index['hour'] = np.linspace(0, 24, 1440)

                ###              Auroral Index 1.2              ####
auroral_index['Auroral_Index_1_2_H'] = aur.auroral_index1_2(magdata, 'KIR_H')
auroral_index['Auroral_Index_1_2_Z'] = aur.auroral_index1_2(magdata, 'KIR_Z')

                ###              Auroral Index 2              ####
auroral_index['Auroral_Index_2_H'] = aur.auroral_index2(magdata, 18000, 36000, 'KIR_H')
auroral_index['Auroral_Index_2_Z'] = aur.auroral_index2(magdata, 18000, 43200, 'KIR_Z')

                ###              Auroral Index 1.2: Z/H              ####
auroral_index['Auroral_Index_1_2_Z/H'] = auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_H']

                ###              Auroral Index 2: Z/H              ####
auroral_index['Auroral_Index_2_Z/H'] = auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_H']

###              (Auroral Index 2: Z/H) / (Auroral Index 1.2: Z/H)             ####
auroral_index['DC/AC'] = auroral_index['Auroral_Index_2_Z/H']/auroral_index['Auroral_Index_1_2_Z/H']

for i in range(0,1440):
    if abs(auroral_index['Auroral_Index_2_H'].iloc[i]) < 50 and abs(auroral_index['Auroral_Index_1_2_H'].iloc[i]) < 1:
        auroral_index['Auroral_Index_1_2_Z/H'].iloc[i] = np.nan
        auroral_index['Auroral_Index_2_Z/H'].iloc[i] = np.nan
        auroral_index['DC/AC'].iloc[i] = np.nan

                ###              Plots              ####
plt.figure(dpi=200, figsize=(15, 8))
gs = gridspec.GridSpec(4, 1)
# Subplot 1
a1 = plt.subplot(gs[0])
line1, = a1.plot(auroral_index['hour'], auroral_index['Auroral_Index_1_2_Z/H'], label='(dBAC_Z/dBAC_H)')
plt.title('Auroral indexes quotients during Auroral Activity', fontsize=15)
# Subplot 2
a2 = plt.subplot(gs[1], sharex = a1)
line2, = a2.plot(auroral_index['hour'], np.sign(auroral_index['Auroral_Index_2_Z/H'])*np.log10(abs(auroral_index['Auroral_Index_2_Z/H'])), label='log10(dBDC_Z/ dBDC_H)')
# Subplot 3
a3 = plt.subplot(gs[2], sharex = a1)
line3, = a3.plot(auroral_index['hour'], np.sign(auroral_index['DC/AC'])*np.log10(abs(auroral_index['DC/AC'])), label='log10((dBDC_Z/ dBDC_H)/(dBAC_Z/ dBAC_H))')
# Subplot 4
a4 = plt.subplot(gs[3], sharex = a1)
(line4, line5) = a4.plot(auroral_index['hour'], auroral_index['Auroral_Index_2_H'],
                         auroral_index['hour'], auroral_index['Auroral_Index_1_2_H'].multiply(100))
# Plot setup
plt.setp(a1.get_xticklabels(), visible=False)
plt.setp(a2.get_xticklabels(), visible=False)
plt.setp(a3.get_xticklabels(), visible=False)
a1.grid()
a2.grid()
a3.grid()
a4.grid()
a1.legend()
a2.legend()
a3.legend()
a4.legend([line4, line5],["dBDC_H", "dBAC_H"])
plt.xlim([0, 24])
plt.xticks(np.arange(0,25,4)) # Show the last tick of the x-axes to see the 24-hours mark
a3.xaxis.set_minor_locator(AutoMinorLocator(5))
a3.tick_params('x', which='minor', length=6)
a3.tick_params('x', which='major', length=8)

# Vertical gap between subplots
plt.subplots_adjust(hspace=0.1)
plt.show()

                ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
