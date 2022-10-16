# -*- coding: utf-8 -*-
"""
@author: hina
"""

print ()

from operator import itemgetter

# manhattan distance between 2 dictionary ratings
def manhattanD(ratings1D, ratings2D):
    
    # calcualte manhattan distance
    distance = 0       
    for k in ratings1D.keys() & ratings2D.keys():
        distance = distance + abs(ratings1D[k] - ratings2D[k])
    
    # return value of manhattan distance
    return distance

#user ratings
UserMovieRatings = {
    'Amy': {'Family Plot':10, 'Rebecca':5, 'Spellbound':9, 'Star Trek':6}, 
    'Bill': {'Apocalypto':8, 'Braveheart':3, 'Rebecca':10, 'Spellbound':5, 'Star Trek':7}, 
    'Cathy': {'Spaceballs':7, 'The Ice Storm':4, 'Family Plot':5, 'Rebecca':9, 'Spellbound':1}, 
    'Dave': {'Braveheart':5, 'Rebecca':7, 'Spellbound':4}, 
    'Ernie': {'Apocalypto':3, 'Braveheart':8, 'Rebecca':1, 'Star Trek':7}, 
    'Fiona': {'The Ice Storm':3, 'Family Plot':10, 'Rebecca':6, 'Spellbound':10}}

# for whom are we making recommendations?
userX = "Amy"
userXRatings = UserMovieRatings[userX]

# find the manhattan distance between userX's ratings, and each of the other user's ratings.
# use a for loop to get at the other users and their ratings - DO NOT hard code.
# use the manhattan function to caclulate the manhattan distance between user ratings.
# assign list of (user, distance) tuples to variable userDistances.
# Example: [('Bill', 4.39), ('Cathy', 3.16), ('Dave', 1.41), ('Ernie', 3.64)]
userDistances = []
for userY, userYRatings in UserMovieRatings.items():
    if (userX != userY):
        # find the euclidean distance between userX and userY 
        # and append (userY, distance) to userPCs list
        manxy = manhattanD (userXRatings, userYRatings)
        tup = (userY, manxy)
        userDistances.append(tup)
#print (userDistances)

# sort list of tuples by lowest distance to highest distance.
# assign sorted list to variable userSortedDistances.
# Example: [('Dave', 1.41), ('Cathy', 3.16), ('Ernie', 3.64), ('Bill', 4.39)]
userSortedDistances = sorted(userDistances, key=itemgetter(1), reverse=False)
#print(userSortedDistances)

# userX's NN is the user at the 0th position of the sorted list.
# assign NN to userXNN.
# Example: 'Dave'
userXNN = userSortedDistances[0][0]
#print(userXNN)

# recos for userX will include movies rated by userXNN, not already rated by userX.
# assign list of (movie, rating) tuples to variable userXRecos.
# Example: [('Family Plot',10), ('The Ice Storm',3), ('Rebecca',6)]
userXRecos = []
for album in (UserMovieRatings[userXNN].keys() - UserMovieRatings[userX].keys()):
    tup = (album, UserMovieRatings[userXNN][album])
    userXRecos.append(tup)
#print (userXRecos)

# sort list of tuples by highest rating to lowest rating.
# assign sorted list to varaible userXSortedRecos.
# Example: [('Family Plot',10), ('Rebecca',6), ('The Ice Storm',3)]
userXSortedRecos = sorted(userXRecos, key=itemgetter(1), reverse=True)

print ("Recommendations for:", userX)
print ("Based on closest user:", userXNN)
print (userXSortedRecos)