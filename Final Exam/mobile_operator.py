contract_term = input()
contract_type = input()
mobile_net = input()
months_count = int(input())

tax = 0
if contract_term == "one":
    if contract_type == "Small":
        tax = 9.98
    elif contract_type == "Middle":
        tax = 18.99
    elif contract_type == "Large":
        tax = 25.98
    elif contract_type == "ExtraLarge":
        tax = 35.99
elif contract_term == "two":
    if contract_type == "Small":
        tax = 8.58
    elif contract_type == "Middle":
        tax = 17.09
    elif contract_type == "Large":
        tax = 23.59
    elif contract_type == "ExtraLarge":
        tax = 31.79

mobile_net_price = 0
if mobile_net == "yes":
    if tax < 10:
        mobile_net_price = 5.50
    elif tax <= 30:
        mobile_net_price = 4.35
    else:
        mobile_net_price = 3.85
total = tax + mobile_net_price

if contract_term == "two":
    total = total - (total * (3.75 / 100))

end_sum = total * months_count

print(f"{end_sum:.2f} lv.")
