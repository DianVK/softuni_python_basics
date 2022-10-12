counter_c = 0
counter_n = 0
counter_o = 0
final_result = ""
current_result = ""
letter = input()
while letter != "End":
    if letter.isalpha():
        if letter == "c":
            counter_c += 1
            if counter_c > 1:
                current_result += letter
        elif letter == "o":
            counter_o += 1
            if counter_o > 1:
                current_result += letter
        elif letter == "n":
            counter_n += 1
            if counter_n > 1:
                current_result += letter
        else:
            current_result += letter
        if counter_o >= 1 and counter_c >= 1 and counter_n >= 1:
            final_result += current_result + " "
            current_result = ""
            counter_c = 0
            counter_n = 0
            counter_o = 0
    letter = input()
print(final_result)