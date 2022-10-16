# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:38:34 2015

@author: hina
"""

print()

import math

# Minkowski Distance between two vectors
def minkowksiD(ratings1, ratings2, r):
    
    # calcualte minkowski distance
    distance = 0       
    for item in ratings1.keys():
        # consider item rating only if 
        # both users have rated item
        if item in ratings2.keys():
            x = ratings1[item]
            y = ratings2[item]
            distance += pow(abs(x - y), r)
    
    # return value of minkowski distance
    return pow(distance,1/r)

UserXRatings = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
UserYRatings = {'A':10, 'B':20, 'D':40, 'E':50}

md = minkowksiD(UserXRatings, UserYRatings, 1)
print ("Manhattan Distance: ", round(md,2))

md = minkowksiD(UserXRatings, UserYRatings, 2)
print ("Euclidean Distance: ", round(md,2))

md = minkowksiD(UserXRatings, UserYRatings, 3)
print ("Minkowski Distance (r=3): ", round(md,2))
