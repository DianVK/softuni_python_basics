minutes_control = int(input())
seconds_control = int(input())
length_meters = float(input())
seconds_per_meter = int(input())

minutes_control = minutes_control * 60

delay = length_meters / 120
delay = delay * 2.5
control_time = minutes_control + seconds_control

player_time = (length_meters / 100) * seconds_per_meter - delay

if player_time <= control_time:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {player_time:.3f}.")
else:
    diff = abs(player_time - control_time)
    print(f"No, Marin failed! He was {diff:.3f} second slower.")