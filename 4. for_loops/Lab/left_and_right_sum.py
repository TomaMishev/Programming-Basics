n = int(input())

left_sum = 0
right_sum = 0

for number in range(n * 2):
    num_to_add = int(input())
    if number < n:
        left_sum += num_to_add
    else:
        right_sum += num_to_add

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
