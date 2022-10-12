junior_cyclists = int(input())
seniors_cyclists = int(input())
type_race = input()
total_cyclists = junior_cyclists + seniors_cyclists
juniors_price = 0
seniors_price = 0
expenses = 0
if type_race == "trail":
    juniors_price = 5.50
    seniors_price = 7
elif type_race == "cross-country":
    juniors_price = 8
    seniors_price = 9.50
elif type_race == "downhill":
    juniors_price = 12.25
    seniors_price = 13.75
else:
    juniors_price = 20
    seniors_price = 21.50

total_sum = (juniors_price * junior_cyclists) + (seniors_price * seniors_cyclists)
expenses = total_sum * 0.95
if type_race == "cross-country":
    if total_cyclists >= 50:
        expenses = expenses * 0.75

print(f"{expenses:.2f}")


