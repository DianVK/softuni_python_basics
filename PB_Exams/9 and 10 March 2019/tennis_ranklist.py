from math import floor
count_tournaments = int(input())
starting_points = int(input())

wins_count = 0
f_counts = 0
sf_counts = 0
average_points = 0
for i in range(1, count_tournaments + 1):
    stage_tournament = input()
    if stage_tournament == "W":
        wins_count += 1
        starting_points += 2000
        average_points += 2000
    elif stage_tournament == "F":
        f_counts += 1
        starting_points += 1200
        average_points += 1200
    elif stage_tournament == "SF":
        sf_counts += 1
        starting_points += 720
        average_points += 720


total_points = starting_points + average_points

average_percentage = average_points / count_tournaments
total_wins = (wins_count / count_tournaments) * 100


print(f"Final points: {starting_points}")
print(f"Average points: {floor(average_percentage)}")
print(f"{total_wins:.2f}%")

