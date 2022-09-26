import sys

n = int(input())

max_num = -sys.maxsize
total_sum = 0
for num in range (1, n + 1):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num

    total_sum += current_num

total_sum -= max_num
if total_sum == max_num:
    print("Yes")
    print(f"Sum = {total_sum}")
else:
    print("No")
    print(f"Diff = {abs(total_sum - max_num)}")
