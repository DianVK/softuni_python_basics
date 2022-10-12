import math
enter_hour = int(input())
enter_minutes = int(input())
hour_to_minutes = enter_hour * 60
time_plus_15_minutes = (enter_hour * 60) + enter_minutes + 15
hours_calc = math.floor(time_plus_15_minutes / 60)
minutes_calc = time_plus_15_minutes % 60
if hours_calc > 23:
    hours_calc = hours_calc * 0
if minutes_calc < 10:
    print(f"{hours_calc}:0{minutes_calc}")
else:
    print(f"{hours_calc}:{minutes_calc}")