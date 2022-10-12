import math

type_figure = input()
if type_figure == "square":
    size_square = float(input())
    a = size_square
    b = a * a
    print(f"{b:.3f}")
elif type_figure == "rectangle":
    lenght_rectangle = float(input())
    sides_rectangle = float(input())
    c = lenght_rectangle * sides_rectangle
    print(f"{c:.3f}")
elif type_figure == "circle":
    radius_circle = float(input())
    d = (radius_circle * radius_circle) * math.pi
    print(f"{d:.3f}")
elif type_figure == "triangle":
    side_triangle = float(input())
    lenght_triangle = float(input())
    g = lenght_triangle / 2
    h = side_triangle * g
    print(f"{h:.3f}")