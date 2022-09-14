kg_price_vegetables = float(input())
kg_price_fruits = float(input())
kg_vegetables = float(input())
kg_fruits = float(input())

vegetables_total = kg_price_vegetables * kg_vegetables
fruit_total = kg_price_fruits * kg_fruits
total = vegetables_total + fruit_total

print(f"{total / 1.94:.2f}")