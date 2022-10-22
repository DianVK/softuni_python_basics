movie_name = input()
type_hall = input()
count_tickets = int(input())
price_of_ticket = 0
total_price = 0
if movie_name == "A Star Is Born":
    if type_hall == "normal":
        price_of_ticket = 7.50
        total_price += price_of_ticket
    elif type_hall == "luxury":
        price_of_ticket = 10.50
        total_price += price_of_ticket
    elif type_hall == "ultra luxury":
        price_of_ticket = 13.50
        total_price += price_of_ticket
elif movie_name == "Bohemian Rhapsody":
    if type_hall == "normal":
        price_of_ticket = 7.35
        total_price += price_of_ticket
    elif type_hall == "luxury":
        price_of_ticket = 9.45
        total_price += price_of_ticket
    elif type_hall == "ultra luxury":
        price_of_ticket = 12.75
        total_price += price_of_ticket
elif movie_name == "Green Book":
    if type_hall == "normal":
        price_of_ticket = 8.15
        total_price += price_of_ticket
    elif type_hall == "luxury":
        price_of_ticket = 10.25
        total_price += price_of_ticket
    elif type_hall == "ultra luxury":
        price_of_ticket = 13.25
        total_price += price_of_ticket
elif movie_name == "The Favourite":
    if type_hall == "normal":
        price_of_ticket = 8.75
        total_price += price_of_ticket
    elif type_hall == "luxury":
        price_of_ticket = 11.55
        total_price += price_of_ticket
    elif type_hall == "ultra luxury":
        price_of_ticket = 13.95
        total_price += price_of_ticket
print(f"{movie_name} -> {(total_price * count_tickets):.2f} lv.")
