price_trip = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())
total_sum = (count_puzzles * 2.60) + (count_dolls * 3) + (count_bears * 4.10) + (count_minions * 8.20) + (count_trucks * 2)
total_count = count_puzzles + count_dolls + count_bears + count_minions + count_trucks

if total_count >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum = total_sum - (total_sum * 0.10)
diff = abs(price_trip - total_sum)
if price_trip <= total_sum:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")

