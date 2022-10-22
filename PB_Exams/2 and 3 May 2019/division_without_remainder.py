n = int(input())
p1 = 0
p2 = 0
p3 = 0
count = 0
for i in range(1, n + 1):
    numb = int(input())
    count += 1
    if numb % 2 == 0:
        p1 += 1
    if numb % 3 == 0:
        p2 += 1
    if numb % 4 == 0:
        p3 += 1

p1Percent = (p1 / count) * 100
p2Percent = (p2 / count) * 100
p3Percent = (p3 / count) * 100
print(f"{p1Percent:.2f}%")
print(f"{p2Percent:.2f}%")
print(f"{p3Percent:.2f}%")
