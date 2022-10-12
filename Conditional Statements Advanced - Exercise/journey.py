budget = float(input())
season = input()
type_destination = str
destination = str
if 1 <= budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_destination = "Camp"
        budget = budget * 0.30
    if season == "winter":
        type_destination = "Hotel"
        budget = budget * 0.70
if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_destination = "Camp"
        budget = budget * 0.40
    if season == "winter":
        type_destination = "Hotel"
        budget = budget * 0.80
if budget > 1000:
    destination = "Europe"
    type_destination = "Hotel"
    budget = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{type_destination} - {budget:.2f}")



