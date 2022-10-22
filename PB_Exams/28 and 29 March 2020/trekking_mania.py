count_groups = int(input())
musala = 0
monblan = 0
kili = 0
k2 = 0
everest = 0
total_people = 0
for i in range(1 , count_groups + 1):
    count_people = int(input())
    total_people += count_people
    if count_people <= 5:
        musala += count_people
    elif 6 <= count_people <= 12:
        monblan += count_people
    elif 13 <= count_people <= 25:
        kili += count_people
    elif 26 <= count_people <= 40:
        k2 += count_people
    elif count_people >= 41:
        everest += count_people

percent_musala = (musala / total_people) * 100
percent_monblan = (monblan / total_people) * 100
percent_kili = (kili / total_people) * 100
percent_k2 = (k2 / total_people) * 100
percent_everest = (everest / total_people) * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kili:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")


