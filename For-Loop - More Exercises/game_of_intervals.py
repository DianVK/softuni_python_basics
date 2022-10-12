total_count = int(input())
bonus = 0
result = 0
count_50 = 0
count_40 = 0
count_30 = 0
count_20 = 0
count_10 = 0
count_invalid = 0
for i in range(1, total_count +1):
    number = int(input())
    if 0 <= number < 10:
        bonus = 0.2 * number
        result += bonus
        count_50 += 1
    elif 0 < number <= 19:
        bonus = 0.3 * number
        result += bonus
        count_40 += 1
    elif 0 < number <= 29:
        bonus = 0.4 * number
        result += bonus
        count_30 += 1
    elif 0 < number <= 39:
        bonus = 50
        result += bonus
        count_20 += 1
    elif 0 < number <= 50:
        bonus = 100
        result += bonus
        count_10 += 1
    else:
        result = result / 2
        count_invalid += 1

print(f"{result:.2f}")
print(f"From 0 to 9: {(count_50 / total_count * 100):.2f}%")
print(f"From 10 to 19: {(count_40 / total_count * 100):.2f}%")
print(f"From 20 to 29: {(count_30 / total_count * 100):.2f}%")
print(f"From 30 to 39: {(count_20 / total_count * 100):.2f}%")
print(f"From 40 to 50: {(count_10 / total_count * 100):.2f}%")
print(f"Invalid numbers: {(count_invalid / total_count * 100):.2f}%")