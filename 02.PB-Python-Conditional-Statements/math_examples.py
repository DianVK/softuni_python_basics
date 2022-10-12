#chetno ili nechetno
import math
number = int(input())
if number % 2 == 0:
    print("even")
else:
    print("odd")
#zakruglqne do po golqmo
up = math.ceil (23.45)
print(up)
#zakruglqne do po malko
down = math.floor(24.55)
print(down)
#namirane na absolutna stoinost (stoinosta do 0)
example1=abs(50)
print(example1)
example2=abs(-50)
print(example2)
#zakruglqne na danni
rounding = round(23.541342, 2)
print(rounding)
#formatirane do 2 znaka sled desetichniq znak
print(f"{12.2452:.2f}")
#Разлика между форматиране и закръгляне:
print(round(45.60000, 4)) # 45.6
print(f"{45.60000:.4f}") # 45.6000