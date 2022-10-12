problem_scores = int(input())
name_of_task = input()
sum_scores = 0
count_scores = 0
problem_scores_count = 0

while name_of_task != "Enough":
    last_name_of_task_save = name_of_task
    current_score = int(input())
    sum_scores += current_score
    count_scores += 1
    if current_score <= 4:
        problem_scores_count += 1
    if problem_scores == problem_scores_count:
        print(f"You need a break, {problem_scores_count} poor grades.")
        break
    name_of_task = input()
if name_of_task == "Enough":
    average = sum_scores / count_scores
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {count_scores}")
    print(f"Last problem: {last_name_of_task_save}")
