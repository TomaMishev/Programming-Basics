import math

record = float(input())
distance = float(input())
time_in_seconds = float(input())

distance_needed = distance * time_in_seconds
added_time = math.floor(distance / 15) * 12.5
total_time = distance_needed + added_time

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = total_time - record
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
