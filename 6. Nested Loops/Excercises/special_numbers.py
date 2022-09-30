number = int(input())
for num1 in range(1, 10):
    for num2 in range(1,10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if number % num1 == 0 and number % num2 == 0 and number % num3 == 0 and number % num4 == 0:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")