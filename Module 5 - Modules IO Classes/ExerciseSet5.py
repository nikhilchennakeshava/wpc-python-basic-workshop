# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:14:24 2016

@author: harora1
"""

print ("-"*11)

lstA = [1, 2, 3, 4, 5]
lstB = [10, 20, 30, 40, 50]

lstC = []
for a, b in zip(lstA, lstB):
    lstC.append(a+b)
print (lstC)

print ("-"*11)

def addLists (lst1, lst2):
    lst = []    
    for l1, l2 in zip(lst1, lst2):
        lst.append(l1+l2)
    return (lst)

lstA = [1, 2, 3, 4, 5]
lstB = [10, 20, 30, 40, 50]

lstC = addLists (lstA, lstB)
print (lstC)

print ("-"*11)

class listComposites:

    def __init__(self, lst1, lst2):
        self.list1 = lst1
        self.list2 = lst2
    
    def addLists(self):
        lst = []
        for l1, l2 in zip(self.list1, self.list2):
            lst.append(l1+l2)
        return (lst)

    def subLists(self):
        lst = []
        for l1, l2 in zip(self.list1, self.list2):
            lst.append(l1-l2)
        return (lst)

lstA = [1, 2, 3, 4, 5]
lstB = [10, 20, 30, 40, 50]

lc = listComposites(lstA, lstB)

lstC = lc.addLists()
print (lstC)

lstC = lc.subLists()
print (lstC)

print ("-"*11)



