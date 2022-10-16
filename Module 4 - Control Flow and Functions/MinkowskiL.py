# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:38:34 2015

@author: hina
"""

print()

import math

# Minkowski Distance between two vectors
def minkowksiL(ratings1, ratings2, r):
    
    # error check
    if (r <= 0):
        print ("r<=0; returning -2 distance!")
        return -2
    
    # calcualte minkowski distance
    distance = 0       
    for x, y in zip(ratings1, ratings2):
        distance += pow(abs(x - y), r)
    
    # return value of minkowski distance
    return pow(distance,1/r)

UserXRatings = [1, 2, 3, 4, 5]
UserYRatings = [10, 20, 30, 40, 50]

md = minkowksiL(UserXRatings, UserYRatings, 1)
print ("Manhattan Distance: ", round(md,2))

md = minkowksiL(UserXRatings, UserYRatings, 2)
print ("Euclidean Distance: ", round(md,2))

md = minkowksiL(UserXRatings, UserYRatings, 3)
print ("Minkowski Distance (r=3): ", round(md,2))
