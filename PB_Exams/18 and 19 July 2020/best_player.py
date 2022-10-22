import sys

best_player = ""
best_score = -sys.maxsize

name_player = input()
count_goals = int(input())
while True:
    if count_goals > best_score:
        best_player = name_player
        best_score = count_goals
    if count_goals >= 10:
        break
    name_player = input()
    if name_player == "END":
        break
    count_goals = int(input())


print(f"{best_player} is the best player!")
if best_score >= 3:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
elif best_score < 3:
    print(f"He has scored {best_score} goals.")
