season = input()
km_per_month = float(input())
salary = 0
if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = km_per_month * 0.75
    elif season == "Summer":
        salary = km_per_month * 0.90
    elif season == "Winter":
        salary = km_per_month * 1.05
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = km_per_month * 0.95
    elif season == "Summer":
        salary = km_per_month * 1.10
    elif season == "Winter":
        salary = km_per_month * 1.25

elif 10000 < km_per_month <= 20000:
    salary = km_per_month * 1.45

salary_after_tax = (salary * 0.90) * 4
print(f"{salary_after_tax:.2f}")

