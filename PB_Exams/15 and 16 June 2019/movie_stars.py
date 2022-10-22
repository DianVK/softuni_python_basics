cash = 0
budget_for_actors = float(input())
command = input()
while command != "ACTION":
    name_of_actor = command

    if len(name_of_actor) <= 15:
        money = float(input())
        budget_for_actors -= money
    elif len(name_of_actor) > 15:
        cash = budget_for_actors * 0.20
        budget_for_actors -= cash
    if budget_for_actors <= 0:
        break
    command = input()

if budget_for_actors > 0:
    print(f"We are left with {abs(budget_for_actors):.2f} leva.")
else:
    diff = abs(budget_for_actors)
    print(f"We need {diff:.2f} leva for our actors.")