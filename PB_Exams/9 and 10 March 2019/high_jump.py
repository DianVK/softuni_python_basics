height_centimeters = int(input())
level = height_centimeters - 30
fails = 0
jump_counter = 0
while fails < 3:
    current_jump = int(input())
    jump_counter += 1
    if current_jump > level:
        level += 5
        fails = 0
    else:
        fails += 1
    if level > height_centimeters:
        print(f"Tihomir succeeded, he jumped over {height_centimeters}cm after {jump_counter} jumps.")
        exit()
print(f"Tihomir failed at {level}cm after {jump_counter} jumps.")