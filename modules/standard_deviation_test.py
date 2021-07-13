# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:10:16 2021
@author: Bastien Longeon
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import gridspec

auroral_index = pd.read_hdf('maggraphs/kir202009sec.hdf5','index', start=0, stop=14400)
time = np.linspace(0, 10, 240)

standard_deviation1 = list()
standard_deviation2 = list()
for i in range(0,14400, 60):
    standard_deviation1.append(np.std(auroral_index['Auroral_Index_1_2_Z/X'].iloc[i:i+59]))
    standard_deviation2.append(np.std(auroral_index['Auroral_Index_1_2_Z/Y'].iloc[i:i+59]))

# =============================================================================
# 10-DAYS
# =============================================================================

plt.figure(dpi=300, figsize=(15, 8))
gs = gridspec.GridSpec(2, 1)
# Subplot 1
a1 = plt.subplot(gs[0])
a1.plot(time, standard_deviation1, linewidth=.6, label='STD(log10(dBAC_Z/dBAC_X))')
plt.title('10-days study of the standard deviation for an hour')
# Subplot 2
a2 = plt.subplot(gs[1], sharex = a1)
a2.plot(time, standard_deviation2, linewidth=.6, label='STD(log10(dBAC_Z/dBAC_Y))')
# Plot setup
plt.setp(a1.get_xticklabels(), visible=False)
a1.grid()
a2.grid()
plt.xlim([0, 10])
plt.xticks(np.arange(0,11,1)) # Show the last tick of the x-axes to see the 24-hours mark
a2.tick_params('x', which='major', length=8)
plt.subplots_adjust(hspace=0.14) # Vertical gap between subplots
plt.show()

# =============================================================================
# 30-DAYS
# =============================================================================
auroral_index = pd.read_hdf('maggraphs/kir202009sec.hdf5','index')
time = np.linspace(0, 30, 720)

standard_deviation1 = list()
standard_deviation2 = list()
for i in range(0,43200, 60):
    standard_deviation1.append(np.std(auroral_index['Auroral_Index_1_2_Z/X'].iloc[i:i+59]))
    standard_deviation2.append(np.std(auroral_index['Auroral_Index_1_2_Z/Y'].iloc[i:i+59]))
plt.figure(dpi=300, figsize=(15, 8))
gs = gridspec.GridSpec(2, 1)
# Subplot 1
a1 = plt.subplot(gs[0])
a1.plot(time, standard_deviation1, linewidth=.6, label='STD(log10(dBAC_Z/dBAC_X))')
plt.title('30-days study of the standard deviation for an hour')
# Subplot 2
a2 = plt.subplot(gs[1], sharex = a1)
a2.plot(time, standard_deviation2, linewidth=.6, label='STD(log10(dBAC_Z/dBAC_Y))')
# Plot setup
plt.setp(a1.get_xticklabels(), visible=False)
a1.grid()
a2.grid()
plt.xlim([0, 30])
plt.xticks(np.arange(0,31,1)) # Show the last tick of the x-axes to see the 24-hours mark
a2.tick_params('x', which='major', length=8)
plt.subplots_adjust(hspace=0.14) # Vertical gap between subplots
plt.show()

# =============================================================================
# 30-DAYS 2D for half an hour
# =============================================================================
time = np.linspace(0, 30, 1440)

standard_deviation1 = list()
standard_deviation2 = list()
for i in range(0,43200, 30):
    standard_deviation1.append(np.std(auroral_index['Auroral_Index_1_2_Z/X'].iloc[i:i+29]))
    standard_deviation2.append(np.std(auroral_index['Auroral_Index_1_2_Z/Y'].iloc[i:i+29]))
plt.figure(dpi=300, figsize=(20,10))
(line1, line2) = plt.plot(time, standard_deviation1, time, standard_deviation2, linewidth=.6)
plt.title('30-days study in 2D plot for an hour')
plt.legend([line1, line2], ['std(AC_Z/X)', 'std(AC_Z/Y)'], loc='best', fontsize=15)
plt.xlim([0, 30])
plt.xticks(np.arange(0,31,1)) # Show the last tick of the x-axes to see the 24-hours mark
plt.tick_params('x', which='major', length=8)
plt.grid()
plt.show()

