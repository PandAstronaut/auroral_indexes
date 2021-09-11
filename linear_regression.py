# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 10:27:23 2021
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
# Linear Regression in function of the inclination
# =============================================================================
# Stations for the linear regression
stations = ['kir','abk','ups','brw','cbb','blc','lyc', 'nur', 'hrn']


x = np.array([])
y = np.array([])

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'wic': inclination = 64.365
    elif station == 'bdv': inclination = 65.255
    elif station == 'clf': inclination = 63.7
    elif station == 'frd': inclination = 64.8
    elif station == 'stj': inclination = 66.66
    elif station == 'hlp': inclination = 67.68
    elif station == 'bel': inclination = 67.86
    elif station == 'shu': inclination = 67.69
    elif station == 'ott': inclination = 69.91
    elif station == 'ups': inclination = 72.89
    elif station == 'nur': inclination = 73.5
    elif station == 'sit': inclination = 73.34
    elif station == 'lyc': inclination = 75.59
    elif station == 'cmo': inclination = 77.07
    elif station == 'abk': inclination = 77.68
    elif station == 'kir': inclination = 78.53
    elif station == 'brw': inclination = 80.81
    elif station == 'iqa': inclination = 80.33
    elif station == 'fcc': inclination = 80.33
    elif station == 'ykc': inclination = 80.58
    elif station == 'hrn': inclination = 81.74
    elif station == 'blc': inclination = 83.05
    elif station == 'cbb': inclination = 84.94
    elif station == 'res': inclination = 87.05

    x = np.append(x, np.nanmean(standard_deviation['Z/H']))
    y = np.append(y, inclination)

x = x.reshape((-1, 1))
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

stations = ['kir','abk','ups','brw','cbb','blc','lyc', 'nur', 'hrn', 'wic','clf','bdv','iqa','sit','fcc','shu','cmo','res','hlp','bel']


