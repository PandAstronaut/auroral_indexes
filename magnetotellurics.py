# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 17:59:05 2021
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
t = np.arange(0, 3600, dt)

stations = ['abk', 'kir']
years = ['2017','2020','2021']
components =['_H', '_Z']

# std = []
for component in components:
    if component == '_H':
        std_min = .5
        std_max = 250
    else:
        std_min = .3
        std_max = 300
    for year in years:
        if year == '2021': month ='03'
        else: month = '09'
        for i in range(720): # 720h in a month
            station = 'abk'
            filename = folder + station +  year + month +  extension_hdf
            magdata = pd.read_hdf(filename, 'data', start=3600*i, stop=3600*(i+1))
            s = magdata[station.upper() + component] # Signal
            # std.append(np.nanstd(s))

            if np.nanstd(s) < std_min or np.nanstd(s) > std_max:
                for station in stations:
                    if station == 'abk':
                        station_name = 'Abisko'
                        if np.nanstd(s) < std_min: cheat = True # To know if there is or isn't activity
                        else: cheat = False
                    elif station == 'kir': station_name = 'Kiruna'
                    if station != 'abk': # To not read the data twice
                        filename = folder + station +  year + month +  extension_hdf
                        magdata = pd.read_hdf(filename, 'data', start=3600*i, stop=3600*(i+1))
                        s = magdata[station.upper() + component] # Signal
                    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(7, 7), dpi=300)
                    day = int(i/24)
                    date = str(day)+'/'+month+'/'+year+' from ' + str(i-day*24) + 'h to ' + str(1 + i-day*24) + 'h'
                    if cheat:
                        title = station_name + ' - No activity - B('+component[1]+')\n' + date
                    else:
                        title = station_name + ' - Very High activity - B('+component[1]+')\n' + date
                    fig.suptitle(title)

                    # plot time signal:
                    axs[0, 0].set_title("Signal", loc='right')
                    axs[0, 0].plot(t, s, color='C0', linewidth=.4)
                    axs[0, 0].set_xlabel("Time [s]")
                    axs[0, 0].set_ylabel("Amplitude")
                    axs[0, 0].set_xlim([0, len(s)])

                    # plot different spectrum types:
                    axs[1, 0].set_title("Magnitude Spectrum")
                    axs[1, 0].magnitude_spectrum(s, Fs=Fs, color='C1', linewidth=1)
                    axs[1, 0].set_xlim([-0.01, .5])

                    axs[1, 1].set_title("Log. Magnitude Spectrum")
                    axs[1, 1].magnitude_spectrum(s, Fs=Fs, scale='dB', color='C1', linewidth=.4)
                    axs[1, 1].set_xlim([-0.01, .5])

                    axs[2, 0].set_title("Phase Spectrum ")
                    axs[2, 0].phase_spectrum(s, Fs=Fs, color='C2', linewidth=.8)
                    axs[2, 0].set_xlim([0, .5])

                    axs[2, 1].set_title("Angle Spectrum")
                    axs[2, 1].angle_spectrum(s, Fs=Fs, color='C2', linewidth=.1)
                    axs[2, 1].set_xlim([0, .5])

                    axs[0, 1].remove()  # don't display empty ax
                    fig.tight_layout()

                    if save:
                        date = year +'.'+ month +'.'+ str(day) +' from ' + str(i-day*24) + 'h to ' + str(1 + i-day*24) + 'h'
                        if cheat:
                            title ='No activity - ' + date +' - ' + station.upper() +component
                            plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Spectral Analysis/' + title  + '.png', dpi=300, bbox_inches='tight')
                        else:
                            title ='Very High Activity - ' + date +' - ' + station.upper() +component
                            plt.savefig('D:/Documents/GitHub/auroral_indexes/Plots/Spectral Analysis/' + title  + '.png', dpi=300, bbox_inches='tight')
                    plt.show()



###              ExecutionTime time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
