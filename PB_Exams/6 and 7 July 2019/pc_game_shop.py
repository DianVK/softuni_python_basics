sold_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for n in range(1, sold_games + 1):
    name_of_game = input()
    if name_of_game == "Hearthstone":
        hearthstone += 1
    elif name_of_game == "Fornite":
        fornite += 1
    elif name_of_game == "Overwatch":
        overwatch += 1
    else:
        others += 1

hearthstone_percentage = (hearthstone / sold_games) * 100
fornite_percentage = (fornite / sold_games) * 100
overwatch_percentage = (overwatch / sold_games) * 100
others_percentage = (others / sold_games) * 100

print(f"Hearthstone - {hearthstone_percentage:.2f}%")
print(f"Fornite - {fornite_percentage:.2f}%")
print(f"Overwatch - {overwatch_percentage:.2f}%")
print(f"Others - {others_percentage:.2f}%")