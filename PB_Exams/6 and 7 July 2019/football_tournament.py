# От конзолата се четат два реда:
name_of_team = input()
count_tournaments = int(input())
w_input = 0
d_input = 0
l_input = 0
total_points = 0
total_games = w_input + d_input + l_input

for match in range(1, count_tournaments + 1):
    result = input()
    if result == "W":
        w_input += 1
        total_points += 3
    elif result == "D":
        d_input += 1
        total_points += 1
    elif result == "L":
        l_input += 1

if total_games == 0:
    print(f"{name_of_team} hasn't played any games during this season.")
if total_points > 1:
    print(f"{name_of_team} has won {total_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {w_input}")
    print(f"## D: {d_input}")
    print(f"## L: {l_input}")
    total_games = w_input + d_input + l_input
    wins_percentage = (w_input / total_games) * 100
    print(f"Win rate: {wins_percentage:.2f}%")

