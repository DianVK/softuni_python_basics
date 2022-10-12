number = input()
max_number = -10000000000000

while number != "Stop":
    num = int(number)

    if num > max_number:
        max_number = num
    number = input()

print(max_number)
