text = input()

output = "unknown"
if text == "banana" or text == "apple" or text == "kiwi" or text == "cherry" or text == "lemon" or text == "grapes":
    output = "fruit"
elif text == "tomato" or text == "cucumber" or text == "pepper" or text == "carrot":
    output = "vegetable"
print(output)