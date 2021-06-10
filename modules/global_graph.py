# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:01:33 2021
@Author: Bastien Longeon
"""

def initialize():
    """
    Color will be incremented each time a plot is drawn so that the
    color always changes.
    """
    global color
    color = 0
    global mark
    mark = 0
