year_tax = int(input())
shoes = year_tax - (year_tax*0.40)
outfit = shoes - (shoes*0.20)
ball = outfit*0.25
accesoaries = ball*0.20
price = year_tax + shoes + outfit + ball + accesoaries
print(price)