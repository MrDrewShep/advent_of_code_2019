# PART ONE
# To do this, before running the program, replace position 1 with the value 12
#  and replace position 2 with the value 2. What value is left at position 0 
# after the program halts?

# Bring puzzle input into a list
# Build intcode() in a library

import sys
sys.path.append('C:\\Users\\Drew\'s Laptop\\OneDrive\\workspace\\advent_of_code\\2019_2')
from intcode_lib import Intcode

def get_program():
    with open("data.txt") as f:
        program = f.read().split(',')
        return [int(i) for i in program]

program = get_program()
program[1] = 12
program[2] = 2

intcode = Intcode(program)

print(f'Answer: At address 0 is the integer {intcode.run()}')

# PART TWO
# Find the input noun and verb that cause the program to produce the output 
# 19690720. What is 100 * noun + verb?

for noun in range(0, 100):
    for verb in range(0, 100):
        program = get_program()
        program[1] = noun
        program[2] = verb
        intcode = Intcode(program)
        
        if intcode.run() == 19690720:
            print(f'noun {noun} verb {verb}: {100 * noun + verb}')
