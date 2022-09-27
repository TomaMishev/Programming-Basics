import sys

command = input()

min_number = sys.maxsize
while command != "Stop":
    current = int(command)
    if min_number > current:
        min_number = current
    command = input()
print(min_number)
