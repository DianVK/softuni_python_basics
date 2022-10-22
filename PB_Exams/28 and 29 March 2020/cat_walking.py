

minutes_per_day = int(input())
count_per_day = int(input())
calories_per_day = int(input())
divide_calories = calories_per_day / 2

calculation = minutes_per_day * count_per_day
calculation2 = 5 * calculation

if divide_calories <= calculation2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calculation2}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calculation2}.")
