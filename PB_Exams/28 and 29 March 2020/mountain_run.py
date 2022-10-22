from math import floor
record_in_seconds = float(input())
lenght_in_meters = float(input())
time_in_seconds_per_meter = float(input())

delay = floor(lenght_in_meters / 50)
delay = delay * 30

time_went = lenght_in_meters * time_in_seconds_per_meter

total_time = time_went + delay
diff = total_time - record_in_seconds

if total_time >= record_in_seconds:
    print(f"No! He was {diff:.2f} seconds slower.")
elif record_in_seconds > total_time:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
