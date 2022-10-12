budget = float(input())
count_videocards = int(input())
count_processors = int(input())
count_ram_memorys= int(input())
one_videocard_price = 250
one_procesor_price = 0.35 * (count_videocards * one_videocard_price)
one_ram_memorys_price = 0.10 * (count_videocards * one_videocard_price)
total_sum = (count_videocards * one_videocard_price) + (count_processors * one_procesor_price) + (count_ram_memorys * one_ram_memorys_price)
if count_videocards > count_processors:
    total_sum = total_sum * 0.85
else:
    total_sum = total_sum
if total_sum <= budget:
    total_sum = budget - total_sum
    print(f"You have {total_sum:.2f} leva left!")
else:
    total_sum = total_sum - budget
    print(f"Not enough money! You need {total_sum:.2f} leva more!")