username = input()
password = input()
password_needed = input()
while password_needed != password:
    password_needed = input()
    if password_needed == password:
        print(f"Welcome {username}!")

