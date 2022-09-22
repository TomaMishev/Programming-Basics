# Write a program that reads from the console: name, surname, age and city and then prints the following message:
# "You are <firstName> <lastName>, a <age>-years old person from <town>."


first_name = input()
second_name = input()
age = int(input())
town = input()
output = f"You are {first_name} {second_name}, a {age}-years old person from {town}."
print(output)
