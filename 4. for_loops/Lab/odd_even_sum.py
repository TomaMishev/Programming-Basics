n = int(input())

even_sum = 0
odd_sum = 0
for number in range(n):
    check_num = int(input())
    if number % 2 == 0:
        even_sum += check_num
    else:
        odd_sum += check_num

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {abs(even_sum - odd_sum)}")