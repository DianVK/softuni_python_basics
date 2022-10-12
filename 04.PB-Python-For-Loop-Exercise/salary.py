open_tabs = int(input())
salary = int(input())
cut_salary = salary
for i in range(1, open_tabs + 1):
    name_tab = input()
    if name_tab == "Facebook":
        cut_salary -= 150
    elif name_tab == "Instagram":
        cut_salary -= 100
    elif name_tab == "Reddit":
        cut_salary -= 50
    if cut_salary <= 0:
        break
if cut_salary <= 0:
    print("You have lost your salary.")

else:
    print(f"{cut_salary}")

