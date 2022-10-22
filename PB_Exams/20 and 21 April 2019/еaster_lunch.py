# •	Брой козунаци - цяло число в интервала [0 … 99]
# •	Брой кори с яйца - цяло число в интервала [0 … 99]
# •	Килограми курабии - цяло число в интервала [0 … 99]
# •	Козунак  – 3.20 лв.
# •	Яйца –  4.35 лв. за кора с 12 яйца
# •	Курабии – 5.40 лв. за килограм
# •	Боя за яйца - 0.15 лв. за яйце
count_kozunaci = int(input())
count_eggs = int(input())
count_cookies = int(input())
eggs_price = 4.35
eggs_paint = (count_eggs * 12) * 0.15
kozunaci_price = count_kozunaci * 3.20
eggs_price_total = count_eggs * eggs_price
total_price_cookies = count_cookies * 5.40
total_price = kozunaci_price + eggs_price_total + eggs_paint + total_price_cookies

print(f"{total_price:.2f}")
