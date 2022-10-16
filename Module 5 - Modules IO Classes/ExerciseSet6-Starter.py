# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:01:21 2017

@author: harora1
"""

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

DirectorMovieRatings = {
    'Alfred Hitchcock': {'Family Plot': '6.8', 'Rebecca': '8.2', 'Spellbound': '7.6'}, 
    'Mel Gibson': {'Apocalypto': '7.8', 'Braveheart': '8.4'}, 
    'Mel Brooks': {'Spaceballs': '7.1', 'History of the World: Part I': '6.9'}, 
    'Ang Lee': {'Life of Pi': '8', 'The Ice Storm': '7.5'}, 
    'J.J. Abrams': {'Star Trek': '8', 'Star Trek Into Darkness': '7.8'}, 
    'Clint Eastwood': {'J. Edgar': '6.6', 'The Bridges of Madison County': '7.5'}}
    
UserMovieRatings = {
    'Amy': {'Family Plot':10, 'Rebecca':5, 'Spellbound':9, 'Star Trek':6}, 
    'Bill': {'Apocalypto':8, 'Braveheart':3, 'Rebecca':10, 'Spellbound':5, 'Star Trek':7}, 
    'Cathy': {'Spaceballs':7, 'The Ice Storm':4, 'Family Plot':5, 'Rebecca':9, 'Spellbound':1}, 
    'Dave': {'Braveheart':5, 'Rebecca':7, 'Spellbound':4}, 
    'Ernie': {'Apocalypto':3, 'Braveheart':8, 'Rebecca':1, 'Star Trek':7}, 
    'Fiona': {'The Ice Storm':3, 'Family Plot':10, 'Rebecca':6, 'Spellbound':10}}

