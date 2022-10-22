from math import floor

n = int(input())
points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
others = 0
for i in range(1, n + 1):
    color = input()
    if color == "red":
        points += 5
        red += 1
    elif color == "orange":
        points += 10
        orange += 1
    elif color == "yellow":
        points += 15
        yellow += 1
    elif color == "white":
        points += 20
        white += 1
    elif color == "black":
        points = floor(points / 2)
        black += 1
    else:
        points = points
        others += 1

print(f"Total points: {points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {others}")
print(f"Divides from black balls: {black}")
