sum = int(input())
sex = input()
age = int(input())
sport = input()
price = 0

if sex == "m":
    if sport == "Gym":
        price = 42
    elif sport == "Boxing":
        price = 41
    elif sport == "Yoga":
        price = 45
    elif sport == "Zumba":
        price = 34
    elif sport == "Dances":
        price = 51
    elif sport == "Pilates":
        price = 39

elif sex == "f":
    if sport == "Gym":
        price = 35
    elif sport == "Boxing":
        price = 37
    elif sport == "Yoga":
        price = 42
    elif sport == "Zumba":
        price = 31
    elif sport == "Dances":
        price = 53
    elif sport == "Pilates":
        price = 37

if age <= 19:
    price = price * 0.80


if sum > price:
    print(f"You purchased a 1 month pass for {sport}.")


elif price > sum:
    diff = abs(sum - price)
    print(f"You don't have enough money! You need ${diff:.2f} more.")