length = int(input())
width = int(input())
hight = int(input())
percentage = float(input())
capacity = length * width * hight
capacity_of_liters = capacity*0.001
percentage_area = percentage*0.01
needed_liters = capacity_of_liters * (1 - percentage_area)
print(needed_liters)