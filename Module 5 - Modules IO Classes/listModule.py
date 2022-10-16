# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:05:23 2016

@author: harora1
"""

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