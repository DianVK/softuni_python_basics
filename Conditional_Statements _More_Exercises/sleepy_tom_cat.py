holidays = int(input())

game_limit_min_yearly = 30000
days_year = 365
workdays_play_min_day = 63
holidays_play_min_day = 127

workdays = days_year - holidays
total_play_min_yearly = (holidays * holidays_play_min_day) + (workdays * workdays_play_min_day)

difference_min = abs(total_play_min_yearly - game_limit_min_yearly)
hours = difference_min // 60
minutes = difference_min % 60

if total_play_min_yearly > game_limit_min_yearly:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")