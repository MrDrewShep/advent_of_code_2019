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
    consecutive = 1
    last = None
    for i in range(len(num)):
        if num[i] == last:
            consecutive += 1
            if i == (len(num) - 1) and consecutive == 2:
                return True
        else:
            if consecutive == 2:
                return True
            last = num[i]
            consecutive = 1

    return False

qualifying = 0
for num in range(first, last + 1):
    num = str(num)
    if check_increasing(num) and check_adjacent(num):
        qualifying += 1

print(f'{qualifying} numbers qualify in part one')


# PART TWO

qualifying = 0
for num in range(first, last + 1):
    num = str(num)
    if check_increasing(num) and check_adjacent_part_2(num):
        qualifying += 1

print(f'{qualifying} numbers qualify in part two')
