total_pages = int(input())
pages_for_read_for_hour = int(input())
day_count = int(input())

total_time_for_book = total_pages // pages_for_read_for_hour
hours_needed = total_time_for_book // day_count

print(hours_needed)