day_from_week = input()
if day_from_week == "Monday" or day_from_week == "Tuesday" or day_from_week == "Wednesday" or day_from_week == "Thursday" or day_from_week == "Friday":
    print("Working day")
elif day_from_week == "Sunday" or day_from_week == "Saturday":
    print("Weekend")
else:
    print("Error")