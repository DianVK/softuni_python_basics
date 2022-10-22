# •	1 биткойн = 1168 лева.
# •	1 китайски юан = 0.15 долара.
# •	1 долар = 1.76 лева.
# •	1 евро = 1.95 лева.

count_bitcoins = int(input())
count_chinese_ioans = float(input())
comision = float(input())

price_bitcoin = 1168
price_chinece_ioan = 0.15
price_dolar = 1.76
price_euro = 1.95

price_bitcoin = price_bitcoin * count_bitcoins
price_chinece_ioan = price_chinece_ioan * count_chinese_ioans
price_ioan_to_leva = price_chinece_ioan * price_dolar

total_price = price_bitcoin + price_ioan_to_leva
total_price = total_price / price_euro
comision = (comision * total_price) / 100
total_price = total_price - comision
print(f"{total_price:.2f}")