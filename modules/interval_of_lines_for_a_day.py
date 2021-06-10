# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:34:09 2021
@author: Bastien Longeon
    Code to find the lines number of a specific day
"""

import linecache      #To read a specific line in a file

folder = "maggraphs/"
filename = "kir201709dsec.sec"
filePath = folder + filename

with open(filePath, 'r') as file: #Determination of the position of the 2017/09/08 data
    starting_line = 0
    for row in file:
        starting_line += 1
        if "-08" in row: 
            starting_line
            break #searching for the first measure on the 09/08
end_line = 86400 + starting_line -1 #Last line of the day

## The following lines reads the first and last line we are reading ###
print(end_line)
particular_line = linecache.getline(filePath, starting_line)
print(particular_line)  
particular_line = linecache.getline(filePath, end_line)
print(particular_line) 