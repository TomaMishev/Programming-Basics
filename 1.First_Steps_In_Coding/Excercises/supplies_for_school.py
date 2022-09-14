pen_count = int(input())
marker_count = int(input())
cleaner_liters = int(input())
discount_percent = int(input())

pen_price = pen_count * 5.80
marker_price = marker_count * 7.20
cleaner_price = cleaner_liters * 1.20
total_price = pen_price + marker_price + cleaner_price
price_after_discount = total_price - (total_price * (discount_percent / 100))

print (price_after_discount)