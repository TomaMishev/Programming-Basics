destination = input()

while destination != "End":
    needed_money = float(input())
    total_sum = 0
    while total_sum < needed_money:
        current_money = float(input())
        total_sum += current_money
    print(f"Going to {destination}!")

    destination = input()
