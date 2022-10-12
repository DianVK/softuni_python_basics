total_students = int(input())
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0
sum_5 = 0
for i in range(1, total_students + 1):
    current_grade = float(input())
    if current_grade < 3.00:
        count_2 += 1
        sum_2 += current_grade
    elif current_grade < 4.00:
        count_3 += 1
        sum_3 += current_grade
    elif current_grade < 5.00:
        count_4 += 1
        sum_4 += current_grade
    else:
        count_5 += 1
        sum_5 += current_grade
total_count = count_2 + count_4 + count_3 + count_5
total_sum = sum_2 + sum_3 + sum_4 + sum_5
average = (total_sum / total_count)

calculation_2 = (count_2/total_students)*100
calculation_3 = (count_3/total_students)*100
calculation_4 = (count_4/total_students)*100
calculation_5 = (count_5/total_students)*100

print(f"Top students: {calculation_5:.2f}%")
print(f"Between 4.00 and 4.99: {calculation_4:.2f}%")
print(f"Between 3.00 and 3.99: {calculation_3:.2f}%")
print(f"Fail: {calculation_2:.2f}%")
print(f"Average: {average:.2f}")
