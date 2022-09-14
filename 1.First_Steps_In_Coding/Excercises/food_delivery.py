chicken_menus_count = int(input())
fish_menus_count = int(input())
vegan_menus = int(input())

chicken_price = chicken_menus_count * 10.35
fish_price = fish_menus_count * 12.40
vegan_price = vegan_menus * 8.15

total_price = chicken_price + fish_price + vegan_price
desert_price = total_price * 0.20
end_sum = total_price + desert_price + 2.50

print(end_sum)