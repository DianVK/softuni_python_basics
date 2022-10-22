rent_of_hall = int(input())
statues = rent_of_hall * 0.70
ketering = statues * 0.85
sound = ketering / 2
total_expenses = rent_of_hall + statues + ketering + sound
print(f"{total_expenses:.2f}")
