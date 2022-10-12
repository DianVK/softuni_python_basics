import math
vineyard_area = int(input())
grape_per_m2 = float(input())
needed_wine_l = int(input())
worker_count = int(input())

all_grape = vineyard_area * grape_per_m2
grape_for_wine = all_grape * 0.4
wine_lt = grape_for_wine / 2.5
difference = abs(wine_lt - needed_wine_l)

if wine_lt < needed_wine_l:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine_lt)} liters.")
    wine_per_worker = difference / worker_count
    print(f"{math.ceil(difference)} liters left -> {math.ceil(wine_per_worker)} liters per person.")



