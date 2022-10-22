count_days = int(input())
wins = 0
loses = 0
total_charity = 0
for i in range(1, count_days + 1):
    sport = input()
    result = input()
    charity = 0
    win = 0
    lose = 0
    while True:
        if result == "win":
            charity += 20
            win += 1
        elif result == "lose":
            lose += 1
        sport = input()
        if sport == "Finish" and win > lose:
            charity = charity * 1.10
            break
        elif sport == "Finish" and lose > win:
            break
        result = input()
    wins += win
    loses += lose
    total_charity += charity


if wins > loses:
    total_charity = total_charity * 1.20
    print(f"You won the tournament! Total raised money: {total_charity:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_charity:.2f}")


