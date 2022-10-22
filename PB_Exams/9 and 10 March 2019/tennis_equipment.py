from math import ceil
from math import floor
price_per_rocket = float(input())
count_rockets = int(input())
count_shoes = int(input())
price_shoes = (price_per_rocket / 6) * count_shoes

total_price = price_shoes + (price_per_rocket * count_rockets)
stuff = total_price * 0.20
total = total_price + stuff
djakovic = total / 8
sponsors = total * 7 / 8

print(f"Price to be paid by Djokovic {floor(djakovic)}")
print(f"Price to be paid by sponsors {ceil(sponsors)}")

