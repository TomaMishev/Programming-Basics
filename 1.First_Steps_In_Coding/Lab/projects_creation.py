# Write a program that calculates how many hours it will take an architect to prepare the projects on several construction sites. 
# The preparation of a project takes three hours.

# INPUT
# From the console read 2 lines:
# Architect's name - text
# Number of projects to draw up - integer in the interval [0 ... 100]

# OUTPUT
# The console prints:
# "The architect {architect name} will need {required hours} hours to complete {number of projects} project/s."


name = input()
number_of_projects = int(input())
time_for_projects = number_of_projects * 3
output = f"The architect {name} will need {time_for_projects} " \
         f"hours to complete {number_of_projects} project/s."
print(output)
