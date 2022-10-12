count_cargo = int(input())
count_bus = 0
count_truck = 0
count_train = 0
total_tons = 0
total_cash = count_train + count_truck + count_bus
for i in range(1, count_cargo +1):
    weight_tons_of_cargo = int(input())
    total_tons += weight_tons_of_cargo

    if weight_tons_of_cargo < 4:
        count_bus += weight_tons_of_cargo

    elif weight_tons_of_cargo < 12:
        count_truck += weight_tons_of_cargo

    elif weight_tons_of_cargo >= 12:
        count_train += weight_tons_of_cargo

average_bus = count_bus * 200
average_truck = count_truck * 175
average_train = count_train * 120
average_sum = average_train + average_truck + average_bus
average = average_sum / total_tons
print(f"{average:.2f}")
percent_bus = (count_bus / total_tons) * 100
percent_truck = (count_truck / total_tons) * 100
percent_train = (count_train / total_tons) * 100
print(f"{percent_bus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")