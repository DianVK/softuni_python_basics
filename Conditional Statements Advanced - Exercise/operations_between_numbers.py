number_1 = int(input())
number_2 = int(input())
operator_symbol = input()
addition = number_1 + number_2
subtraction = number_1 - number_2
multiplication = number_1 * number_2
operation = str
if operator_symbol == "+" or operator_symbol == "-" or operator_symbol == "*":
    if operator_symbol == "+":
        if addition % 2 == 0:
            operation = "even"
            print(f"{number_1} + {number_2} = {addition} - even")
        else:
            operation = "odd"
            print(f"{number_1} + {number_2} = {addition} - odd")

    if operator_symbol == "-":
        if subtraction % 2 == 0:
            operation = "even"
            print(f"{number_1} - {number_2} = {subtraction} - even")
        else:
            operation = "odd"
            print(f"{number_1} - {number_2} = {subtraction} - odd")

    if operator_symbol == "*":
        if multiplication % 2 == 0:
            operation = "even"
            print(f"{number_1} * {number_2} = {multiplication} - even")
        else:
            operation = "odd"
            print(f"{number_1} * {number_2} = {multiplication} - odd")
if operator_symbol == "/":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        print(f"{number_1} / {number_2} = {(number_1 / number_2):.2f}")
if operator_symbol == "%":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        print(f"{number_1} % {number_2} = {(number_1 % number_2)}")