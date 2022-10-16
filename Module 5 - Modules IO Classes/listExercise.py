# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:22:08 2016

@author: harora1
"""

print ("-"*11)

import listModule

lstA = [1, 2, 3, 4, 5]
lstB = [10, 20, 30, 40, 50]

lc = listModule.listComposites(lstA, lstB)

lstC = lc.addLists()
print (lstC)

lstC = lc.subLists()
print (lstC)

print ("-"*11)