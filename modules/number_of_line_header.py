# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:13:01 2021
@author: Bastien Longeon
    Reading the header comment lines and define its length
"""

filePath = "maggraphs/kir202104dsec.sec" #put your own filePath
with open(filePath, 'r') as file: #Determination of the number of rows to skip before the datas
    comments_size = 0
    for row in file:
        comments_size += 1
        if "DATE" in row: #the >50 is here to avoid reading the whole documents
            break
        if comments_size > 50:
            print("The end of the header has not been found.")
            break
