# PART ONE
# How many different passwords within the range given in your puzzle input
#  meet these criteria?
# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase
#  or stay the same (like 111123 or 135679).

first = 197487
last = 673251


def check_increasing(num):
    return all(int(num[i]) <= int(num[i + 1]) for i in range(len(num) - 1))

def check_adjacent(num):
    return any(int(num[i]) == int(num[i + 1]) for i in range(len(num) - 1))

def check_adjacent_part_2(num): # got 99 problems and this function is oneofem
    if not check_adjacent(num):
        return False
        
    j = 0
    for index in range(len(num) - 1):
        if num[i] == num[i + 1]:
            j += 1


    for index in range(len(num) - 2):
        if index == 0:
            if num[index] == num[index + 1] and \
                num[index] != num[index + 2]:
                return True
        elif index == (len(num) - 1):
            if num[index] == num:
                pass
        if num[index] == num[index + 1]:
            try:
                if num[index] != num[index + 2]:
                    return True
                else:
                    continue
            except:
                return True
    return False

qualifying = 0
for num in range(first, last + 1):
    num = str(num)
    if check_increasing(num) and check_adjacent(num):
        qualifying += 1

print(f'{qualifying} numbers qualify')


# PART TWO

qualifying = 0
for num in range(first, last + 1):
    num = str(num)
    if check_increasing(num) and check_adjacent_part_2(num):
        qualifying += 1

print(f'{qualifying} numbers qualify in part two')
