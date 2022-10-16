# -*- coding: utf-8 -*-
"""

@author: hina
"""

# Let's assume:
#  - Amy Hernandez is 10 years old.
#  - kids are 6 years old when they graduate 1st grade, 
#    and 18 years old when they graduate high school.

# Step 1:
# store the first name, last name and age of Amy in 3 variables.
# remember to use meaningful variable names
firstName = 'Amy'
lastName = 'Hernandex'
age = 10

# Step 2:
# store the age at 1st grade and age at 12th grade in 2 variables.
# remember to use meaningful variable names
age1stGradeGraduation = 6
ageHighSchoolGraduation = 18

# Step 3:
# Caculate current grade based on above variables and store in a variable
# remember to use meaningful variable names
currentGrade = age - age1stGradeGraduation + 1

# Step 4:
# Caculate number of years to graduation based on above variables 
#  and store in a variable
# remember to use meaningful variable names
yearsToGraduation = ageHighSchoolGraduation - age

# Step 5:
# Print first name, last name, age, current grade, and # years to graduation
# remember to use meaningful messages when printing out the data
print('First Name: ', firstName)
print('Last Name: ', lastName)
print('Age: ', age)
print ('Current Grade: ', currentGrade)
print ('Number of Years to Graduation: ', yearsToGraduation)

# Step 6:
# Try running your program for ages 5, 7, 17, 18, 19
# Do you see expected results?
# Note: for ages >=18, we'll learn how to write "if-statements" in later
#       modules to control what gets stored/printed

