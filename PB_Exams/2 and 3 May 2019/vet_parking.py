count_days = int(input())
count_hours_per_day = int(input())
# За всеки четен ден и нечетен час, паркингът таксува 2.50 лева.\
tax = 0
total_sum_all_days = 0
total_sum_all_days_2 = 0
counter_days = 0
counter_hours = 0
for i in range(1, count_days + 1):
    counter_days += 1
    total_sum = 0
    for j in range(1, count_hours_per_day + 1):
        counter_hours = 1
        if i % 2 == 0 and j % 2 != 0:
            tax = 2.50
        elif i % 2 != 0 and j % 2 == 0:
            tax = 1.25
        else:
            tax = 1
        total_sum = 1 * tax
        total_sum_all_days += total_sum

    print(f"Day: {i} - {total_sum_all_days:.2f} leva")
    total_sum_all_days_2 += total_sum_all_days
    total_sum_all_days = 0


print(f"Total: {total_sum_all_days_2:.2f} leva")
