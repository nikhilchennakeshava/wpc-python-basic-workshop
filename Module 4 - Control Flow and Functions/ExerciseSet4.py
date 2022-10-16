# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:05:41 2016

@author: hina
"""

print ("-"*11)

num = 10

print ("before if statement")

if (num==10):
    print ("inside if statement")
    print (num)

print ("after if statement")

print ("-"*11)

num = 20

print ("before if statement")

if (num==10):
    print ("inside if statement")
    print (num)

print ("after if statement")

print ("-"*11)

num1 = 10
num2 = 20

print ("before if statement")

if (num1==10 and num2==10):
    print ("inside if statement")
    print (num1, num2)

print ("after if statement")

print ("-"*11)

num1 = 10
num2 = 20

print ("before if statement")

if (num1==10 or num2==10):
    print ("inside if statement")
    print (num1, num2)

print ("after if statement")

print ("-"*11)

UserXRatingsD = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}

print ("before if statement")

if ('Z' in UserXRatingsD.keys()):
    print("key found")

print ("after if statement")

print ("-"*11)

for i in range(10):
    if (i%2==0):
        print(i)

print ("-"*11)

UserXRatingsD = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
UserYRatingsD = {'A':10, 'B':20, 'D':40, 'E':50}

for k in sorted(UserXRatingsD.keys()):
    if (k in UserYRatingsD.keys()):
        print(k, UserXRatingsD[k], UserYRatingsD[k])

print ("-"*11)

UserXRatings = [1, 2, 3, 4, 5]
UserYRatings = [10, 20, 30, 40, 50]

for x, y in zip(UserXRatings, UserYRatings):
    print(x,y)

print ("-"*11)

