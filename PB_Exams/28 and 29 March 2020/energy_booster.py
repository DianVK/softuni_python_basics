fruit = input()
size = input()
amount = int(input())
price = 0
if fruit == "Watermelon":
    if size == "small":
        price = 2 * 56
    elif size == "big":
        price = 5 * 28.70
if fruit == "Mango":
    if size == "small":
        price = 2 * 36.66
    elif size == "big":
        price = 5 * 19.60
if fruit == "Pineapple":
    if size == "small":
        price = 2 * 42.10
    elif size == "big":
        price = 5 * 24.80
if fruit == "Raspberry":
    if size == "small":
        price = 2 * 20
    elif size == "big":
        price = 5 * 15.20

cash = price * amount

# •	от 400 лв. до 1000 лв. включително има 15% отстъпка
# •	над 1000 лв. има 50% отстъпка

if 400 <= cash <= 1000:
    cash = cash * 0.85
elif cash > 1000:
    cash = cash * 0.50

print(f"{cash:.2f} lv.")
