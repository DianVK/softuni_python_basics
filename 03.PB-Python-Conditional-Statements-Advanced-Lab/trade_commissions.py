city = input()
volume = float(input())
percentage = -1
if city == "Sofia":
    if volume >= 0 and volume <= 500: percentage = 0.05
    elif volume > 500 and volume <= 1000: percentage = 0.07
    elif volume > 1000 and volume <= 10000: percentage = 0.08
    elif volume > 10000: percentage = 0.12
if city == "Varna":
    if volume >= 0 and volume <= 500: percentage = 0.045
    elif volume > 500 and volume <= 1000: percentage = 0.075
    elif volume > 1000 and volume <= 10000: percentage = 0.10
    elif volume > 10000: percentage = 0.13
if city == "Plovdiv":
    if volume >= 0 and volume <= 500: percentage = 0.055
    elif volume > 500 and volume <= 1000: percentage = 0.08
    elif volume > 1000 and volume <= 10000: percentage = 0.12
    elif volume > 10000: percentage = 0.145
if percentage >= 0:
    print(f"{volume * percentage:.2f}")
else:
    print("error")
