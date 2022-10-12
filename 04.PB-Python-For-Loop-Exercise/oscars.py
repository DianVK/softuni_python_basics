name_of_actor = input()
points_from_the_academy = float(input())
count_of_jury = int(input())
total_points = points_from_the_academy
for i in range(1, count_of_jury + 1):
    name_of_jury = input()
    points_from_jury = float(input())
    current_points = (points_from_jury * len(name_of_jury)) / 2
    total_points += current_points

    if total_points > 1250.5:
        break
if total_points < 1250.5:
    diff = 1250.5 - total_points
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
