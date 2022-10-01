kozunak_count = int(input())
egg_box_count = int(input())
cookies_kg = int(input())

kozunak_price = kozunak_count * 3.20
egg_box_price = egg_box_count * 4.35
cookies_price = cookies_kg * 5.40
price_for_egg_paint = egg_box_count * 12 * 0.15
total = kozunak_price + egg_box_price + cookies_price + price_for_egg_paint
print(f"{total:.2f}")
