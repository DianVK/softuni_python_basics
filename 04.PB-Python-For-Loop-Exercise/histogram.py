numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(1, numbers + 1):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif 200 <= current_num <= 399:
        p2 += 1
    elif 400 <= current_num <= 599:
        p3 += 1
    elif 600 <= current_num <= 799:
        p4 += 1
    elif 800 <= current_num:
        p5 += 1
p1_percentage = p1 / numbers * 100
print(f"{p1_percentage:.2f}%")
p2_percentage = p2 / numbers * 100
print(f"{p2_percentage:.2f}%")
p3_percentage = p3 / numbers * 100
print(f"{p3_percentage:.2f}%")
p4_percentage = p4 / numbers * 100
print(f"{p4_percentage:.2f}%")
p5_percentage = p5 / numbers * 100
print(f"{p5_percentage:.2f}%")


