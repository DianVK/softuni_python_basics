from math import floor, ceil
magnoliasCount = int(input())
hyathinthusCount = int(input())
rosesCount = int(input())
cactiCount = int(input())
price_gift = float(input())
magnoliasPrice = magnoliasCount * 3.25
hyathinthusPrice = hyathinthusCount * 4
rosesPrice = rosesCount * 3.5
cactiPrice = cactiCount * 8
totalPrice = magnoliasPrice + hyathinthusPrice + rosesPrice + cactiPrice
taxes = totalPrice * 0.05
profit = totalPrice - taxes
if profit >= price_gift:
    result = profit - price_gift
    print(f"She is left with {floor(result)} leva.")
else:
    result = price_gift - profit
    print(f"She will have to borrow {ceil(result)} leva.")

