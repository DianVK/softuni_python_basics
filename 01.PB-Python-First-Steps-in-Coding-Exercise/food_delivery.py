chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery = 2.50
amount_chicken = int(input())
amount_fish = int(input())
amount_vegan = int(input())
chicken_count = chicken_menu * amount_chicken
fish_count = fish_menu * amount_fish
vegan_count = vegan_menu * amount_vegan
price = fish_count + chicken_count + vegan_count
desert = price*0.20
last_price = vegan_count + chicken_count + fish_count + desert + delivery
print(last_price)