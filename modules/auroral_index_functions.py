# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:15:24 2021
@author: Bastien Longeon
"""
offsetY_kir = {2011:-260,
               2012:-220,
               2013:-180,
               2014:-140,
               2015:-100,
               2016:-60,
               2017:0,
               2018:40,
               2019:80,
               2020:100}

offsetZ_kir = {2011:51657,
               2012:51695,
               2013:51725,
               2014:51750,
               2015:51800,
               2016:51847,
               2017:51918,
               2018:51950,
               2019:52000,
               2020:52055}

offsetH_kir = {2011:10700,
               2012:10680,
               2013:10680,
               2014:10650,
               2015:10640,
               2016:10640,
               2017:10600,
               2018:10588,
               2019:10584,
               2020:10560}

offsetX_cbb = {2011:4420,
               2012:4500,
               2013:4580,
               2014:4660,
               2016:4795,
               2017:4860,
               2018:4950,
               2019:5000,
               2020:5090}

offsetY_cbb = {2011:540,
               2012:510,
               2013:500,
               2014:490,
               2016:475,
               2017:480,
               2018:570,
               2019:580,
               2020:590}

offsetZ_cbb = {2011:58700,
               2012:58635,
               2013:58565,
               2014:58480,
               2016:58330,
               2017:58275,
               2018:58210,
               2019:58140,
               2020:58080}

offsetH_cbb = {2011:4450,
               2012:4520,
               2013:4615,
               2014:4680,
               2016:4820,
               2017:4875,
               2018:4980,
               2019:5060,
               2020:5140}

offsetX_abk = {2014:11350,
               2015:11340,
               2016:11340,
               2017:11350,
               2018:11280,
               2019:11270,
               2020:11250}

offsetY_abk = {2014:1600,
               2015:1650,
               2016:1690,
               2017:1725,
               2018:1800,
               2019:1850,
               2020:1890}

offsetZ_abk = {2014:51880,
               2015:51935,
               2016:51970,
               2017:52025,
               2018:52075,
               2019:52110,
               2020:52200}

offsetH_abk = {2014:11470,
               2015:11450,
               2016:11450,
               2017:11450,
               2018:11430,
               2019:11420,
               2020:11400}

def auroral_index1_1 (magdata, data):
    """
                        AURORAL INDEX 1_1:
                        dBAC(1) = <dB/dt>_1min
                                = [B(t-60sec) - B(t)]/60
    Parameters
    ----------
    magdata : DataFrame
        DF of all the magnetometer data
    data : string
        data corresponds to the string colname of the data we want to work with.
        i.e. KIR_H.
    Returns
    -------
    mean : list
    This functions returns the first version of auroral index 1 for a specific day.
    range(0,60) is actually 0 to 59 so 60 iterations
    """
    mean = list()
    days = int(len(magdata)/86400)
    for k in range(days):
        for h in range(0,24): # For each hour in a day
            for m in range(0,60): # For each minute every hour
                mean.append((magdata[data].iloc[60*m + 3600*h + k*86400] - magdata[data].iloc[59 + 60*m +3600*h + k*86400])/60)
    return mean # We actually return dBAC(1) = [B(t-60sec) - B(t)]/60

def auroral_index1_2 (magdata, data):
    """
                            AURORAL INDEX 1_2:
                        dBAC(2) = <|dB/dt|>_1min
                                = <dB_1sec>_1min
                                = ave(dB_1s(t-60s):dB_1s(t))
                                where dB_1s(t) = |dB(t-1s) - dB(t)|

    This functions returns the first version of auroral index 1 for a specific day.
    """
    mean = list()
    x = 0
    days = int(len(magdata)/86400)
    for k in range(days):
        for h in range(0,24): # For each hour in a day
            for m in range(0,60): # For each minute every hour
                x = 0
                for i in range(0,59): # Calculate the mean value for a minute
                    x += abs(magdata[data].iloc[i + 60*m + 3600*h + k*86400] - magdata[data].iloc[i+1 + 60*m + 3600*h + k*86400])
                mean.append(x/59) # Add the value to a list
    return mean # We actually return dBAC(2) = <dB_1s(t-60s):dB_1s(t)>


def auroral_index2 (magdata, data, year):
    """
                            AURORAL INDEX 2:
                            dBDC = <B>_1min – B0
    Parameters
    ----------
    magdata : DataFrame
        DF of all the magnetometer data
    data : string
        data corresponds to the string colname of the data we want to work with.
        i.e. KIR_H.
    Returns
    -------
    mean : list
        This functions returns the second auroral index for a specific day.

    iloc is used to access a specific index in a DataFrame
    range(0,60) is actually 0 to 59 so 60 iterations
    """
    if data[0:3] == 'KIR':
        if data[-1].lower() == 'x' or data[-1].lower() == 'h':
            b0 = offsetH_kir[year]
        if data[-1].lower() == 'y':
            b0 = offsetY_kir[year]
        if data[-1].lower() == 'z':
            b0 = offsetZ_kir[year]
    if data[0:3] == 'CBB':
        if data[-1].lower() == 'x':
            b0 = offsetX_cbb[year]
        if data[-1].lower() == 'y':
            b0 = offsetY_cbb[year]
        if data[-1].lower() == 'z':
            b0 = offsetZ_cbb[year]
        if data[-1].lower() == 'h':
             b0 = offsetH_cbb[year]
    if data[0:3] == 'ABK':
        if data[-1].lower() == 'x':
            b0 = offsetX_abk[year]
        if data[-1].lower() == 'y':
            b0 = offsetY_abk[year]
        if data[-1].lower() == 'z':
            b0 = offsetZ_abk[year]
        if data[-1].lower() == 'h':
             b0 = offsetH_abk[year]

    mean = list()
    days = int(len(magdata)/86400)
    for k in range(days):
        for h in range(0,24): # For each hour in a day
            for m in range(0,60): # For each minute every hour
                x = 0
                for i in range(0,60): # Calculate the mean value for a minute
                    x += magdata[data].iloc[i + 60*m + 3600*h + k*86400]
                mean.append(x/60) # Add the value to a list
    mean = [n - b0 for n in mean] # Doing the same operation for each cell in the list
    return mean # We actually return BDC = <B>_1min – B0
