brashno_price_per_kg = float(input())
kg_brashno = float(input())
kg_sugar = float(input())
amount_packages_eggs = int(input())
packages_maya = int(input())

price_kg_sugar = brashno_price_per_kg * 0.75
price_per_package_eggs = brashno_price_per_kg * 1.10
price_per_package_maya = price_kg_sugar * 0.20

sugar = price_kg_sugar * kg_sugar
brashno = brashno_price_per_kg * kg_brashno
eggs = price_per_package_eggs * amount_packages_eggs
maya = price_per_package_maya * packages_maya

total_sum = brashno + eggs + maya + sugar
print(f"{total_sum:.2f}")