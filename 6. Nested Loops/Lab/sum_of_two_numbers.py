start = int(input())
finish = int(input())
magic_num = int(input())
combinations_count = 0
combination_is_found = False

for num1 in range(start, finish + 1):
    for num2 in range(start, finish +1):
        combinations_count += 1
        result = num1 + num2
        if result == magic_num:
            combination_is_found = True
            break
    if combination_is_found:
        break
if combination_is_found:
    print(f"Combination N:{combinations_count} ({num1} + {num2} = {magic_num})")
else:
    print(f"{combinations_count} combinations - neither equals {magic_num}")
