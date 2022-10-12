type_projects = input()
rows = int(input())
columns = int(input())
income = 0
capacity = rows * columns
if type_projects == "Premiere":
    income = capacity * 12.00
elif type_projects == "Normal":
    income = capacity * 7.50
elif type_projects == "Discount":
    income = capacity * 5.00
else:
    print("Wrong Input")
print(f"{income:.2f} leva")