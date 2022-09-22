number1 = int(input())
number2 = int(input())
operator = input()

output = ""
result = 0
odd_or_even = ""
if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = number1 + number2
        if result % 2 == 0:
            odd_or_even = "even"
        else:
            odd_or_even = "odd"
    elif operator == "-":
        result = number1 - number2
        if result % 2 == 0:
            odd_or_even = "even"
        else:
            odd_or_even = "odd"
    elif operator == "*":
        result = number1 * number2
        if result % 2 == 0:
            odd_or_even = "even"
        else:
            odd_or_even = "odd"
elif operator == "/":
    if number2 == 0:
        output = f"Cannot divide {number1} by zero"
    else:
        result = number1 / number2
elif operator == "%":
    if number2 == 0:
        output = f"Cannot divide {number1} by zero"
    else:
        result = int(number1 % number2)

if len(odd_or_even) > 0:
    print(f"{number1} {operator} {number2} = {result} - {odd_or_even}")
if output == "" and (operator == "/" or operator == "%"):
    if operator == "%":
        print(f"{number1} {operator} {number2} = {result}")
    else:
        print(f"{number1} {operator} {number2} = {result:.2f}")
else:
    print(f"{output}")
