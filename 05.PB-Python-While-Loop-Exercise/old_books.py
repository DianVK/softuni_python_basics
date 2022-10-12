book = input()
searching_book = input()
count_books = 0
while searching_book != "No More Books":
    if searching_book == book:
        print(f"You checked {count_books} books and found it.")
        break
    searching_book = input()
    count_books += 1
if searching_book == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {count_books} books.")
