name_serial = input()
count_seasons = int(input())
count_episodes = int(input())
timelapse_episode = float(input())
special_episode_count = 0

advertisement = timelapse_episode * 0.20
special_episodes = count_seasons * 10
minutes = advertisement + timelapse_episode
total_episodes = count_episodes * count_seasons
total_minutes = (total_episodes * minutes) + special_episodes
print(f"Total time needed to watch the {name_serial} series is {total_minutes:.0f} minutes.")

