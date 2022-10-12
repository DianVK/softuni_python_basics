number_day = int(input())
if 1 <= number_day <= 7:
    if number_day == 1:
        print("Monday")
    if number_day == 2:
        print("Tuesday")
    if number_day == 3:
        print("Wednesday")
    if number_day == 4:
        print("Thursday")
    if number_day == 5:
        print("Friday")
    if number_day == 6:
        print("Saturday")
    if number_day == 7:
        print("Sunday")
else:
    print("Error")