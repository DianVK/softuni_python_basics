h = float(input())
w = float(input())
work_station_row = w // 1.2
work_station_column = (h - 1) // 0.7
total_work_station = (work_station_row * work_station_column)
print(total_work_station)