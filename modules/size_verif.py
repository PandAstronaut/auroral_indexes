# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 12:21:20 2021
@author: Bastien Longeon

This code verifies that the length of the sec file is appropriate and fill it
with errors if it's not the case.
This code does not take into account the possibility of empty spaces inside a
day. It only fills new rows at the end of the day.
"""
import time
startTime = time.time()

station = 'ups'
folder = 'maggraphs/sec files/'
extension_sec = '.sec'


for year in range(2012,2021): # Year: 11 to 21
    print('Processing data from {}'.format(year))
    for i in range(0,30): # Day in september: 0 to 30
        if i < 9: day = '0' + str(i+1)
        else : day = str(i+1)
        date = str(year) + '09' + day
        filename = folder + station +  date + extension_sec
        with open(filename) as file:
            for row in file:
                if "DATE" in row: break
            lines = 86400 - sum(1 for _ in file)
            if lines > 0:
                print(i+1,year)
                with open(filename, 'a') as file:
                    file.write(row.replace(row,'####-##-## ##:##:##.### ###      nan       nan      nan       nan     \n'))
                    for k in range(lines - 1):
                        file.write('####-##-## ##:##:##.### ###      nan       nan      nan       nan     \n')
            file.close()
            ###              Execution time              ####
executionTime = (time.time() - startTime)
print("Execution time: {0:.2f}s".format(executionTime))
