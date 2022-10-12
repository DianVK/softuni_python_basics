import math
count_tournaments = int(input())
starting_points = int(input())
total_points = starting_points
win_counts = 0
for i in range(1, count_tournaments + 1):
    level = input()
    if level == "W":
        win_counts += 1
        total_points += 2000
    elif level == "F":
        total_points += 1200
    elif level == "SF":
        total_points += 720
print(f"Final points: {total_points}")
points_without_starting_points = total_points - starting_points
average_points = math.floor(points_without_starting_points / count_tournaments)
print(f"Average points: {average_points}")
percent_win = win_counts / count_tournaments * 100
print(f"{percent_win:.2f}%")
