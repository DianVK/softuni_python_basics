from math import ceil
count_people = int(input())
entrance_tax = float(input())
price_per_sunbed = float(input())
price_per_umbrella = float(input())
sum_entrance = count_people * entrance_tax
sum_sunbeds = ceil(count_people * 0.75) * price_per_sunbed
sum_umbrellas = ceil(count_people / 2) * price_per_umbrella
total_sum = sum_sunbeds + sum_umbrellas + sum_entrance
print(f"{total_sum:.2f} lv." )