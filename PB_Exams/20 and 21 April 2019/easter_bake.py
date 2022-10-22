import sys
from math import ceil
package_sugar = 950
package_brashno = 750
max_gram_brashno = -sys.maxsize
max_gram_sugar = -sys.maxsize
count_kozunaci = int(input())
needed_sugar = 0
needed_brashno = 0
for i in range(1,count_kozunaci + 1):
    sugar = int(input())
    needed_sugar += sugar
    if sugar > max_gram_sugar:
        max_gram_sugar = sugar
    brashno = int(input())
    needed_brashno += brashno
    if brashno > max_gram_brashno:
        max_gram_brashno = brashno


sugar = ceil(needed_sugar / package_sugar)
brashno = ceil(needed_brashno / package_brashno)

print(f"Sugar: {sugar}")
print(f"Flour: {brashno}")
print(f"Max used flour is {max_gram_brashno} grams, max used sugar is {max_gram_sugar} grams.")
