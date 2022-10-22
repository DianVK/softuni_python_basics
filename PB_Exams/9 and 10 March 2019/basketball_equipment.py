year_tax = int(input())
# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
shoes = year_tax * 0.60
outfit = shoes * 0.80
ball = outfit / 4
accessoares = ball / 5
total_price = year_tax + shoes + outfit + ball + accessoares

print(f"{total_price:.2f}")