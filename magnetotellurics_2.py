# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 10:30:46 2021
@author: Bastien Longeon
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
startTime = time.time()

save = False

folder = "maggraphs/"
extension_hdf = 'sec.hdf5'

np.random.seed(0)

dt = 1  # sampling interval
Fs = 1 / dt  # sampling frequency
t = np.arange(0, 180, dt)

stations = ['kir','abk']
year = '2020'
month = '09'

hours = [642, 667, 689]
for hour in hours:
    i=0
    fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(14, 9), dpi=300)
    for station in stations:
        filename = folder + station +  year + month +  extension_hdf
        auroral_index = pd.read_hdf(filename, 'index', start=60*hour, stop=60*(hour+3))
        s = auroral_index['Auroral_Index_1_2_Z/H']


        day = int(hour/24)
        date = str(day)+'/'+month+'/'+year+' from ' + str(hour-day*24) + 'h to ' + str(3 + hour-day*24) + 'h'
        title = 'Very High activity - log((dB(Z)/dt) / (dB(H)/dt))\n' + date + '\nKIRUNA                                                                      ABISKO'
        fig.suptitle(title, fontsize=20)

        # plot time signal:
        axs[0, 0+i].set_title("Signal")
        axs[0, 0+i].plot(t, s, color='C0', linewidth=1)
        axs[0, 0+i].set_xlabel("Time [s]")
        axs[0, 0+i].set_ylabel("Amplitude")
        axs[0, 0+i].set_xlim([0, len(s)])
        axs[0, 0+i].set_ylim([-1.2,0.7])

        # plot different spectrum types:
        axs[1, 0+i].set_title("Magnitude Spectrum")
        axs[1, 0+i].magnitude_spectrum(s, Fs=Fs, color='C1', linewidth=1)
        axs[1, 0+i].set_xlim([-0.01, .5])
        axs[1, 0+i].set_ylim([0,0.15])

        axs[1, 1+i].set_title("Log. Magnitude Spectrum")
        axs[1, 1+i].magnitude_spectrum(s, Fs=Fs, scale='dB', color='C1', linewidth=1)
        axs[1, 1+i].set_xlim([-0.01, .5])
        axs[1, 1+i].set_ylim([-62,-15])

        axs[2, 0+i].set_title("Phase Spectrum ")
        axs[2, 0+i].phase_spectrum(s, Fs=Fs, color='C2', linewidth=1)
        axs[2, 0+i].set_xlim([0, .5])
        axs[2, 0+i].set_ylim([-45, 25])
        if hour == 689: axs[2, 0+i].set_ylim([-5, 85])


        axs[2, 1+i].set_title("Angle Spectrum")
        axs[2, 1+i].angle_spectrum(s, Fs=Fs, color='C2', linewidth=1)
        axs[2, 1+i].set_xlim([0, .5])
        axs[2, 1+i].set_ylim([-3, 3])

        axs[0, 1+i].remove()  # don't display empty ax
        i = 2
    fig.tight_layout()

    if save:
        date = str(day)+'.'+month+'.'+year+' from ' + str(hour-day*24) + 'h to ' + str(3 + hour-day*24) + 'h'
        plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Spectral Analysis/Very High activity - log((dB(Z).dt).(dB(H).dt))' + date + '.png', dpi=300, bbox_inches='tight')

for hour in hours:
    i=0
    fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(14, 9), dpi=300)
    for station in stations:
        filename = folder + station +  year + month +  extension_hdf
        magdata = pd.read_hdf(filename, 'data', start=60*hour, stop=60*(hour+3))
        s = magdata[station.upper()+'_Z']/magdata[station.upper()+'_H']


        day = int(hour/24)
        date = str(day)+'/'+month+'/'+year+' from ' + str(hour-day*24) + 'h to ' + str(3 + hour-day*24) + 'h'
        title = 'Very High activity - Z/H\n' + date + '\nKIRUNA                                                                      ABISKO'
        fig.suptitle(title, fontsize=20)

        # plot time signal:
        axs[0, 0+i].set_title("Signal")
        axs[0, 0+i].plot(t, s, color='C0', linewidth=1)
        axs[0, 0+i].set_xlabel("Time [s]")
        axs[0, 0+i].set_ylabel("Amplitude")
        axs[0, 0+i].set_xlim([0, len(s)])
        # axs[0, 0+i].set_ylim([-1.2,0.7])

        # plot different spectrum types:
        axs[1, 0+i].set_title("Magnitude Spectrum")
        axs[1, 0+i].magnitude_spectrum(s, Fs=Fs, color='C1', linewidth=1)
        axs[1, 0+i].set_xlim([-0.01, .5])
        # axs[1, 0+i].set_ylim([0,0.15])

        axs[1, 1+i].set_title("Log. Magnitude Spectrum")
        axs[1, 1+i].magnitude_spectrum(s, Fs=Fs, scale='dB', color='C1', linewidth=1)
        # axs[1, 1+i].set_xlim([-0.00000001, 0.00000001])
        # axs[1, 1+i].set_ylim([-62,-15])

        axs[2, 0+i].set_title("Phase Spectrum ")
        axs[2, 0+i].phase_spectrum(s, Fs=Fs, color='C2', linewidth=1)
        axs[2, 0+i].set_xlim([0, .5])
        # axs[2, 0+i].set_ylim([-45, 25])


        axs[2, 1+i].set_title("Angle Spectrum")
        axs[2, 1+i].angle_spectrum(s, Fs=Fs, color='C2', linewidth=1)
        axs[2, 1+i].set_xlim([0, .5])
        # axs[2, 1+i].set_ylim([-3, 3])

        axs[0, 1+i].remove()  # don't display empty ax
        i = 2
    fig.tight_layout()
