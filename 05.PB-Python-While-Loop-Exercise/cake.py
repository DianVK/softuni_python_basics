width = int(input())
length = int(input())
count_pieces = input()
full_size_cake = width * length
counting = full_size_cake
while count_pieces != "STOP":
    counter_pieces = int(count_pieces)
    counting -= counter_pieces

    if counting < 0:
        print(f"No more cake left! You need {abs(counting)} pieces more.")
        break
    count_pieces = input()

if count_pieces == "STOP":
    print(f"{counting} pieces are left.")
