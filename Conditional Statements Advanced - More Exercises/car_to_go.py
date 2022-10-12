budget = float(input())
season = input()
cabrio = 0
jeep = 0
class_car = ""
if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        cabrio = budget * 0.35
        print(class_car)
        print(f"Cabrio - {cabrio:.2f}")

    if season == "Winter":
        jeep = budget * 0.65
        print(class_car)
        print(f"Jeep - {jeep:.2f}")

if 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        cabrio = budget * 0.45
        print(class_car)
        print(f"Cabrio - {cabrio:.2f}")

    if season == "Winter":
        jeep = budget * 0.80
        print(class_car)
        print(f"Jeep - {jeep:.2f}")

if budget > 500:
    class_car = "Luxury class"
    jeep = budget * 0.90
    print(class_car)
    print(f"Jeep - {jeep:.2f}")

