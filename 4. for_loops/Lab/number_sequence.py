import sys

n = int(input())

current_min = sys.maxsize
current_max = - sys.maxsize
for number in range(n):
    sequence_num = int(input())
    if current_min > sequence_num:
        current_min = sequence_num
    if current_max < sequence_num:
        current_max = sequence_num
print(f"Max number: {current_max}")
print(f"Min number: {current_min}")