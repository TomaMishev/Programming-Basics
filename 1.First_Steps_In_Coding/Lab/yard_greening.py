square_meters = float(input())
total_price = square_meters * 7.61
discount = total_price * 0.18
end_price = total_price - discount
print(f"The final price is: {end_price} lv.")
print(f"The discount is: {discount} lv.")