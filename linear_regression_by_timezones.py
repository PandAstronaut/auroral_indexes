# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 16:05:32 2021
@author: Bastien Longeon
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

save = False

folder = "maggraphs/"
year = '2020'
month = '09'
extension_hdf = month + 'sec.hdf5'

# =============================================================================
# SWEDEN + FINLAND + SVALBARD
# =============================================================================
stations = ['nur','ups','lyc','abk','hrn']

x = np.array([])
y = np.array([])

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station =='ups': latitude = 58.53
    elif station == 'nur': latitude = 58.06
    elif station =='lyc': latitude = 62.82
    elif station =='abk': latitude = 66.28
    elif station == 'hrn': latitude = 74.28

    x = np.append(x, np.nanmean(standard_deviation['Z/H']))
    y = np.append(y, latitude)

x = x.reshape((-1, 1))
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

stations = ['nur','ups','lyc','kir','abk','hrn']

plt.figure(dpi=300)
# Expected values from the linear regression
ax1 = np.array([0, 1])
ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
plt.plot(ax2, ax1,'--', label = 'Expected values')
plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of dB/dt(Z/H) in function of the geomagnetic latitude\nSweden + Finland + Svalbard - September 2020\nR²={0:.3f} (without Kiruna)'.format(r_sq)
plt.title(title, fontsize=10)
plt.xlabel('Geomagnetic Latitude (°)')

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')

    if station =='ups': latitude = 58.53
    elif station == 'nur': latitude = 58.06
    elif station =='lyc': latitude = 62.82
    elif station =='abk': latitude = 66.28
    elif station == 'kir': latitude = 65.58
    elif station == 'hrn': latitude = 74.28

    plt.scatter(latitude, np.nanmean(standard_deviation['Z/H']))
    plt.annotate(station.upper(), # Text
                  (latitude, np.nanmean(standard_deviation['Z/H'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([45,83])
plt.ylim([0,0.3])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression in function of geomagnetic latitude - Scandinavia.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# West America
# =============================================================================
stations = ['brw','cmo','sit','shu']

x = np.array([])
y = np.array([])

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station =='shu': latitude = 54.29
    elif station == 'sit': latitude = 60.25
    elif station =='cmo': latitude = 64.84
    elif station == 'brw': latitude = 70.07
    elif station == 'ded': latitude = 76.13 # No data for Deadhorse, only 9999
    elif station =='ykc': latitude = 81.84

    x = np.append(x, np.nanmean(standard_deviation['Z/H']))
    y = np.append(y, latitude)

x = x.reshape((-1, 1))
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

plt.figure(dpi=300)
# Expected values from the linear regression
ax1 = np.array([0, 1])
ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
plt.plot(ax2, ax1,'--', label = 'Expected values')
plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of dB/dt(Z/H) in function of the geomagnetic latitude\nWest America - September 2020\nR²={0:.3f}'.format(r_sq)
plt.title(title, fontsize=10)
plt.xlabel('Geomagnetic Latitude (°)')

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station =='shu': latitude = 54.29
    elif station == 'sit': latitude = 60.25
    elif station =='cmo': latitude = 64.84
    elif station =='ykc': latitude = 68.59
    elif station == 'brw': latitude = 70.07
    elif station == 'ded': latitude = 70.47

    plt.scatter(latitude, np.nanmean(standard_deviation['Z/H']))
    plt.annotate(station.upper(), # Text
                  (latitude, np.nanmean(standard_deviation['Z/H'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([45,83])
plt.ylim([0,0.3])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression in function of geomagnetic latitude - West America.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# East + Middle America
# =============================================================================
stations = ['cbb','res','fcc','blc','ykc','iqa','stj','frd','ott']

x = np.array([])
y = np.array([])

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'fcc': latitude = 66.47
    elif station == 'ykc': latitude = 68.59
    elif station == 'blc': latitude = 72.55
    elif station == 'cbb': latitude = 76.13
    elif station == 'res': latitude = 81.84

    x = np.append(x, np.nanmean(standard_deviation['Z/H']))
    y = np.append(y, latitude)

x = x.reshape((-1, 1))
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

plt.figure(dpi=300)
# Expected values from the linear regression
# ax1 = np.array([0, 1])
# ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
# plt.plot(ax2, ax1,'--', label = 'Expected values')
# plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of dB/dt(Z/H) in function of the geomagnetic latitude\nEast and Middle America - September 2020\nR²={0:.3f}'.format(r_sq)
plt.title(title, fontsize=10)
plt.xlabel('Geomagnetic Latitude (°)')

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'frd': latitude = 47.54
    elif station == 'ott': latitude = 54.75
    elif station == 'stj': latitude = 56.26
    elif station == 'iqa': latitude = 72.29
    elif station == 'fcc': latitude = 66.47
    elif station == 'ykc': latitude = 68.59
    elif station == 'blc': latitude = 72.55
    elif station == 'cbb': latitude = 76.13
    elif station == 'res': latitude = 81.84

    plt.scatter(latitude, np.nanmean(standard_deviation['Z/H']))
    plt.annotate(station.upper(), # Text
                  (latitude, np.nanmean(standard_deviation['Z/H'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([45,83])
plt.ylim([0,0.3])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression in function of geomagnetic latitude - East and Middle America.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# Mid EU
# =============================================================================
stations = ['bdv','bel','hlp','wic']

x = np.array([])
y = np.array([])

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'wic': latitude = 46.43
    elif station == 'bdv': latitude = 48.75
    elif station == 'hlp': latitude = 53.31
    elif station == 'bel': latitude = 50.31

    x = np.append(x, np.nanmean(standard_deviation['Z/H']))
    y = np.append(y, latitude)

x = x.reshape((-1, 1))
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

plt.figure(dpi=300)
# Expected values from the linear regression
ax1 = np.array([0, 1])
ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
plt.plot(ax2, ax1,'--', label = 'Expected values')
plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of dB/dt(Z/H) in function of the geomagnetic latitude\nMid Europe - September 2020\nR²={0:.3f}'.format(r_sq)
plt.title(title, fontsize=10)
plt.xlabel('Geomagnetic Latitude (°)')

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'wic': latitude = 46.43
    elif station == 'bdv': latitude = 48.75
    elif station == 'hlp': latitude = 53.31
    elif station == 'bel': latitude = 50.31

    plt.scatter(latitude, np.nanmean(standard_deviation['Z/H']))
    plt.annotate(station.upper(), # Text
                  (latitude, np.nanmean(standard_deviation['Z/H'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([45,83])
plt.ylim([0,0.3])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression in function of geomagnetic latitude - Mid EU.png', dpi=300, bbox_inches='tight')
plt.show()


# =============================================================================
# SWEDEN + FINLAND + SVALBARD
# =============================================================================
stations = ['nur','ups','lyc','abk','hrn']

x = np.array([])
y = np.array([])

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station =='ups': inclination = 72.89
    elif station == 'nur': inclination = 73.5
    elif station =='lyc': inclination = 75.59
    elif station =='abk': inclination = 77.68
    elif station == 'hrn': inclination = 81.74

    x = np.append(x, np.nanmean(standard_deviation['Z/H']))
    y = np.append(y, inclination)

x = x.reshape((-1, 1))
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

stations = ['nur','ups','lyc','kir','abk','hrn']

plt.figure(dpi=300)
# Expected values from the linear regression
ax1 = np.array([0, 1])
ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
plt.plot(ax2, ax1,'--', label = 'Expected values')
plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of dB/dt(Z/H) in function of the inclination\nSweden + Finland + Svalbard - September 2020\nR²={0:.3f} (without Kiruna)'.format(r_sq)
plt.title(title, fontsize=10)
plt.xlabel('inclination')

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')

    if station =='ups': inclination = 72.89
    elif station == 'nur': inclination = 73.5
    elif station =='lyc': inclination = 75.59
    elif station =='abk': inclination = 77.68
    elif station == 'hrn': inclination = 81.74
    elif station == 'kir': inclination = 78.53

    plt.scatter(inclination, np.nanmean(standard_deviation['Z/H']))
    plt.annotate(station.upper(), # Text
                  (inclination, np.nanmean(standard_deviation['Z/H'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([68,90])
plt.ylim([0,0.3])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression in function of inclination - Scandinavia.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# West America
# =============================================================================
stations = ['brw','cmo','sit','shu']

x = np.array([])
y = np.array([])

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'shu': inclination = 67.69
    elif station == 'sit': inclination = 73.34
    elif station == 'cmo': inclination = 77.07
    elif station == 'brw': inclination = 80.81
    elif station == 'ykc': inclination = 80.58

    x = np.append(x, np.nanmean(standard_deviation['Z/H']))
    y = np.append(y, inclination)

x = x.reshape((-1, 1))
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

plt.figure(dpi=300)
# Expected values from the linear regression
ax1 = np.array([0, 1])
ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
plt.plot(ax2, ax1,'--', label = 'Expected values')
plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of dB/dt(Z/H) in function of the inclination\nWest America - September 2020\nR²={0:.3f}'.format(r_sq)
plt.title(title, fontsize=10)
plt.xlabel('inclination')

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'shu': inclination = 67.69
    elif station == 'sit': inclination = 73.34
    elif station == 'cmo': inclination = 77.07
    elif station == 'brw': inclination = 80.81
    elif station == 'ykc': inclination = 80.58

    plt.scatter(inclination, np.nanmean(standard_deviation['Z/H']))
    plt.annotate(station.upper(), # Text
                  (inclination, np.nanmean(standard_deviation['Z/H'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([65,82])
plt.ylim([0,0.3])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression in function of inclination - West America.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# Middle America
# =============================================================================
stations = ['cbb','res','fcc','blc','ykc','iqa','stj','frd','ott']

x = np.array([])
y = np.array([])

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'fcc': inclination = 80.33
    elif station == 'ykc': inclination = 80.58
    elif station == 'blc': inclination = 83.05
    elif station == 'cbb': inclination = 84.94
    elif station == 'res': inclination = 87.05
    elif station == 'frd': inclination = 64.80
    elif station == 'ott': inclination = 69.91
    elif station == 'stj': inclination = 66.66
    elif station == 'iqa': inclination = 80.33

    x = np.append(x, np.nanmean(standard_deviation['Z/H']))
    y = np.append(y, inclination)

x = x.reshape((-1, 1))
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

plt.figure(dpi=300)
# Expected values from the linear regression
ax1 = np.array([0, 1])
ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
plt.plot(ax2, ax1,'--', label = 'Expected values')
plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of dB/dt(Z/H) in function of the inclination\nEast and Middle America - September 2020\nR²={0:.3f}'.format(r_sq)
plt.title(title, fontsize=10)
plt.xlabel('inclination')

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'fcc': inclination = 80.33
    elif station == 'ykc': inclination = 80.58
    elif station == 'blc': inclination = 83.05
    elif station == 'cbb': inclination = 84.94
    elif station == 'res': inclination = 87.05
    elif station == 'frd': inclination = 64.80
    elif station == 'ott': inclination = 69.91
    elif station == 'stj': inclination = 66.66
    elif station == 'iqa': inclination = 80.33

    plt.scatter(inclination, np.nanmean(standard_deviation['Z/H']))
    plt.annotate(station.upper(), # Text
                  (inclination, np.nanmean(standard_deviation['Z/H'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([65,88])
plt.ylim([0,0.3])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression in function of inclination -East and Middle America.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# Mid EU
# =============================================================================
stations = ['bdv','bel','hlp','wic']

x = np.array([])
y = np.array([])

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'wic': inclination = 64.365
    elif station == 'bdv': inclination = 65.255
    elif station == 'hlp': inclination = 67.68
    elif station == 'bel': inclination = 67.86
    elif station == 'clf': latitude = 63.7

    x = np.append(x, np.nanmean(standard_deviation['Z/H']))
    y = np.append(y, inclination)

x = x.reshape((-1, 1))
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

plt.figure(dpi=300)
# Expected values from the linear regression
ax1 = np.array([0, 1])
ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
plt.plot(ax2, ax1,'--', label = 'Expected values')
plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of dB/dt(Z/H) in function of the inclination\nMid Europe - September 2020\nR²={0:.3f}'.format(r_sq)
plt.title(title, fontsize=10)
plt.xlabel('inclination')

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'wic': inclination = 64.365
    elif station == 'bdv': inclination = 65.255
    elif station == 'hlp': inclination = 67.68
    elif station == 'bel': inclination = 67.86
    elif station == 'clf': latitude = 63.7

    plt.scatter(inclination, np.nanmean(standard_deviation['Z/H']))
    plt.annotate(station.upper(), # Text
                  (inclination, np.nanmean(standard_deviation['Z/H'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([62,70])
plt.ylim([0,0.3])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression in function of inclination - Mid EU.png', dpi=300, bbox_inches='tight')
plt.show()
