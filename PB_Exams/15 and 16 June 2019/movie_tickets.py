a1 = int(input())
a2 = int(input())
n = int(input())
m = int(n / 2)
for i in range(a1, a2):
    for j in range(1, n):
        for k in range(1, m):
            if i % 2 == 1 and ((j + k + i) % 2 == 1):
                print(f"{chr(i)}-{j}{k}{i}")