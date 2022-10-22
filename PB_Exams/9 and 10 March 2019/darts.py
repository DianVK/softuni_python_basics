name = input()
score = 301
shots_successful = 0
shots_unsuccessful = 0

type = input()


while type != "Retire":

    points = int(input())

    if type == "Single":
        score -= points
        if score >= 0:
            shots_successful += 1
        else:
            shots_unsuccessful += 1
            score += points

    elif type == "Double":
        score -= points * 2
        if score >= 0:
            shots_successful += 1
        else:
            shots_unsuccessful += 1
            score += points * 2

    elif type == "Triple":
        score -= points * 3
        if score >= 0:
            shots_successful += 1
        else:
            shots_unsuccessful +=1
            score += points * 3

    if score == 0:
        print(f"{name} won the leg with {shots_successful:.0f} shots.")
        break

    type = input()


if type == "Retire":
    print(f"{name} retired after {shots_unsuccessful:.0f} unsuccessful shots.")

