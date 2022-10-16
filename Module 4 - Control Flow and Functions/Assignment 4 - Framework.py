# -*- coding: utf-8 -*-
"""
@author: hina
"""

import math

# Pearson Correlation between two vectors
def pearsonD(userratings1, userratings2):
    
    # Step 1:
    # Initialize variables to store partial sums sumpq, sump, sumq, sump2, sumq2
    # Your code here

    
    # Step 2: 
    # calcualte n 
    #  - your solution should work for *any* userratings1 and useratings2;
    #    so do not hardcode based on the specpfic ratings we are considering...
    # Your code here

    
    # Step 3: 
    # error check: check if n==0, and return -2 if that is so
    # Your code here

    
    # Step 4: 
    # calcualte pearson correlation
    #  - use the computationally efficient form
    #  - use a single for loop        
    #  - use variables initialized above to calcualte and store partial sums
    # Your code here
   
    
    # Step 5: 
    # calcualte numerator (nr) and denominator (dr) for pearson correlation
    # Your code here

    
    # Step 6:
    # error check: check is dr==0, and return -2 if that is so
    # Your code here


    # Step 7:
    # return value of pearson correlation coefficient as nr/dr
    # Your code here

        
UserPRatings = {'Apple':1, 'Samsung':5, 'Nokia':7, 'Motorola':8, 'LG':5, 'Sony':1, 'Blackberry':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}

# Step 8: 
# call pearsonD for UserPRatings and UserQRatings and 
# store the returned value in variable pc
# Your code here


# Step 9: 
# print the returned pearson correlation pc
# Your code here


