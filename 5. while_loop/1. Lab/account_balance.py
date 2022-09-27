text = input()
is_valid = True
total = 0
while text != "NoMoreMoney":
    current = float(text)
    if current < 0:
        is_valid = False
        break
    print(f"Increase: {current:.2f}")
    total += current
    text = input()
if not is_valid:
    print("Invalid operation!")
    print(f"Total: {total:.2f}")
else:
    print(f"Total: {total:.2f}")
