import math
record_in_seconds = float(input())
range_meters = float(input())
time_in_seconds_for_one_meter = float(input())
delay = math.floor(range_meters / 15)
delay = delay * 12.5
time_to_swim_the_rage = range_meters * time_in_seconds_for_one_meter
total_time = time_to_swim_the_rage + delay
if record_in_seconds <= total_time:
    diff = total_time - record_in_seconds
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")