price_for_kilo_vegetables = float(input())
price_for_kilo_fruits = float(input())
total_kilos_vegetables = int(input())
total_kilos_fruits = int(input())
calculation_vegetables = price_for_kilo_vegetables * total_kilos_vegetables
calculation_fruits = price_for_kilo_fruits * total_kilos_fruits
total_calculation = calculation_vegetables + calculation_fruits
leva_to_euro_calc = total_calculation / 1.94
print(f"{leva_to_euro_calc:.2f}")