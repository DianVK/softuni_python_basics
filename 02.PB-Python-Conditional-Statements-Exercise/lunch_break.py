import math
name_serial = input()
episode_time = int(input())
brake_time = int(input())
lunch_time = brake_time * 0.125
breath_time = brake_time * 0.25
sum_brakes = brake_time - lunch_time - breath_time
diff = abs(sum_brakes - episode_time)
rounded_diff = math.ceil(diff)
if sum_brakes >= episode_time:
    print(f"You have enough time to watch {name_serial} and left with {rounded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need {rounded_diff} more minutes.")
