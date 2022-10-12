import sys
biggest = -sys.maxsize
smallest = sys.maxsize
n = int(input())
for i in range(0, n):
    num = int(input())
    if num < smallest:
        smallest = num
    if num > biggest:
        biggest = num
print(f"Max number: {biggest}")
print(f"Min number: {smallest}")

