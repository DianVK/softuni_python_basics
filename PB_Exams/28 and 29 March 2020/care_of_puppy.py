
food_kg = int(input())
food_kg = food_kg * 1000
command = input()
while command != "Adopted":
    food_per_eat = int(command)
    food_kg -= food_per_eat


    command = input()

if command == "Adopted" and food_kg >= 0:
    print(f"Food is enough! Leftovers: {food_kg} grams.")
else:
    print(f"Food is not enough. You need {abs(food_kg)} grams more.")
