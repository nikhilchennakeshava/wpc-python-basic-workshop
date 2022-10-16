# -*- coding: utf-8 -*-
"""

@author: hina
"""

# Assume we have 5 students in our class:
# 1: Amy Douglas, 24 years old
# 2: Bob McCurry, 23 years old
# 3: Cathy Butler, 20 years old
# 4: Doug Elder, 25 years old
# 5: Emily Atkins, 21 years old

# Step 1:
# Create a nested dictionary called students as follows
#  - set the keys of the dictionary to 1, 2, 3, 4, 5
#  - set the values of the dictionary to another dictionary with 3 keys:
#    first name, last name, age
#  - store the information of the 5 stdents in our class in this nested dictionary
# You code here
students = {1: {'first':'Amy', 'last':'Douglas', 'age':24},
            2: {'first':'Bob', 'last':'Curry', 'age':23},
            3: {'first':'Cathy', 'last':'Butler', 'age':20},
            4: {'first':'Doug', 'last':'Elder', 'age':25},
            5: {'first':'Emily', 'last':'Atkins', 'age':21}}

# Step 2:
# As it turns out, Bob has decided to update his last name to McCurry
# Update Bob's last name to reflect this change (by indexing into the nested dictionary),
# Then print the nested dictionary to ensure the it was updated
# You code here
students[2]['last']='McCurry'
print(students)

# Step 3:
# Use a for loop to print out the first name, 
# followed by the first letter of the last name, 
# followed by age of the 5 students as follows:
#  Student 1 - Amy D is 10 years old
#  Student 2 - Bob M is 30 years old
#  Student 3 - Cathy B is 25 years old
#  Student 4 - Doug E is 50 years old
#  Student 5 - Emily A is 40 years old
# You code here
for idx, bio in students.items():
    print("Student", idx, "-", bio['first'], bio['last'][0], "is", bio['age'], "years old")

# Step 4:
# Update the for loop above to also calcualte the average age
# and print the average age
avgAge = 0
for idx, bio in students.items():
    print("Student", idx, "-", bio['first'], bio['last'][0], "is", bio['age'], "years old")
    avgAge += bio['age']
print("average class age:", avgAge/len(students))
