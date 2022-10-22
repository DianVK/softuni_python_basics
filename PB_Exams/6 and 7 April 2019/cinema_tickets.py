tickets_count = 0
all_tickets = 0
count_standard_ticket = 0
count_student_ticket = 0
count_kid_ticket = 0
free_ones_places = 0
movie_name = ""
while True:
    input_line = input()
    if input_line == "Finish":
        break
    else:
         movie_name = input_line
         free_ones_places = int(input())

    for i in range(1, free_ones_places + 1):
        ticketType = input()
        if ticketType == "End":
            count_tickets = (tickets_count / free_ones_places) * 100
            print(f"{movie_name} - {count_tickets:.2f}% full.")
            tickets_count = 0
            break
        else:
            tickets_count += 1
            all_tickets += 1
            if ticketType == "student":
                count_student_ticket += 1
            elif ticketType == "standard":
                count_standard_ticket += 1
            elif ticketType == "kid":
                count_kid_ticket += 1
        if i == free_ones_places:
            calculation = (tickets_count / free_ones_places) * 100
            print(f"{movie_name} - {calculation:.2f}% full.")
            tickets_count = 0

print(f"Total tickets: {all_tickets}")
calculation_student = (count_student_ticket / all_tickets) * 100
calculation_standard = (count_standard_ticket / all_tickets) * 100
calculation_kid = (count_kid_ticket / all_tickets) * 100


print(f"{calculation_student:.2f}% student tickets.")
print(f"{calculation_standard:.2f}% standard tickets.")
print(f"{calculation_kid:.2f}% kids tickets.")
