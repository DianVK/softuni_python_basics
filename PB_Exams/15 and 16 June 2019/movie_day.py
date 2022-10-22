photos_time = int(input())
count_scenes = int(input())
scene_time = int(input())
preparation_time = photos_time * 0.15

total_needed_time = (count_scenes * scene_time) + preparation_time
if photos_time < total_needed_time:
    print(f"Time is up! To complete the movie you need {(total_needed_time - photos_time):.0f} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {(photos_time - total_needed_time):.0f} minutes left!")

