pages_in_book = int(input())
pages_read_for_hour = int(input())
days_to_read = int(input())
calculation = pages_in_book / pages_read_for_hour
secondcalculation = int(calculation / days_to_read)
print(secondcalculation)