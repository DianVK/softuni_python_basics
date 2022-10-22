
start = int(input())
end = int(input())

first_start = (start / 1000) % 10
second_start = (start / 100) % 10
third_start = (start / 10) % 10
fourth_start = start % 10

first_end = (end / 1000) % 10
second_end = (end / 100) % 10
third_end = (end / 10) % 10
fourth_end = end % 10


for num1 in range(int(first_start), int(first_end +1)):
    for num2 in range(int(second_start), int(second_end +1)):
        for num3 in range(int(third_start), int(third_end +1)):
            for num4 in range(int(fourth_start), int(fourth_end +1)):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")


