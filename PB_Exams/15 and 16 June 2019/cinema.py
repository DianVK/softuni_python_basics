capacity = int(input())
command = input()
profit = 0
full_cinema = False
while command != "Movie time!":
    people = int(command)
    capacity -= people
    if capacity < 0:
        print("The cinema is full.")
        full_cinema = True
        break

    if people % 3 == 0:
        profit += (people * 5 - 5)
    else:
        profit += people * 5

    command = input()

if not full_cinema:
    print(f"There are {capacity} seats left in the cinema.")


print(f"Cinema income - {profit} lv.")