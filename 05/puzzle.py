# PART ONE
# Add opcodes 3 & 4, as well as parameter modes 0 & 1

import sys
sys.path.append('C:\\Users\\Drew\'s Laptop\\OneDrive\\workspace\\advent_of_code\\2019_2')
from intcode_lib import Intcode

def get_program():
    with open("data.txt") as f:
        program = f.read().split(',')
        return [int(i) for i in program]

program = get_program()
user_input = input("What is the ID of the system you want to run? ")
intcode = Intcode(program, user_input)
intcode.run()

# PART TWO
# Add opcodes 5 - 8, also with support for parameter modes