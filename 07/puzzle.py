# PART ONE
# What is the highest signal that can be sent to the thrusters?
# Incorporate phase_setting
# TODO find a better way to access intcode_lib from a level above

import itertools
import sys
sys.path.append('C:\\Users\\Drew\'s Laptop\\OneDrive\\workspace\\advent_of_code\\2019_2')
from intcode_lib import Intcode

def get_software():
    with open('data.txt', 'r') as f:
        data = f.read().split(',')
    data = [int(i) for i in data]
    return data

def part_one():
    phase_setting_permutations = [i for i in itertools.permutations(range(5))]
    largest_output = -9999999
    for perm in phase_setting_permutations:
        amplifier_a = Intcode(get_software(), 0, perm[0], True).run()
        amplifier_b = Intcode(get_software(), amplifier_a, perm[1], True).run()
        amplifier_c = Intcode(get_software(), amplifier_b, perm[2], True).run()
        amplifier_d = Intcode(get_software(), amplifier_c, perm[3], True).run()
        amplifier_e = Intcode(get_software(), amplifier_d, perm[4], True).run()

        if amplifier_e > largest_output:
            largest_output = amplifier_e

    return largest_output

print(part_one())


def part_two():
    phase_setting_permutations = [i for i in itertools.permutations(range(5, 10))]
    largest_output = -9999999
    for perm in phase_setting_permutations:
        amplifier_a = Intcode(get_software(), None, perm[0], True)
        amplifier_b = Intcode(get_software(), None, perm[1], True)
        amplifier_c = Intcode(get_software(), None, perm[2], True)
        amplifier_d = Intcode(get_software(), None, perm[3], True)
        amplifier_e = Intcode(get_software(), None, perm[4], True)
        a_input = 0
        while True:
            amplifier_a.user_input = a_input
            amplifier_b.user_input = amplifier_a.run()
            amplifier_c.user_input = amplifier_b.run()
            amplifier_d.user_input = amplifier_c.run()
            amplifier_e.user_input = amplifier_d.run()
            e_output = amplifier_e.run()
            if e_output == "HALT":
                break
            else:
                last_e_result = e_output
                a_input = e_output

        if last_e_result > largest_output:
            largest_output = last_e_result

    return largest_output

print(part_two())