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
               2020:100,
               2021:107}

offsetZ_kir = {2011:51657,
               2012:51695,
               2013:51725,
               2014:51750,
               2015:51800,
               2016:51847,
               2017:51918,
               2018:51950,
               2019:52000,
               2020:52055,
               2021:52030}

offsetH_kir = {2011:10700,
               2012:10680,
               2013:10680,
               2014:10650,
               2015:10640,
               2016:10640,
               2017:10600,
               2018:10588,
               2019:10584,
               2020:10560,
               2021:10560}

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
               2020:11250,
               2021:11250}

offsetY_abk = {2014:1600,
               2015:1650,
               2016:1690,
               2017:1725,
               2018:1800,
               2019:1850,
               2020:1890,
               2021:1900}

offsetZ_abk = {2014:51880,
               2015:51935,
               2016:51970,
               2017:52025,
               2018:52075,
               2019:52110,
               2020:52200,
               2021:52200}

offsetH_abk = {2014:11470,
               2015:11450,
               2016:11450,
               2017:11450,
               2018:11430,
               2019:11420,
               2020:11400,
               2021:11400}

offsetY_blc = {2011:-350,
               2012:-360,
               2013:-360,
               2014:-360,
               2015:-350,
               2016:-350,
               2017:-330,
               2018:-300,
               2019:-290,
               2020:-270}

offsetZ_blc = {2011:58740,
               2012:58640,
               2013:58540,
               2014:58460,
               2015:58400,
               2016:58300,
               2017:58230,
               2018:58125,
               2019:58050,
               2020:58000}

offsetH_blc = {2011:6450,
               2012:6540,
               2013:6600,
               2014:6650,
               2015:6750,
               2016:6800,
               2017:6875,
               2018:6950,
               2019:7000,
               2020:7075}

offsetX_lyc = {2017:12970,
               2020:12950,
               2021:12940}

offsetY_lyc = {2017:1700,
               2020:1820,
               2021:1840}

offsetZ_lyc = {2017:50700,
               2020:50850,
               2021:50885}

offsetH_lyc = {2017:13100,
               2020:13070,
               2021:13070}

offsetX_brw = {2019:8875,
               2020:8920}

offsetY_brw = {2011:-115,
               2012:-43,
               2013:-75,
               2014:-10,
               2015:-40,
               2016:-20,
               2017:-60,
               2018:-90,
               2019:2075,
               2020:2000}

offsetZ_brw = {2011:56850,
               2012:56900,
               2013:56910,
               2014:56900,
               2015:56880,
               2016:56870,
               2017:56840,
               2018:56775,
               2019:56600,
               2020:56535}

offsetH_brw = {2011:9525,
               2012:9200,
               2013:9180,
               2014:9150,
               2015:9175,
               2016:9175,
               2017:9200,
               2018:9200,
               2019:9150,
               2020:9150}

offsetY_ups = {2011:1275,
               2012:1320,
               2013:1370,
               2014:1410,
               2015:1460,
               2016:1510,
               2017:1560,
               2018:1615,
               2019:1665,
               2020:1715,
               2021:1740}

offsetZ_ups = {2011:48930,
               2012:48970,
               2013:49000,
               2014:49030,
               2015:49075,
               2016:49125,
               2017:49170,
               2018:49223,
               2019:49275,
               2020:49330,
               2021:49360}

