name_of_actor = input()
starting_points = float(input())
count_jury = int(input())
total_points = 0
result = starting_points

for jury in range(1, count_jury + 1):
    name_of_jury = input()
    points_from_jury = float(input())
    total_points = (len(name_of_jury) * points_from_jury) / 2
    result += total_points
    if result > 1250.5:
        break

if result > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {result:.1f}!")

else:
    diff = 1250.5 - result
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")