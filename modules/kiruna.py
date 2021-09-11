# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:47:36 2021
@author: Bastien Longeon
"""
import pandas as pd
import numpy as np

colnumber = [(31, 40),   # X [nT]
             (41, 50),   # Y [nT]
             (51, 60)]   # Z [nT]
station = 'kir'

columnx = station.upper() + '_X'
columny = station.upper() + '_Y'
columnz = station.upper() + '_Z'
columnh = station.upper() + '_H'
colnames = [columnx, columny, columnz]
magdata = pd.read_fwf('D:/Téléchargements/kir202003dsec.sec', skiprows=13, colspecs=colnumber, names=colnames)
magdata[columnx].replace(to_replace= 99999.0, value=np.nan, inplace=True)
magdata[columny].replace(to_replace= 99999.0, value=np.nan, inplace=True)
magdata[columnz].replace(to_replace= 99999.0, value=np.nan, inplace=True)
magdata[columnh] = np.sqrt(magdata[columnx]*magdata[columnx] + magdata[columny]*magdata[columny])
magdata.to_hdf('D:/Documents/GitHub/auroral_indexes/maggraphs/kir202103sec.hdf5', 'data', mode='w')