# =============================================================================
# 30-DAYS 2D for a half an hour
# =============================================================================
time = np.linspace(1, 30, 360)

standard_deviation1 = list()
standard_deviation2 = list()
for i in range(0,43200, 120):
    standard_deviation1.append(np.std(auroral_index['Auroral_Index_1_2_Z/X'].iloc[i:i+119]))
    standard_deviation2.append(np.std(auroral_index['Auroral_Index_1_2_Z/Y'].iloc[i:i+119]))
plt.figure(dpi=300)
(line1, line2) = plt.plot(time, standard_deviation1, time, standard_deviation2, linewidth=1)
plt.title('30-days study in 2D plot for 2 hours')
plt.legend([line1, line2], ['std(AC_Z/X)', 'std(AC_Z/Y)'], loc='best')
plt.xticks(np.arange(0,31,5)) # Show the last tick of the x-axes to see the 24-hours mark
plt.xlim([1, 30])
plt.tick_params('x', which='major', length=8)
plt.grid()
plt.show()

# =============================================================================
# 30-DAYS 2D for 6h
# =============================================================================
time = np.linspace(1, 30, 120)

standard_deviation1 = list()
standard_deviation2 = list()
for i in range(0,43200, 360):
    standard_deviation1.append(np.std(auroral_index['Auroral_Index_1_2_Z/X'].iloc[i:i+359]))
    standard_deviation2.append(np.std(auroral_index['Auroral_Index_1_2_Z/Y'].iloc[i:i+359]))
plt.figure(dpi=300)
(line1, line2) = plt.plot(time, standard_deviation1, time, standard_deviation2, linewidth=1)
plt.title('30-days study in 2D plot for 6h')
plt.legend([line1, line2], ['std(AC_Z/X)', 'std(AC_Z/Y)'], loc='best')
plt.xticks(np.arange(0,31,5)) # Show the last tick of the x-axes to see the 24-hours mark
plt.xlim([1, 30])
plt.tick_params('x', which='major', length=8)
plt.grid()
plt.show()

# =============================================================================
# 30-DAYS 2D for 12h
# =============================================================================
time = np.linspace(1, 30, 60)

standard_deviation1 = list()
standard_deviation2 = list()
for i in range(0,43200, 720):
    standard_deviation1.append(np.std(auroral_index['Auroral_Index_1_2_Z/X'].iloc[i:i+719]))
    standard_deviation2.append(np.std(auroral_index['Auroral_Index_1_2_Z/Y'].iloc[i:i+719]))
plt.figure(dpi=300)
(line1, line2) = plt.plot(time, standard_deviation1, time, standard_deviation2, linewidth=1)
plt.title('30-days study in 2D plot for 12h')
plt.legend([line1, line2], ['std(AC_Z/X)', 'std(AC_Z/Y)'], loc='best')
plt.xticks(np.arange(0,31,5)) # Show the last tick of the x-axes to see the 24-hours mark
plt.xlim([1, 30])
plt.tick_params('x', which='major', length=8)
plt.grid()
plt.show()

# =============================================================================
# 30-DAYS 2D for a day
# =============================================================================
time = np.linspace(1, 30, 30)

standard_deviation1 = list()
standard_deviation2 = list()
for i in range(0,43200, 1440):
    standard_deviation1.append(np.std(auroral_index['Auroral_Index_1_2_Z/X'].iloc[i:i+1439]))
    standard_deviation2.append(np.std(auroral_index['Auroral_Index_1_2_Z/Y'].iloc[i:i+1439]))
plt.figure(dpi=300)
(line1, line2) = plt.plot(time, standard_deviation1, time, standard_deviation2, linewidth=1)
plt.title('30-days study in 2D plot for a day')
plt.legend([line1, line2], ['std(AC_Z/X)', 'std(AC_Z/Y)'], loc='best')
plt.xticks(np.arange(0,31,5)) # Show the last tick of the x-axes to see the 24-hours mark
plt.xlim([1, 30])
plt.tick_params('x', which='major', length=8)
plt.grid()
plt.show()
