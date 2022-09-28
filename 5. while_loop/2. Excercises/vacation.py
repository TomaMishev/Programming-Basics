money_needed = float(input())
current_money = float(input())

days_passed = 0
copy_of_current_money = current_money
spending_days = 0
if_failed_to_save = False
while True:
    command = input()
    money = float(input())
    days_passed += 1
    if command == "spend":
        copy_of_current_money -= money
        if copy_of_current_money < 0:
            copy_of_current_money = 0
        spending_days += 1
        if spending_days == 5:
            if_failed_to_save = True
            break
    elif command == "save":
        spending_days = 0
        copy_of_current_money += money

    if copy_of_current_money >= money_needed:
        if_failed_to_save = False
        break
if if_failed_to_save:
    print("You can't save the money.")
    print(f"{days_passed}")
else:
    print(f"You saved the money for {days_passed} days.")