plt.figure(dpi=300)
# ax1 = np.array([0, 1])
# ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
# plt.plot(ax2, ax1,'--', label = 'Expected values')
# plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of dB/dt(Z/H) in function of the inclination\nSeptember 2020'
plt.title(title, fontsize=10)
plt.xlabel('Inclination (°)')
for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'wic': inclination = 64.365
    elif station == 'bdv': inclination = 65.255
    elif station == 'clf': inclination = 63.7
    elif station == 'hlp': inclination = 67.68
    elif station == 'bel': inclination = 67.86
    elif station == 'shu': inclination = 67.69
    elif station == 'ups': inclination = 72.89
    elif station == 'nur': inclination = 73.5
    elif station == 'sit': inclination = 73.34
    elif station == 'lyc': inclination = 75.59
    elif station == 'cmo': inclination = 77.07
    elif station == 'abk': inclination = 77.68
    elif station == 'kir': inclination = 78.53
    elif station == 'brw': inclination = 80.81
    elif station == 'iqa': inclination = 80.33
    elif station == 'fcc': inclination = 80.33
    elif station == 'hrn': inclination = 81.74
    elif station == 'blc': inclination = 83.05
    elif station == 'cbb': inclination = 84.94
    elif station == 'res': inclination = 87.05

    plt.scatter(inclination, np.nanmean(standard_deviation['Z/H']))
    plt.annotate(station.upper(), # Text
                  (inclination, np.nanmean(standard_deviation['Z/H'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([62,90])
plt.ylim([0,0.3])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression in function of Inclination.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# Linear Regression in function of the geomagnetic latitude
# =============================================================================

stations = ['nur','ups','lyc','abk','blc','hrn','cbb']

x = np.array([])
y = np.array([])

for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'wic': latitude = 46.43
    elif station == 'frd': latitude = 47.54
    elif station == 'bdv': latitude = 48.75
    elif station == 'clf': latitude = 49.61
    elif station == 'hlp': latitude = 53.31
    elif station == 'bel': latitude = 50.31
    elif station == 'shu': latitude = 54.29
    elif station == 'ott': latitude = 54.75
    elif station == 'stj': latitude = 56.26
    elif station == 'ups': latitude = 58.53
    elif station == 'nur': latitude = 58.06
    elif station == 'sit': latitude = 60.25
    elif station == 'lyc': latitude = 62.82
    elif station == 'cmo': latitude = 64.84
    elif station == 'abk': latitude = 66.28
    elif station == 'kir': latitude = 65.58
    elif station == 'fcc': latitude = 66.47
    elif station == 'ykc': latitude = 68.59
    elif station == 'brw': latitude = 70.07
    elif station == 'ded': latitude = 70.47
    elif station == 'iqa': latitude = 72.29
    elif station == 'blc': latitude = 72.55
    elif station == 'hrn': latitude = 74.28
    elif station == 'cbb': latitude = 76.13
    elif station == 'res': latitude = 81.84
    x = np.append(x, np.nanmean(standard_deviation['Z/H']))
    y = np.append(y, latitude)

x = x.reshape((-1, 1))
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

stations = ['kir','abk','ups','brw','cbb','blc','lyc', 'nur', 'hrn', 'wic','clf','bdv','iqa','sit','fcc','shu','cmo','res','hlp','bel']

plt.figure(dpi=300)
ax1 = np.array([0, 1])
ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
plt.plot(ax2, ax1,'--', label = 'Expected values')
plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of dB/dt(Z/H) in function of the geomagnetic latitude\nSeptember 2020'
plt.title(title, fontsize=10)
plt.xlabel('Geomagnetic Latitude (°)')
for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'wic': latitude = 46.43
    elif station == 'frd': latitude = 47.54
    elif station == 'bdv': latitude = 48.75
    elif station == 'clf': latitude = 49.61
    elif station == 'hlp': latitude = 53.31
    elif station == 'bel': latitude = 50.31
    elif station == 'shu': latitude = 54.29
    elif station == 'ott': latitude = 54.75
    elif station == 'stj': latitude = 56.26
    elif station == 'ups': latitude = 58.53
    elif station == 'nur': latitude = 58.06
    elif station == 'sit': latitude = 60.25
    elif station == 'lyc': latitude = 62.82
    elif station == 'cmo': latitude = 64.84
    elif station == 'abk': latitude = 66.28
    elif station == 'kir': latitude = 65.58
    elif station == 'fcc': latitude = 66.47
    elif station == 'ykc': latitude = 68.59
    elif station == 'brw': latitude = 70.07
    elif station == 'ded': latitude = 70.47
    elif station == 'iqa': latitude = 72.29
    elif station == 'blc': latitude = 72.55
    elif station == 'hrn': latitude = 74.28
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
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression in function of geomagnetic latitude.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# Linear Regression of std(inclination) in function of the geomagnetic latitude
# =============================================================================

# stations = ['nur','ups','sit','lyc','abk','kir','fcc','cmo','brw']

# x = np.array([])
# y = np.array([])

# for station in stations:
#     filename = folder + station +  year + extension_hdf
#     standard_deviation = pd.read_hdf(filename, 'std')
#     if station =='wic': latitude = 46.43
#     elif station =='bdv': latitude = 48.75
#     elif station =='clf': latitude = 49.61
#     elif station =='hlp': latitude = 53.31
#     elif station =='bel': latitude = 50.31
#     elif station =='shu': latitude = 54.29
#     elif station =='ups': latitude = 58.53
#     elif station == 'nur': latitude = 58.06
#     elif station == 'sit': latitude = 60.25
#     elif station =='lyc': latitude = 62.82
#     elif station =='cmo': latitude = 64.84
#     elif station =='abk': latitude = 66.28
#     elif station == 'kir': latitude = 65.58
#     elif station == 'fcc': latitude = 66.47
#     elif station == 'brw': latitude = 70.07
#     elif station == 'iqa': latitude = 72.29
#     elif station == 'blc': latitude = 72.55
#     elif station == 'hrn': latitude = 74.28
#     elif station == 'cbb': latitude = 76.13
#     elif station =='res': latitude = 81.84
#     x = np.append(x, np.nanmean(standard_deviation['angle']))
#     y = np.append(y, latitude)

# x = x.reshape((-1, 1))
# model = LinearRegression().fit(x, y)
# r_sq = model.score(x, y)

stations = ['kir','abk','ups','brw','cbb','blc','lyc', 'nur', 'hrn', 'wic','clf','bdv','iqa','sit','fcc','shu','cmo','res','hlp','bel']

plt.figure(dpi=300)
# ax1 = np.array([0, 1])
# ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
# plt.plot(ax2, ax1,'--', label = 'Expected values')
# plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of the inclination in function of the geomagnetic latitude\nSeptember 2020'
plt.title(title, fontsize=10)
plt.xlabel('Geomagnetic Latitude (°)')
for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'wic': latitude = 46.43
    elif station == 'frd': latitude = 47.54
    elif station == 'bdv': latitude = 48.75
    elif station == 'clf': latitude = 49.61
    elif station == 'hlp': latitude = 53.31
    elif station == 'bel': latitude = 50.31
    elif station == 'shu': latitude = 54.29
    elif station == 'ott': latitude = 54.75
    elif station == 'stj': latitude = 56.26
    elif station == 'ups': latitude = 58.53
    elif station == 'nur': latitude = 58.06
    elif station == 'sit': latitude = 60.25
    elif station == 'lyc': latitude = 62.82
    elif station == 'cmo': latitude = 64.84
    elif station == 'abk': latitude = 66.28
    elif station == 'kir': latitude = 65.58
    elif station == 'fcc': latitude = 66.47
    elif station == 'ykc': latitude = 68.59
    elif station == 'brw': latitude = 70.07
    elif station == 'ded': latitude = 70.47
    elif station == 'iqa': latitude = 72.29
    elif station == 'blc': latitude = 72.55
    elif station == 'hrn': latitude = 74.28
    elif station == 'cbb': latitude = 76.13
    elif station == 'res': latitude = 81.84

    plt.scatter(latitude, np.nanmean(standard_deviation['angle']))
    plt.annotate(station.upper(), # Text
                  (latitude, np.nanmean(standard_deviation['angle'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([45,83])
plt.ylim([0,0.06])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression of the incliination in function of geomagnetic latitude.png', dpi=300, bbox_inches='tight')
plt.show()


# =============================================================================
# Linear Regression of std(dI/dt) in function of the geomagnetic latitude
# =============================================================================

# stations = ['nur','ups','lyc','abk','kir']

# x = np.array([])
# y = np.array([])

# for station in stations:
#     filename = folder + station +  year + extension_hdf
#     standard_deviation = pd.read_hdf(filename, 'std')
#     if station =='wic': latitude = 46.43
#     elif station =='bdv': latitude = 48.75
#     elif station =='clf': latitude = 49.61
#     elif station =='hlp': latitude = 53.31
#     elif station =='bel': latitude = 50.31
#     elif station =='shu': latitude = 54.29
#     elif station =='ups': latitude = 58.53
#     elif station == 'nur': latitude = 58.06
#     elif station == 'sit': latitude = 60.25
#     elif station =='lyc': latitude = 62.82
#     elif station =='cmo': latitude = 64.84
#     elif station =='abk': latitude = 66.28
#     elif station == 'kir': latitude = 65.58
#     elif station == 'fcc': latitude = 66.47
#     elif station == 'brw': latitude = 70.07
#     elif station == 'iqa': latitude = 72.29
#     elif station == 'blc': latitude = 72.55
#     elif station == 'hrn': latitude = 74.28
#     elif station == 'cbb': latitude = 76.13
#     elif station =='res': latitude = 81.84
#     x = np.append(x, np.nanmean(standard_deviation['dI/dt']))
#     y = np.append(y, latitude)

# x = x.reshape((-1, 1))
# model = LinearRegression().fit(x, y)
# r_sq = model.score(x, y)

stations = ['kir','abk','ups','brw','cbb','blc','lyc', 'nur', 'hrn', 'wic','clf','bdv','iqa','sit','fcc','shu','cmo','res','hlp','bel']

plt.figure(dpi=300)
# ax1 = np.array([0, 1])
# ax2 = np.array([model.intercept_, model.coef_[0] + model.intercept_])
# plt.plot(ax2, ax1,'--', label = 'Expected values')
# plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of dI/dt in function of the geomagnetic latitude\nSeptember 2020'
plt.title(title, fontsize=10)
plt.xlabel('Geomagnetic Latitude (°)')
for station in stations:
    filename = folder + station +  year + extension_hdf
    standard_deviation = pd.read_hdf(filename, 'std')
    if station == 'wic': latitude = 46.43
    elif station == 'frd': latitude = 47.54
    elif station == 'bdv': latitude = 48.75
    elif station == 'clf': latitude = 49.61
    elif station == 'hlp': latitude = 53.31
    elif station == 'bel': latitude = 50.31
    elif station == 'shu': latitude = 54.29
    elif station == 'ott': latitude = 54.75
    elif station == 'stj': latitude = 56.26
    elif station == 'ups': latitude = 58.53
    elif station == 'nur': latitude = 58.06
    elif station == 'sit': latitude = 60.25
    elif station == 'lyc': latitude = 62.82
    elif station == 'cmo': latitude = 64.84
    elif station == 'abk': latitude = 66.28
    elif station == 'kir': latitude = 65.58
    elif station == 'fcc': latitude = 66.47
    elif station == 'ykc': latitude = 68.59
    elif station == 'brw': latitude = 70.07
    elif station == 'ded': latitude = 70.47
    elif station == 'iqa': latitude = 72.29
    elif station == 'blc': latitude = 72.55
    elif station == 'hrn': latitude = 74.28
    elif station == 'cbb': latitude = 76.13
    elif station == 'res': latitude = 81.84

    plt.scatter(latitude, np.nanmean(standard_deviation['dI/dt']))
    plt.annotate(station.upper(), # Text
                  (latitude, np.nanmean(standard_deviation['dI/dt'])), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([45,83])
plt.ylim([0,0.0008])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression of dI.dt in function of geomagnetic latitude.png', dpi=300, bbox_inches='tight')
plt.show()


# =============================================================================
# Linear Regression of B(Z) in function of the geomagnetic latitude
# =============================================================================

# stations = ['nur','ups','lyc','abk','kir','blc','brw','hrn','cbb']
# x = np.array([])
# y = np.array([])

# for station in stations:
#     filename = folder + station +  year + extension_hdf
#     magdata = pd.read_hdf(filename, 'data')

#     std_Z = np.array([])
#     for i in range(0, 2592000, 10800):
#         std_Z = np.append(std_Z, np.nanstd(magdata[station.upper() + '_Z'].iloc[i:i+10799]))
#     mean = np.nanmean(std_Z)
#     if station =='wic': latitude = 46.43
#     elif station =='bdv': latitude = 48.75
#     elif station =='clf': latitude = 49.61
#     elif station =='hlp': latitude = 53.31
#     elif station =='bel': latitude = 50.31
#     elif station =='shu': latitude = 54.29
#     elif station =='ups': latitude = 58.53
#     elif station == 'nur': latitude = 58.06
#     elif station == 'sit': latitude = 60.25
#     elif station =='lyc': latitude = 62.82
#     elif station =='cmo': latitude = 64.84
#     elif station =='abk': latitude = 66.28
#     elif station == 'kir': latitude = 65.58
#     elif station == 'fcc': latitude = 66.47
#     elif station == 'brw': latitude = 70.07
#     elif station == 'iqa': latitude = 72.29
#     elif station == 'blc': latitude = 72.55
#     elif station == 'hrn': latitude = 74.28
#     elif station == 'cbb': latitude = 76.13
#     elif station =='res': latitude = 81.84

#     x = np.append(x, mean)
#     y = np.append(y, latitude)

# x = x.reshape((-1, 1))
# model = LinearRegression().fit(x, y)
# r_sq = model.score(x, y)

stations = ['kir','abk','ups','brw','cbb','blc','lyc', 'nur', 'hrn', 'wic','clf','bdv','iqa','sit','fcc','shu','cmo','res','hlp','bel']

plt.figure(dpi=300)
# ax1 = np.array([0, 40])
# ax2 = np.array([model.intercept_, 40*model.coef_[0] + model.intercept_])
# plt.plot(ax2, ax1,'--', label = 'Expected values')
# plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of B(Z) in function of the geomagnetic latitude\nSeptember 2020'
plt.title(title, fontsize=10)
plt.xlabel('Geomagnetic Latitude (°)')
plt.ylabel('nT')
for station in stations:
    filename = folder + station +  year + extension_hdf
    magdata = pd.read_hdf(filename, 'data')

    std_Z = np.array([])
    for i in range(0, 2592000, 10800):
        std_Z = np.append(std_Z, np.nanstd(magdata[station.upper() + '_Z'].iloc[i:i+10799]))
    mean = np.nanmean(std_Z)
    if station == 'wic': latitude = 46.43
    elif station == 'frd': latitude = 47.54
    elif station == 'bdv': latitude = 48.75
    elif station == 'clf': latitude = 49.61
    elif station == 'hlp': latitude = 53.31
    elif station == 'bel': latitude = 50.31
    elif station == 'shu': latitude = 54.29
    elif station == 'ott': latitude = 54.75
    elif station == 'stj': latitude = 56.26
    elif station == 'ups': latitude = 58.53
    elif station == 'nur': latitude = 58.06
    elif station == 'sit': latitude = 60.25
    elif station == 'lyc': latitude = 62.82
    elif station == 'cmo': latitude = 64.84
    elif station == 'abk': latitude = 66.28
    elif station == 'kir': latitude = 65.58
    elif station == 'fcc': latitude = 66.47
    elif station == 'ykc': latitude = 68.59
    elif station == 'brw': latitude = 70.07
    elif station == 'ded': latitude = 70.47
    elif station == 'iqa': latitude = 72.29
    elif station == 'blc': latitude = 72.55
    elif station == 'hrn': latitude = 74.28
    elif station == 'cbb': latitude = 76.13
    elif station == 'res': latitude = 81.84

    plt.scatter(latitude, mean)
    plt.annotate(station.upper(), # Text
                  (latitude, mean), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([45,83])
plt.ylim([0,37])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression of B_Z in function of geomagnetic latitude.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# Linear Regression of B(H) in function of the geomagnetic latitude
# =============================================================================

# stations = ['nur','ups','lyc','abk','kir','blc','brw','hrn','cbb']
# x = np.array([])
# y = np.array([])

# for station in stations:
#     filename = folder + station +  year + extension_hdf
#     magdata = pd.read_hdf(filename, 'data')

#     std_H = np.array([])
#     for i in range(0, 2592000, 10800):
#         std_H = np.append(std_H, np.nanstd(magdata[station.upper() + '_H'].iloc[i:i+10799]))
#     mean = np.nanmean(std_H)
#     if station =='wic': latitude = 46.43
#     elif station =='bdv': latitude = 48.75
#     elif station =='clf': latitude = 49.61
#     elif station =='hlp': latitude = 53.31
#     elif station =='bel': latitude = 50.31
#     elif station =='shu': latitude = 54.29
#     elif station =='ups': latitude = 58.53
#     elif station == 'nur': latitude = 58.06
#     elif station == 'sit': latitude = 60.25
#     elif station =='lyc': latitude = 62.82
#     elif station =='cmo': latitude = 64.84
#     elif station =='abk': latitude = 66.28
#     elif station == 'kir': latitude = 65.58
#     elif station == 'fcc': latitude = 66.47
#     elif station == 'brw': latitude = 70.07
#     elif station == 'iqa': latitude = 72.29
#     elif station == 'blc': latitude = 72.55
#     elif station == 'hrn': latitude = 74.28
#     elif station == 'cbb': latitude = 76.13
#     elif station =='res': latitude = 81.84

#     x = np.append(x, mean)
#     y = np.append(y, latitude)

# x = x.reshape((-1, 1))
# model = LinearRegression().fit(x, y)
# r_sq = model.score(x, y)

stations = ['kir','abk','ups','brw','cbb','blc','lyc', 'nur', 'hrn', 'wic','clf','bdv','iqa','sit','fcc','shu','cmo','res','hlp','bel']

plt.figure(dpi=300)
# ax1 = np.array([0, 40])
# ax2 = np.array([model.intercept_, 40*model.coef_[0] + model.intercept_])
# plt.plot(ax2, ax1,'--', label = 'Expected values')
# plt.legend(fontsize=8, loc='upper left')
title ='Average Standard Deviation of B(H) in function of the geomagnetic latitude\nSeptember 2020'
plt.title(title, fontsize=10)
plt.xlabel('Geomagnetic Latitude (°)')
plt.ylabel('nT')
for station in stations:
    filename = folder + station +  year + extension_hdf
    magdata = pd.read_hdf(filename, 'data')

    std_H = np.array([])
    for i in range(0, 2592000, 10800):
        std_H = np.append(std_H, np.nanstd(magdata[station.upper() + '_H'].iloc[i:i+10799]))
    mean = np.nanmean(std_H)
    if station == 'wic': latitude = 46.43
    elif station == 'frd': latitude = 47.54
    elif station == 'bdv': latitude = 48.75
    elif station == 'clf': latitude = 49.61
    elif station == 'hlp': latitude = 53.31
    elif station == 'bel': latitude = 50.31
    elif station == 'shu': latitude = 54.29
    elif station == 'ott': latitude = 54.75
    elif station == 'stj': latitude = 56.26
    elif station == 'ups': latitude = 58.53
    elif station == 'nur': latitude = 58.06
    elif station == 'sit': latitude = 60.25
    elif station == 'lyc': latitude = 62.82
    elif station == 'cmo': latitude = 64.84
    elif station == 'abk': latitude = 66.28
    elif station == 'kir': latitude = 65.58
    elif station == 'fcc': latitude = 66.47
    elif station == 'ykc': latitude = 68.59
    elif station == 'brw': latitude = 70.07
    elif station == 'ded': latitude = 70.47
    elif station == 'iqa': latitude = 72.29
    elif station == 'blc': latitude = 72.55
    elif station == 'hrn': latitude = 74.28
    elif station == 'cbb': latitude = 76.13
    elif station == 'res': latitude = 81.84

    plt.scatter(latitude, mean)
    plt.annotate(station.upper(), # Text
                  (latitude, mean), # these are the coordinates to position the label
                  textcoords="offset points", # how to position the text
                  xytext=(0,5), # distance from text to points (x,y)
                  ha='center', # horizontal alignment can be left, right or center
                  fontsize=6)

plt.xlim([45,83])
plt.ylim([4,56])
if save:
    plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Linear Regression/Linear Regression of B_H in function of geomagnetic latitude.png', dpi=300, bbox_inches='tight')
plt.show()
