season = input()
type_group = input()
count_students = int(input())
count_nightstands = int(input())
price = 0
sport_practice = ""
if type_group == "boys" or type_group == "girls":
    if season == "Winter":
        price = count_students * 9.60 * count_nightstands
    elif season == "Spring":
        price = count_students * 7.20 * count_nightstands
    elif season == "Summer":
        price = count_students * 15 * count_nightstands

elif type_group == "mixed":
    if season == "Winter":
        price = count_students * 10 * count_nightstands
    elif season == "Spring":
        price = count_students * 9.50 * count_nightstands
    elif season == "Summer":
        price = count_students * 20 * count_nightstands

if 20 > count_students >= 10:
    price = price * 0.95
elif 50 > count_students >= 20:
    price = price * 0.85
elif count_students >= 50:
    price = price * 0.50
if season == "Winter" and type_group == "girls":
    sport_practice = "Gymnastics"
elif season == "Winter" and type_group == "boys":
    sport_practice = "Judo"
elif season == "Winter" and type_group == "mixed":
    sport_practice = "Ski"
elif season == "Summer" and type_group == "girls":
    sport_practice = "Volleyball"
elif season == "Summer" and type_group == "boys":
    sport_practice = "Football"
elif season == "Summer" and type_group == "mixed":
    sport_practice = "Swimming"
elif season == "Spring" and type_group == "girls":
    sport_practice = "Athletics"
elif season == "Spring" and type_group == "boys":
    sport_practice = "Tennis"
elif season == "Spring" and type_group == "mixed":
    sport_practice = "Cycling"

print(f"{sport_practice} {price:.2f} lv.")
