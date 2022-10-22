count_red = 0
count_orange = 0
count_blue = 0
count_green = 0
best_egg = 0
best = ""
count_eggs = int(input())
for i in range(1,count_eggs +1):
    paint = input()
    if paint == "red":
        count_red += 1
    elif paint == "orange":
        count_orange += 1
    elif paint == "blue":
        count_blue += 1
    elif paint == "green":
        count_green += 1

if count_red > count_green and count_red > count_blue and count_red > count_orange:
    best_egg = count_red
    best = "red"
elif count_orange > count_blue and count_orange > count_green and count_orange > count_red:
    best_egg = count_orange
    best = "orange"
elif count_blue > count_orange and count_blue > count_green and count_blue > count_red:
    best_egg = count_blue
    best = "blue"
elif count_green > count_blue and count_green > count_orange and count_green > count_red:
    best_egg = count_green
    best = "green"

print(f"Red eggs: {count_red}")
print(f"Orange eggs: {count_orange}")
print(f"Blue eggs: {count_blue}")
print(f"Green eggs: {count_green}")
print(f"Max eggs: {best_egg} -> {best}")


