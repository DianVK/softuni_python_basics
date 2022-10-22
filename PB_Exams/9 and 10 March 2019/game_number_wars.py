player_one_name = input()
player_two_name = input()
playerOnePoints = 0
playerTwoPoints = 0
while True:
    command = input()
    if command == "End of game":
        print(f"{player_one_name} has {playerOnePoints} points")
        print(f"{player_two_name} has {playerTwoPoints} points")
        break

    card_player_one = int(command)
    command = input()
    card_player_two = int(command)

    if card_player_one > card_player_two:
        playerOnePoints += abs(card_player_one - card_player_two)
    elif card_player_two > card_player_one:
        playerTwoPoints += abs(card_player_one - card_player_two)
    else:
        print(f"Number wars!")
        command = input()
        card_player_one = int(command)
        command = input()
        card_player_two = int(command)
        if card_player_one > card_player_two:
            print(f"{player_one_name} is winner with {playerOnePoints} points")

        else:
            print(f"{player_two_name} is winner with {playerTwoPoints} points")
        break