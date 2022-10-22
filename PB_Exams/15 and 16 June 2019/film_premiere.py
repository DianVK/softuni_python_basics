projection = input()
package = input()
count_tickets = int(input())
price = 0
if projection == "John Wick":
    if package == "Drink":
        price = 12
    elif package == "Popcorn":
        price = 15
    elif package == "Menu":
        price = 19
elif projection == "Star Wars":
    if package == "Drink":
        price = 18
    elif package == "Popcorn":
        price = 25
    elif package == "Menu":
        price = 30
elif projection == "Jumanji":
    if package == "Drink":
        price = 9
    elif package == "Popcorn":
        price = 11
    elif package == "Menu":
        price = 14

total_price = count_tickets * price
if projection == "Star Wars" and count_tickets >= 4:
    total_price = total_price * 0.70
elif projection == "Jumanji" and count_tickets == 2:
    total_price = total_price * 0.85


print(f"Your bill is {total_price:.2f} leva.")



