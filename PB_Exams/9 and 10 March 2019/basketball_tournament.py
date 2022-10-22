name_tournament = input()
n_tournaments = int(input())
team_win = 0
win_count = 0
enemy_win = 0
lose_count = 0
count_tournaments = 0
counter = 0
while name_tournament != "End of tournaments":
    count_tournaments += n_tournaments
    for i in range(1, n_tournaments + 1):

        points_team = int(input())
        points_enemy = int(input())
        if points_team > points_enemy:
            team_win = points_team - points_enemy
            win_count += 1
            counter += 1
            print(f"Game {i} of tournament {name_tournament}: win with {team_win} points.")
        elif points_team < points_enemy:
            enemy_win = points_enemy - points_team
            lose_count += 1
            counter += 1
            print(f"Game {i} of tournament {name_tournament}: lost with {enemy_win} points.")
    name_tournament = input()
    wins_percent = (win_count / count_tournaments) * 100
    lose_percent = (lose_count / count_tournaments) * 100
    if name_tournament == "End of tournaments":
        print(f"{wins_percent:.2f}% matches win")
        print(f"{lose_percent:.2f}% matches lost")
        break
    n_tournaments = int(input())


