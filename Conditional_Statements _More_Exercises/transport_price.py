n = int(input())
time = input()

taxi_day = (n * 0.79) + 0.70
taxi_night = (n * 0.90) + 0.70

bus = n * 0.09
train = n * 0.06

if n < 20 and time == "day":
    print(f'{taxi_day:.2f}')
elif n < 20 and time == "night":
    print(f'{taxi_night:.2f}')
elif 20 <= n < 100:
    print(f'{bus:.2f}')
elif n >= 100:
    print(f'{train:.2f}')
