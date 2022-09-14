nylon_needed = int(input())
paint_needed = int(input())
razr_needed = int(input())
hours_needed = int(input())

nylon_price = (nylon_needed + 2) * 1.50
paint_price = (paint_needed + (paint_needed * 0.10)) * 14.50
razr_price = razr_needed * 5.00

total_sum = nylon_price + paint_price + razr_price + 0.40
workers_sum = (total_sum * 30 / 100) * hours_needed
end_sum = total_sum + workers_sum

print(end_sum)

