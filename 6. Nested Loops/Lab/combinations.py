num_to_check = int(input())
combinations_count = 0
for num1 in range(0, num_to_check + 1):
    for num2 in range(0, num_to_check + 1):
        for num3 in range(0, num_to_check + 1):
            result = num1 + num2 + num3
            if result == num_to_check:
                combinations_count += 1

print(combinations_count)
