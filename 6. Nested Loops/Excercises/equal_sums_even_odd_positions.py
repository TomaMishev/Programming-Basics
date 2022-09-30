start = int(input())
finish = int(input())

for current_num in range(start, finish + 1):
    num_to_check = str(current_num)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(num_to_check):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(num_to_check, end=" ")
