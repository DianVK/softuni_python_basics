#Лице = π * r * r
#Периметър = 2 * π * r
#π ≈ 3.14159265358979323846…
import math
r = float(input())
calculated_area = math.pi * r * r
calculated_perimeter = 2 * math.pi * r
print(f"{calculated_area:.2f}")
print(f"{calculated_perimeter:.2f}")
