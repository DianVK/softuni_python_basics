hrizantemi = int(input())
roses = int(input())
laleta = int(input())
season = input()
holiday = input()
price_hrizantemi = 0
price_laleta = 0
price_roses = 0
total_flowers = hrizantemi + roses + laleta
if season == "Spring" or season == "Summer":
    price_hrizantemi = hrizantemi * 2
    price_roses = roses * 4.10
    price_laleta = laleta * 2.50
elif season == "Autumn" or season == "Winter":
    price_hrizantemi = hrizantemi * 3.75
    price_roses = roses * 4.50
    price_laleta = laleta * 4.15
total_price = price_roses + price_laleta + price_hrizantemi
if holiday == "Y":
    total_price = total_price * 1.15
if laleta > 7 and season == "Spring":
    total_price = total_price * 0.95
if roses >= 10 and season == "Winter":
    total_price = total_price * 0.90
if total_flowers > 20:
    total_price = total_price * 0.80
total_price += 2
print(f"{total_price:.2f}")



