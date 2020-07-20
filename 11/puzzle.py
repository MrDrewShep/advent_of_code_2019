# PART ONE
# How many panels does it paint at least once?
# Intcode Robot first output
#    0 = paint panel black
#    1 = paint panel white
# Intcode Robot second output
#    0 = turn left 90 degrees
#    1 = turn right 90 degrees
# Registration panel colors
#    . = black
#    # = white

import sys
sys.path.append('C:\\Users\\Drew\'s Laptop\\OneDrive\\workspace\\advent_of_code\\2019_2')
from intcode_lib import Intcode
import numpy as np
from collections import deque
from pprint import pprint

def get_program():
    with open("data.txt") as f:
        program = f.read().split(',')
        return [int(i) for i in program]

class Robot():

    def __init__(self, registration):
        self.robot = Intcode(get_program(), user_input=0, day=11)
        self.facing = deque(["up", "right", "down", "left"])
        self.y = 2
        self.x = 2
        self.registration = registration

    def detect_user_input(self):
        return self.registration.get_panel_color(self.y, self.x)

    def paint_panel(self, color):
        return self.registration.update_panel_color(color)

    def move(self, turn):
        if turn == 0:
            self.facing.rotate(1)
        elif turn == 1:
            self.facing.rotate(-1)

        if self.facing[0] == "up":
            if self.y == 0:
                self.registration.new_row_top()
                self.y += 1
            self.y -= 1
        elif self.facing[0] == "right":
            if self.x == self.registration.grid.shape[1] - 1:
                self.registration.new_col_right()
            self.x += 1
        elif self.facing[0] == "down":
            if self.y == self.registration.grid.shape[0] - 1:
                self.registration.new_row_bottom()
            self.y += 1
        elif self.facing[0] == "left":
            if self.x == 0:
                self.registration.new_col_left()
                self.x += 1
            self.x -= 1


    def run_intcode(self):
        for _ in range(9999):
            self.robot.update_user_input(self.detect_user_input())

            paint_color = self.robot.run()
            if paint_color == 'HALT':
                break
            turn = self.robot.run()

            self.registration.paint_panel(self.y, self.x, paint_color)
            self.move(turn)

            # print(paint_color, turn)
            # print(self.registration)

        return f'sum is: {self.registration.change_grid.sum()}'


class Registration():
    
    def __init__(self):
        self.grid = np.full((5,5), ".")
        self.change_grid = np.zeros((5,5), dtype='int8')

    def __repr__(self):
        return f'{self.grid}\n{self.change_grid}'

    def new_row_bottom(self):
        self.grid = np.vstack((self.grid, np.full(self.grid.shape[1], ".")))
        self.change_grid = np.vstack((self.change_grid, np.full(self.change_grid.shape[1], 0)))

    def new_row_top(self):
        self.grid = np.vstack((np.full(self.grid.shape[1], "."), self.grid))
        self.change_grid = np.vstack((np.full(self.change_grid.shape[1], 0), self.change_grid))

    def new_col_right(self):
        self.grid = np.hstack((self.grid, np.full(self.grid.shape[0], ".").reshape(self.grid.shape[0], 1)))
        self.change_grid = np.hstack((self.change_grid, np.full(self.change_grid.shape[0], 0).reshape(self.change_grid.shape[0], 1)))

    def new_col_left(self):
        self.grid = np.hstack((np.full(self.grid.shape[0], ".").reshape(self.grid.shape[0], 1), self.grid))
        self.change_grid = np.hstack((np.full(self.change_grid.shape[0], 0).reshape(self.change_grid.shape[0], 1), self.change_grid))

    def get_panel_color(self, y, x):
        panel = self.grid[y,x]
        if panel == ".":
            return 0
        elif panel == "#":
            return 1
    
    def paint_panel(self, y, x, paint_color):
        if paint_color == 0:
            output = "."
        elif paint_color == 1:
            output = "#"

        self.grid[y,x] = output
        self.change_grid[y,x] = 1
        return paint_color

registration = Registration()
robot = Robot(registration)
print(robot.run_intcode())

# PART TWO
# a valid registration identifier is always eight capital letters. 
# After starting the robot on a single white panel instead, what registration 
# identifier does it paint on your hull?

registration = Registration()
registration.paint_panel(2, 2, 1)
robot = Robot(registration)
robot.run_intcode()
x = registration.grid.shape[1]
y = registration.grid.shape[0]
display = str()
for row in range(y):
    for col in range(x):
        display += registration.grid[row,col]
    display += "\n"
print(display)
