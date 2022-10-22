price_strawberries = float(input())
amount_bananas = float(input())
amount_oranges = float(input())
amount_raspberries = float(input())
amount_strawberries = float(input())

price_raspberries = price_strawberries * 0.50
price_oranges = price_raspberries * 0.60
price_bananas = price_raspberries * 0.20

total_price = (price_strawberries * amount_strawberries) + (price_bananas * amount_bananas) + \
              (price_oranges * amount_oranges) + (price_raspberries * amount_raspberries)

print(f"{total_price:.2f}")