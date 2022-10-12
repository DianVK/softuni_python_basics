steps = int(input())
sum_steps = steps
while sum_steps < 10000:
    steps_inp = input()
    if steps_inp == "Going home":
        last_steps = int(input())
        sum_steps += last_steps
        break
    steps_input = int(steps_inp)
    sum_steps += steps_input
diff = abs(sum_steps - 10000)
if sum_steps >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    steps_less = 10000 - sum_steps
    print(f"{diff} more steps to reach goal.")
