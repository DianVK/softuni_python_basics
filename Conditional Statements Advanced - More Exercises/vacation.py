budget = float(input())
season = input()
location = ""
city = ""
cost = 0
if budget <= 1000:
    location = "Camp"
    if season == "Summer":
        city = "Alaska"
        cost = budget * 0.65
    elif season == "Winter":
        city = "Morocco"
        cost = budget * 0.45


elif 1000 < budget <= 3000:
    location = "Hut"
    if season == "Summer":
        city = "Alaska"
        cost = budget * 0.80
    elif season == "Winter":
        city = "Morocco"
        cost = budget * 0.60

elif budget > 3000:
    location = "Hotel"
    if season == "Summer":
        city = "Alaska"
        cost = budget * 0.90
    elif season == "Winter":
        city = "Morocco"
        cost = budget * 0.90

print(f"{city} - {location} - {cost:.2f}")