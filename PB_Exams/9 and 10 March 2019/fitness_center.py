# От конзолата се чете число, след това поредица от низове, всяко на отделен ред:
# •	На първия ред – броят на посетителите във фитнеса – цяло число в интервала [1...1000]
# •	За всеки един посетител на отделен ред – дейността във фитнеса – текст ("Back", "Chest", "Legs", "Abs", "Protein shake" или "Protein bar")
count_people = int(input())
counter_back = 0
counter_chest = 0
counter_legs = 0
counter_abs = 0
counter_protein_shake = 0
counter_protein_bar = 0
total_training = 0
total_protein = 0
for i in range(1, count_people + 1):
    body_part = input()
    if body_part == "Back":
        counter_back += 1
        total_training += 1
    elif body_part == "Chest":
        counter_chest += 1
        total_training += 1
    elif body_part == "Legs":
        counter_legs += 1
        total_training += 1
    elif body_part == "Abs":
        counter_abs += 1
        total_training += 1
    elif body_part == "Protein shake":
        counter_protein_shake += 1
        total_protein += 1
    elif body_part == "Protein bar":
        counter_protein_bar += 1
        total_protein += 1
percent_people = (total_training / count_people) * 100
percent_protein = (total_protein / count_people) * 100
print(f"{counter_back} - back")
print(f"{counter_chest} - chest")
print(f"{counter_legs} - legs")
print(f"{counter_abs} - abs")
print(f"{counter_protein_shake} - protein shake")
print(f"{counter_protein_bar} - protein bar")
print(f"{percent_people:.2f}% - work out")
print(f"{percent_protein:.2f}% - protein")

