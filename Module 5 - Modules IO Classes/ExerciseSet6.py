# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:01:21 2017

@author: harora1
"""
print ()

print ("-"*11)

var = [45, 30, 21, 50]

sortvar = sorted(var)
print (sortvar)

sortvar = sorted(var, reverse=True)
print (sortvar)

print ("-"*11)

from operator import itemgetter

var = [('Car',45), ('Amy',30), ('Zach',21), ('Jane',50)]

sortvar = sorted(var)
print (sortvar)

sortvar = sorted(var, key=itemgetter(1))
print (sortvar)

sortvar = sorted(var, key=itemgetter(1), reverse=True)
print (sortvar)

print ("-"*11)

from operator import itemgetter

var = {'Car':45, 'Amy':30, 'Zach':21, 'Jane':50}

sortvar = sorted(var.items())
print (sortvar)

sortvar = sorted(var.items(), key=itemgetter(1))
print (sortvar)

sortvar = sorted(var.items(), key=itemgetter(1), reverse=True)
print (sortvar)

print ("-"*11)

nl = [[10,20,30],[100,200,300,400],[1000,2000,3000,4000,5000]]

for i in range(len(nl)):
    for j in range(len(nl[i])):
        print ("elelment", i,j, "is:", nl[i][j])
    print ("---")

print ("-"*11)

IMDB = {
    'Alfred Hitchcock': {'Family Plot': '6.8', 'Rebecca': '8.2', 'Spellbound': '7.6'}, 
    'Mel Gibson': {'Apocalypto': '7.8', 'Braveheart': '8.4'}, 
    'Mel Brooks': {'Spaceballs': '7.1', 'History of the World: Part I': '6.9'}, 
    'Ang Lee': {'Life of Pi': '8', 'The Ice Storm': '7.5'}, 
    'J.J. Abrams': {'Star Trek': '8', 'Star Trek Into Darkness': '7.8'}, 
    'Clint Eastwood': {'J. Edgar': '6.6', 'The Bridges of Madison County': '7.5'}}

for director, movieRatings in IMDB.items():
    print (director)
    for movie, rating in movieRatings.items():
        print (movie, rating)
    print ("---")
    
print ("-"*11)