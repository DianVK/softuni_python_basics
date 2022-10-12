#височина на къщата
x = float(input())
#дължината на страничната стена
y = float(input())
#височината на триъгълната стена на прокрива
h = float(input())
side_of_house = x * y
window = 1.5 * 1.5
two_sides_sum = (2 * side_of_house) - (2 * window)
rear_side_of_house = x * x
calc_entrance = 1.2*2
sum_front_and_rear = (2*rear_side_of_house) - calc_entrance
total_area = two_sides_sum + sum_front_and_rear
green_paint = total_area / 3.4
print(f"{green_paint:.2f}")
two_sides_roof = 2 * (x * y)
front_and_rear_roof = 2 * (x*h / 2)
total_area_roof = front_and_rear_roof + two_sides_roof
red_paint = total_area_roof / 4.3
print(f"{red_paint:.2f}")