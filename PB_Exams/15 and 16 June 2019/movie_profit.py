name_of_movie = input()
count_days = int(input())
count_tickets = int(input())
price_ticket = float(input())
cinema_percentage = int(input())


cinema_income = count_days * (count_tickets * price_ticket)
cinema_income_percentage = cinema_income * (cinema_percentage / 100)
income = cinema_income - cinema_income_percentage


print(f"The profit from the movie {name_of_movie} is {income:.2f} lv.")


