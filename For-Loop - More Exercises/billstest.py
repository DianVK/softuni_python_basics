months_average_bill_to_pay = int(input())
waterBill = 20
internet_bill = 15
others_bill = 0
water_bill_count = 0
internet_bill_count = 0
electricity_bill_count = 0
others_bill_count = 0
for i in range(1, months_average_bill_to_pay + 1):
    electricity_bill = float(input())
    electricity_bill_count += electricity_bill
    water_bill_count += waterBill
    internet_bill_count += internet_bill
    others_bill = (electricity_bill + waterBill + internet_bill) * 1.2
    others_bill_count += others_bill
avg = (electricity_bill_count + water_bill_count + internet_bill_count + others_bill_count) / months_average_bill_to_pay
print(f"Electricity: {electricity_bill_count:.2f} lv")
print(f"Water: {water_bill_count:.2f} lv")
print(f"Internet: {internet_bill_count:.2f} lv")
print(f"Other: {others_bill_count:.2f} lv")
print(f"Average: {avg:.2f} lv")

