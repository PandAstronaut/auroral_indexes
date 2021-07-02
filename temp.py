# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:35:41 2021
@author: Bastien Longeon
"""
import pandas as pd
import numpy as np
import modules.auroral_index_functions as aur

folder = 'maggraphs/'
station = 'abk'
columnx = station.upper() + '_X'
columny = station.upper() + '_Y'
columnz = station.upper() + '_Z'
columnh = station.upper() + '_H'

for year in range(2014,2021): # Year: 2011 to 2020
    print(year)
    filename = folder + station + str(year) + '09sec.hdf5' # Corresponds to the path + filename
    magdata = pd.read_hdf(filename, 'data')
    auroral_index = pd.read_hdf(filename, 'index')

    # ####              Auroral Index 1              ####
    # auroral_index['Auroral_Index_1_1_Z'] = aur.auroral_index1_1(magdata, columnz)
    # auroral_index['Auroral_Index_1_1_H'] = aur.auroral_index1_1(magdata, columnh)
    # auroral_index['Auroral_Index_1_2_X'] = aur.auroral_index1_2(magdata, columnx)
    # auroral_index['Auroral_Index_1_2_Y'] = aur.auroral_index1_2(magdata, columny)
    # auroral_index['Auroral_Index_1_2_Z'] = aur.auroral_index1_2(magdata, columnz)
    # auroral_index['Auroral_Index_1_2_H'] = aur.auroral_index1_2(magdata, columnh)

    #                 ###              Auroral Index 2              ###
    # auroral_index['Auroral_Index_2_X'] = aur.auroral_index2(magdata, columnx, year)
    # auroral_index['Auroral_Index_2_Y'] = aur.auroral_index2(magdata, columny, year)
    # auroral_index['Auroral_Index_2_Z'] = aur.auroral_index2(magdata, columnz, year)
    # auroral_index['Auroral_Index_2_H'] = aur.auroral_index2(magdata, columnh, year)

    # These replacements avoid log10(0) or inf errors without modifying the plots
    auroral_index['Auroral_Index_1_2_X'].replace(to_replace=0, value=np.nan, inplace=True)
    auroral_index['Auroral_Index_1_2_Y'].replace(to_replace=0, value=np.nan, inplace=True)
    auroral_index['Auroral_Index_1_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)
    # auroral_index['Auroral_Index_2_X'].replace(to_replace=0, value=np.nan, inplace=True)
    # auroral_index['Auroral_Index_2_Y'].replace(to_replace=0, value=np.nan, inplace=True)
    # auroral_index['Auroral_Index_2_Z'].replace(to_replace=0, value=np.nan, inplace=True)

                    ###              Auroral Index 1.2: Z/X Z/Y              ####
    auroral_index['Auroral_Index_1_2_Z/X'] = np.sign(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_X'])*np.log10(abs(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_X']))
    auroral_index['Auroral_Index_1_2_Z/Y'] = np.sign(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_Y'])*np.log10(abs(auroral_index['Auroral_Index_1_2_Z']/auroral_index['Auroral_Index_1_2_Y']))

    # ###              (Auroral Index 2: Z/X and Z/Y)             ####
    # auroral_index['DC_ratio_X'] = np.sign(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_X'])*np.log10(abs(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_X']))
    # auroral_index['DC_ratio_Y'] = np.sign(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_Y'])*np.log10(abs(auroral_index['Auroral_Index_2_Z']/auroral_index['Auroral_Index_2_Y']))

    # ###              (dB/dt)/(<dB_1sec>_1min)             ####
    # auroral_index['AC_ratio'] = abs(auroral_index['Auroral_Index_1_1_H'])/auroral_index['Auroral_Index_1_2_H']

    magdata.to_hdf(filename, 'data', mode='w')
    auroral_index.to_hdf(filename, 'index', mode='a')
