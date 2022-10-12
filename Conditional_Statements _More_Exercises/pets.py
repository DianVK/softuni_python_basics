from math import floor
from math import ceil
broi_dni = int(input())
ostavena_hrana = int(input())
hrana_kuche = float(input())
hrana_kote = float(input())
hrana_kostenurka = float(input())
calculation1 = broi_dni * hrana_kuche
calculation2 = broi_dni * hrana_kote
calculation3 = broi_dni*(hrana_kostenurka/1000)
calculation4 = calculation1 + calculation3 + calculation2
if calculation4 <= ostavena_hrana:
    calculation5 = floor(ostavena_hrana - calculation4)
    print(f"{calculation5} kilos of food left.")
elif calculation4 > ostavena_hrana:
    calculation6 = ceil(calculation4 - ostavena_hrana)
    print(f"{calculation6} more kilos of food are needed.")




