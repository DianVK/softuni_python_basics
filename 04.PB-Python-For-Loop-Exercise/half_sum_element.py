import sys

n = int(input())

max_num = -sys.maxsize
sum = 0
for i in range(1, n + 1):
    current_num = int(input())

    sum = sum + current_num

    if current_num > max_num:
        max_num = current_num

other_nums_sum = sum - max_num

if other_nums_sum == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    diff = abs(other_nums_sum - max_num)
    print(f"Diff = {diff}")