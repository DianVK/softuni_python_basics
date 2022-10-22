# 1.	Име на авиокомпанията - текст
# 2.	Брой билети за	 възрастни – цяло число в диапазона [1…400]
# 3.	Брой детски билети – цяло число в диапазона [25…120]
# 4.	Нетна цена на билет за възрастен – реално число в диапазона [100.0…1600.0]
# 5.	Цената на такса обслужване - реално число в диапазона [10.0…50.0]

name = input()
count_tickets = int(input())
count_kids_tickets = int(input())
price_ticket = float(input())
price_kid_ticket = price_ticket * 0.30
tax_comision = float(input())

price_per_adult = price_ticket + tax_comision
price_per_kid = price_kid_ticket + tax_comision
total_price = (price_per_kid * count_kids_tickets) + (price_per_adult * count_tickets)
win = total_price * 0.20
print(f"The profit of your agency from {name} tickets is {win:.2f} lv.")