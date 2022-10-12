secure_nylon = 1.50
paint = 14.50
paint_reducer = 5.00
additional_nylon = 2 * secure_nylon
additional_bag = 0.40
needed_secure_nylon = int(input())
needed_paint = int(input())
additional_paint = needed_paint/10
needed_paint_reducer = int(input())
working_hours = int(input())
price_for_nylon = (needed_secure_nylon * secure_nylon) + additional_nylon
price_for_paint = (needed_paint + additional_paint)*paint
price_for_reducer = needed_paint_reducer * paint_reducer
total_price = price_for_reducer + price_for_nylon + price_for_paint + additional_bag
price_for_workers = (total_price * 0.30) * working_hours
price_with_work = total_price + price_for_workers
print(price_with_work)