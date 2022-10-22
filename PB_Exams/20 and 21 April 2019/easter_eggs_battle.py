count_eggs_first = int(input())
count_eggs_second = int(input())

winner = input()
while winner != "End":
    if winner == "one":
        count_eggs_second -= 1
        if count_eggs_second == 0:
            print(f"Player two is out of eggs. Player one has {count_eggs_first} eggs left.")
            break
    elif winner == "two":
        count_eggs_first -= 1
        if count_eggs_first == 0:
            print(f"Player one is out of eggs. Player two has {count_eggs_second} eggs left.")
            break

    winner = input()
if count_eggs_first > 0 and count_eggs_second > 0:
    print(f"Player one has {count_eggs_first} eggs left.")
    print(f"Player two has {count_eggs_second} eggs left.")
