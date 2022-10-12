age_of_lily = int(input())
price_washing_machine = float(input())
price_of_one_toy = int(input())
brothers_count = 0
count_toys = 0
total_sum = 0
money = 10
for i in range(1, age_of_lily + 1):
    if i % 2 != 0:
        count_toys += 1
    else:
        brothers_count += 1
        total_sum = total_sum + money
        money = money + 10
result = total_sum + (count_toys * price_of_one_toy ) - brothers_count
diff = abs(result - price_washing_machine)
if result >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
