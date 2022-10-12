count_bottles_cleaner = int(input())
count_dishes = input()
dishes = 0
counter = 1
total_ml_cleaner = count_bottles_cleaner * 750
used_cleaner_plates = 0
used_cleaner_pots = 0
used_cleaner = 0
count_plates = 0
count_pots = 0

while count_dishes != "End":
    dishes = int(count_dishes)
    if counter % 3 == 0:
        used_cleaner_pots = dishes * 15
        total_ml_cleaner = (total_ml_cleaner - used_cleaner_pots)
        count_pots += dishes
        used_cleaner = used_cleaner_pots
    else:
        used_cleaner_plates = dishes * 5
        total_ml_cleaner = (total_ml_cleaner - used_cleaner_plates)
        count_plates += dishes
        used_cleaner = used_cleaner_plates
    if total_ml_cleaner < 0:
        print(f"Not enough detergent, {abs(total_ml_cleaner)} ml. more necessary!")
        break
    count_dishes = input()
    counter += 1
if total_ml_cleaner >= 0:
    print("Detergent was enough!")
    print(f"{count_plates} dishes and {count_pots} pots were washed.")
    print(f"Leftover detergent {total_ml_cleaner} ml.")