# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:15:24 2021
@author: Bastien Longeon
"""

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
    for h in range(0,24): # For each hour in a day
        for m in range(0,60): # For each minute every hour
            mean.append((magdata[data].iloc[60*m + 3600*h] - magdata[data].iloc[59 + 60*m +3600*h])/60)
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
    for h in range(0,24): # For each hour in a day
        for m in range(0,60): # For each minute every hour
            x = 0
            for i in range(0,59): # Calculate the mean value for a minute
                x += abs(magdata[data].iloc[i + 60*m + 3600*h] - magdata[data].iloc[i+1 + 60*m + 3600*h])
            mean.append(x/59) # Add the value to a list
    return mean # We actually return dBAC(2) = <dB_1s(t-60s):dB_1s(t)>


def auroral_index2 (magdata,range_min, range_max, data):
    """
                            AURORAL INDEX 2:
                            dBDC = <B>_1min – B0
    Parameters
    ----------
    magdata : DataFrame
        DF of all the magnetometer data
    range_min : int
    range_max : int
        range_min/max defines the period where the activity is minimal to null
        to compute B0.
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
    x = 0
    for i in range(range_min, range_max):
        x += magdata[data].iloc[i]
    b0 = int(x/len(range(range_min,range_max))) # int for more simplicity

    mean = list()
    for h in range(0,24): # For each hour in a day
        for m in range(0,60): # For each minute every hour
            x = 0
            for i in range(0,60): # Calculate the mean value for a minute
                x += magdata[data].iloc[i + 60*m + 3600*h]
            mean.append(x/60) # Add the value to a list
    mean = [n - b0 for n in mean] # Doing the same operation for each cell in the list
    return mean # We actually return BDC = <B>_1min – B0