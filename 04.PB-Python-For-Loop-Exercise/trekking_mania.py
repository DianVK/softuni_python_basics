groups_count = int(input())
mountain_name = ""
total_sum = 0
musala_sum = 0
monblan_sum = 0
kilimandzharo_sum = 0
k2_sum = 0
everest_sum = 0
for i in range(1, groups_count + 1):
    count_climbers = int(input())
    total_sum = total_sum + count_climbers
    if count_climbers <= 5:
        musala_sum += count_climbers
    elif count_climbers <= 12:
        monblan_sum += count_climbers
    elif count_climbers <= 25:
        kilimandzharo_sum += count_climbers
    elif count_climbers <= 40:
        k2_sum += count_climbers
    elif count_climbers > 40:
        everest_sum += count_climbers
percent_musala = musala_sum / total_sum * 100
print(f"{percent_musala:.2f}%")
percent_monblan = monblan_sum / total_sum * 100
print(f"{percent_monblan:.2f}%")
percent_kilimandzharo = kilimandzharo_sum / total_sum * 100
print(f"{percent_kilimandzharo:.2f}%")
percent_k2 = k2_sum / total_sum * 100
print(f"{percent_k2:.2f}%")
percent_everest = everest_sum / total_sum * 100
print(f"{percent_everest:.2f}%")