def auroral_index1_min (magdata, data):
    mean = list()
    days = int(len(magdata)/1440)
    for k in range(days):
        for h in range(0,24): # For each hour in a day
            for m in range(0,60): # For each minute every hour
                mean.append((magdata[data].iloc[m + 60*h + k*1440] - magdata[data].iloc[m+1 + 60*h + k*1440])/60)
    return mean

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
                                = <|dB_1sec|>_1min
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
    if data[0:3] == 'BLC':
        if data[-1].lower() == 'x' or data[-1].lower() == 'h':
            b0 = offsetH_blc[year]
        if data[-1].lower() == 'y':
            b0 = offsetY_blc[year]
        if data[-1].lower() == 'z':
            b0 = offsetZ_blc[year]
    if data[0:3] == 'BRW':
        if data[-1].lower() == 'x':
            if year < 2019 : b0 = offsetH_brw[year]
            else: b0 = offsetX_brw[year]
        if data[-1].lower() == 'y':
            b0 = offsetY_brw[year]
        if data[-1].lower() == 'z':
            b0 = offsetZ_brw[year]
        if data[-1].lower() == 'h':
             b0 = offsetH_brw[year]
    if data[0:3] == 'UPS':
        if data[-1].lower() == 'x':
            if year == 2021:
                b0 = 15085
            else:
                b0 = 15122.5
        if data[-1].lower() == 'y':
            b0 = offsetY_ups[year]
        if data[-1].lower() == 'z':
            b0 = offsetZ_ups[year]
        if data[-1].lower() == 'h':
             b0 = 15196
    if data[0:3] == 'LYC':
        if data[-1].lower() == 'x':
            b0 = offsetX_lyc[year]
        if data[-1].lower() == 'y':
            b0 = offsetY_lyc[year]
        if data[-1].lower() == 'z':
            b0 = offsetZ_lyc[year]
        if data[-1].lower() == 'h':
             b0 = offsetH_lyc[year]
    if data[0:3] == 'NUR':
        if data[-1].lower() == 'x':
            b0 = 14735
        if data[-1].lower() == 'y':
            b0 = 2315
        if data[-1].lower() == 'z':
            b0 = 50365
        if data[-1].lower() == 'h':
             b0 = 14920
    if data[0:3] == 'HRN':
        if data[-1].lower() == 'x':
            b0 = 7800
        if data[-1].lower() == 'y':
            b0 = 1050
        if data[-1].lower() == 'z':
            b0 = 54050
        if data[-1].lower() == 'h':
             b0 = 7850
    if data[0:3] == 'HLP':
        if data[-1].lower() == 'x':
            b0 = 17470
        if data[-1].lower() == 'y':
            b0 = 1730
        if data[-1].lower() == 'z':
            b0 = 47440
        if data[-1].lower() == 'h':
             b0 = 17555
    if data[0:3] == 'BEL':
        if data[-1].lower() == 'x':
            b0 = 18910
        if data[-1].lower() == 'y':
            b0 = 2185
        if data[-1].lower() == 'z':
            b0 = 46787
        if data[-1].lower() == 'h':
             b0 = 19035
    if data[0:3] == 'WIC':
        if data[-1].lower() == 'x':
            b0 = 21000
        if data[-1].lower() == 'y':
            b0 = 1685
        if data[-1].lower() == 'z':
            b0 = 43952
        if data[-1].lower() == 'h':
             b0 = 21070
    if data[0:3] == 'CLF':
        if data[-1].lower() == 'x':
            b0 = 21260
        if data[-1].lower() == 'y':
            b0 = 420
        if data[-1].lower() == 'z':
            b0 = 43065
        if data[-1].lower() == 'h':
             b0 = 21270
    if data[0:3] == 'BDV':
        if data[-1].lower() == 'x':
            b0 = 20415
        if data[-1].lower() == 'y':
            b0 = 1510
        if data[-1].lower() == 'z':
            b0 = 44415
        if data[-1].lower() == 'h':
             b0 = 20470
    if data[0:3] == 'IQA':
        if data[-1].lower() == 'x':
            b0 = 8620
        if data[-1].lower() == 'y':
            b0 = -4070
        if data[-1].lower() == 'z':
            b0 = 55990
        if data[-1].lower() == 'h':
             b0 = 9540
    if data[0:3] == 'SIT':
        if data[-1].lower() == 'x':
            b0 = 15020
        if data[-1].lower() == 'y':
            b0 = 5000
        if data[-1].lower() == 'z':
            b0 = 52902
        if data[-1].lower() == 'h':
             b0 = 15830
    if data[0:3] == 'FCC':
        if data[-1].lower() == 'x':
            b0 = 9610
        if data[-1].lower() == 'y':
            b0 = -210
        if data[-1].lower() == 'z':
            b0 = 56395
        if data[-1].lower() == 'h':
             b0 = 9610
    if data[0:3] == 'SHU':
        if data[-1].lower() == 'x':
            b0 = 19455
        if data[-1].lower() == 'y':
            b0 = 3420
        if data[-1].lower() == 'z':
            b0 = 48151
        if data[-1].lower() == 'h':
             b0 = 19755
    if data[0:3] == 'CMO':
        if data[-1].lower() == 'x':
            b0 = 12100
        if data[-1].lower() == 'y':
            b0 = 3630
        if data[-1].lower() == 'z':
            b0 = 55020
        if data[-1].lower() == 'h':
             b0 = 12635
    if data[0:3] == 'RES':
        if data[-1].lower() == 'x':
            b0 = 2800
        if data[-1].lower() == 'y':
            b0 = -940
        if data[-1].lower() == 'z':
            b0 = 57400
        if data[-1].lower() == 'h':
             b0 = 2960
    if data[0:3] == 'OTT':
        if data[-1].lower() == 'x':
            b0 = 18040
        if data[-1].lower() == 'y':
            b0 = -4290
        if data[-1].lower() == 'z':
            b0 = 50695
        if data[-1].lower() == 'h':
             b0 = 18540
    if data[0:3] == 'YKC':
        if data[-1].lower() == 'x':
            b0 = 9120
        if data[-1].lower() == 'y':
            b0 = 2630
        if data[-1].lower() == 'z':
            b0 = 57220
        if data[-1].lower() == 'h':
             b0 = 9480
    if data[0:3] == 'STJ':
        if data[-1].lower() == 'x':
            b0 = 19240
        if data[-1].lower() == 'y':
            b0 = -6020
        if data[-1].lower() == 'z':
            b0 = 46710
        if data[-1].lower() == 'h':
             b0 = 20160
    if data[0:3] == 'FRD':
        if data[-1].lower() == 'x':
            b0 = 21230
        if data[-1].lower() == 'y':
            b0 = -3955
        if data[-1].lower() == 'z':
            b0 = 45897
        if data[-1].lower() == 'h':
             b0 = 21595

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
