# Първоначално се чете един ред:
# •	Брой дни – цяло число в диапазона [1…30]
# •	Общо количество храна – реално число в диапазона [0.00…10000.00]
# След това за всеки ден се чете:
# o	Количество изядена храна от кучето – цяло число в диапазона [10…500]
# o	Количество изядена храна от котката – цяло число в диапазона [10…500]

count_days = int(input())
amount_food = float(input())
counter = 0
total_eated_food = 0
eated_food_per_day = 0
biscuit = 0
food_eaten_from_dog = 0
food_eaten_from_cat = 0
for day in range (1, count_days + 1):
    food_dog = int(input())
    food_cat = int(input())
    food_eaten_from_dog += food_dog
    food_eaten_from_cat += food_cat
    total_eated_food += food_cat + food_dog
    eated_food_per_day = food_cat + food_dog
    counter += 1
    if counter % 3 == 0:
        biscuit += eated_food_per_day * 0.10

print(f"Total eaten biscuits: {round(biscuit)}gr.")
percentage = (total_eated_food / amount_food) * 100
percentage_dog = (food_eaten_from_dog / total_eated_food) * 100
percentage_cat = (food_eaten_from_cat / total_eated_food) * 100
print(f"{percentage:.2f}% of the food has been eaten.")
print(f"{percentage_dog:.2f}% eaten from the dog.")
print(f"{percentage_cat:.2f}% eaten from the cat.")

