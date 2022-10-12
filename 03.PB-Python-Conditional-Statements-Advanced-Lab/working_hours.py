hour = int(input())
weekday = input()

if weekday == 'Sunday' or hour < 10 or hour > 18:
    print('closed')
else:
    print('open')