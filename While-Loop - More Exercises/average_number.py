number = int(input())
sum = 0
for i in range(1, number +1):
    numbers = int(input())
    sum += numbers
    average = sum / number
print(f"{average:.2f}")