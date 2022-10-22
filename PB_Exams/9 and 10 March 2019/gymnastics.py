# •	Първи ред – държава – текст ("Russia", "Bulgaria" или "Italy")
# •	Втори ред – уред - текст ("ribbon", "hoop" или "rope")
country = input()
item = input()
difficulty = 0
performance = 0
goal = 20.00
if country == "Russia":
    if item == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif item == "hoop":
        difficulty = 9.300
        performance = 9.800
    elif item == "rope":
        difficulty = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if item == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif item == "hoop":
        difficulty = 9.550
        performance = 9.750
    elif item == "rope":
        difficulty = 9.500
        performance = 9.400
elif country == "Italy":
    if item == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif item == "hoop":
        difficulty = 9.450
        performance = 9.350
    elif item == "rope":
        difficulty = 9.700
        performance = 9.150

total_score = difficulty + performance
diff = abs(goal - total_score)
percent = (diff / 20) * 100
print(f"The team of {country} get {total_score:.3f} on {item}.")
print(f"{percent:.2f}%")


