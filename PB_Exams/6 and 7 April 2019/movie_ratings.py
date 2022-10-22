import sys
count_movies = int(input())
movie_best_rating = ""
movie_lowest_rating = ""
best_rating = -sys.maxsize
lowest_rating = sys.maxsize
average_rating = 0
for movie in range(1, count_movies + 1):
    movie_name = input()
    movie_rating = float(input())
    average_rating += movie_rating
    if movie_rating > best_rating:
        best_rating = movie_rating
        movie_best_rating = movie_name

    elif movie_rating < lowest_rating:
        lowest_rating = movie_rating
        movie_lowest_rating = movie_name


average_rating = average_rating / count_movies
print(f"{movie_best_rating} is with highest rating: {best_rating:.1f}")
print(f"{movie_lowest_rating} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
