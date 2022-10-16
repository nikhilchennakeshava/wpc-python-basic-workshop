# -*- coding: utf-8 -*-
"""

@author: hina
"""

# Step 1:
# Store the following first names in a list
# Amy, Bob, Cathy, Doug, Emily
# Remember to use a meaningful variable name
# You code here
firstNames = ['Amy', 'Bob', 'Cathy', 'Doug', 'Emily']

# Step 2:
# Store their last names in a list
# Douglas, Curry, Butler, Elder, Atkins
# Remember to use a meaningful variable name
# You code here
lastNames = ['Douglas', 'Curry', 'Butler', 'Elder', 'Atkins']

# Step 3:
# Store their ages in a list
# 10, 30, 25, 50, 40
# Remember to use a meaningful variable name
# You code here
ages = [10, 30, 25, 50, 40]

# Step 4:
# As it turns out, Bob has decided to update his last name to McCurry
# Update the lastNames list to reflect this change (by indexing into the list),
# Then print the lastNames list to ensure the it was updated
# You code here
lastNames[1]='McCurry'
print (lastNames)

# Step 5:
# Use the above lists to print out the first name, 
# followed by the first letter of the last name, 
# followed by age of the 5 people as follows:
#  Person 1: Amy D is 10 years old
#  Person 2: Bob M is 30 years old
#  Person 3: Cathy B is 25 years old
#  Person 4: Doug E is 50 years old
#  Person 5: Emily A is 40 years old
# You code here
print("Person 1:", firstNames[0], lastNames[0][0], "is", ages[0], "years old")
print("Person 2:", firstNames[1], lastNames[1][0], "is", ages[1], "years old")
print("Person 3:", firstNames[2], lastNames[2][0], "is", ages[2], "years old")
print("Person 4:", firstNames[3], lastNames[3][0], "is", ages[3], "years old")
print("Person 5:", firstNames[4], lastNames[4][0], "is", ages[4], "years old")


