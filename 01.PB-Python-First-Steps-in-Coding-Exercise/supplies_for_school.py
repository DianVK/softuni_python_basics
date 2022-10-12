package_pens = 5.80
package_markers = 7.20
spray = 1.20
amount_package_pens = int(input())
amount_package_markers = int(input())
amount_spray = int(input())
discount = int(input())
money_needed = (amount_spray*spray) + (amount_package_pens*package_pens) + (amount_package_markers*package_markers)
discount_calculation = discount/100
money_needed_discount = money_needed * discount_calculation
final_price = money_needed - money_needed_discount
print(final_price)
