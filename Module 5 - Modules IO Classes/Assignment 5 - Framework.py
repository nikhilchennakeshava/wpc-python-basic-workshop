# -*- coding: utf-8 -*-
"""
@author: hina
"""

import math

# definie class similarity
class similarity:
    
    # Class instantiation 
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ

    # Minkowski Distance between two vectors
    def minkowksi(self, r):
    
        # Step 1.1: initialize minkowski distance
        # Your code here
   
        
        # Step 1.2: for cell phone brands rated by both users
        # Your code here
        
            
            # Step 1.3: add absolute distance between cell phone brands 
            #           to the minkowski distance
            # Your code here
            
    
        # Step: 1.4: return value of minkowski distance
        # Your code here
        

    # Pearson Correlation between two vectors
    def pearson(self):
        
        # Step 2.1:
        # Initialize partial sums sumpq, sump, sumq, sump2, sumq2
        # Your code here
        
        
        # Step 2.2: 
        # calcualte n 
        #  - your solution should work for *any* ratings1 and ratings2;
        #    do not hardcode based on the specpfic ratings we are considering
        # Your code here
        
        
        # Step 2.3: 
        # error check: check if n==0, and return -2 if that is so
        # Your code here
        

        # Step 2.4: 
        # calcualte pearson correlation
        #  - use the computationally efficient form
        #  - use a single for loop        
        #  - use variables initialized above to calcualte and store partial sums
        # Your code here 
          

        # Step 2.5: 
        # calcualte numerator (nr) and denominator (dr) for pearson correlation
        # Your code here
        
        
        # Step 2.6:
        # error check: check is dr==0, and return -2 if that is so
        # Your code here
        

        # Step 2.7:
        # return value of pearson correlation coefficient as nr/dr
        # Your code here   
        

# user ratings
UserPRatings = {'Motorola':8, 'LG':5, 'Sony':1, 'Apple':1, 'Samsung':5, 'Nokia':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}

# Step 3.1: instantiate object of class similarity
# Your code here


# Step 3.2: compute and print manhattan distance (minkowski with r=1)
# Your code here


# Step 3.3: compute and print euclidean distance (minkowski with r=2)
# Your code here


# Step 3.4: compute and print minkowski with r=3
# Your code here


# Step 3.5: compute and print perason similarity
# Your code here



