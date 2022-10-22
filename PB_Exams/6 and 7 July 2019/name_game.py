name = input()
char_letter = 0
max_score = 0
winner_name = ""
while name != "Stop":
    current_score = 0
    for i in range(len(name)):
        char_letter = ord(name[i])
        n = int(input())
        if char_letter == n:
            current_score = current_score + 10
        else:
            current_score = current_score + 2
        if current_score >= max_score:
            max_score = current_score
            winner_name = name
    name = input()
print(f"The winner is {winner_name} with {max_score} points!")
