movie_name = input()
counter = 0
best_movie = ""
max_points = 0
while movie_name != "STOP":
    counter += 1
    if counter == 7:
        break
    current_points = 0
    for letter in movie_name:
        current_points += ord(letter)
        if letter.islower():
            current_points -= len(movie_name) * 2
        elif letter.isupper():
            current_points -= len(movie_name)
    if current_points > max_points:
        best_movie = movie_name
        max_points = current_points
    current_points = 0
    movie_name = input()
if counter == 7:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {max_points} ASCII sum.")