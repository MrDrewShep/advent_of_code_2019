# PART ONE
# Find the best location for a new monitoring station. How many other
#  asteroids can be detected from that location?

# x values rise from left to right
# y values rise from top to bottom, unlike traditional algebra
#                   |
#          (3,0) i  |    b (6,0)
#                   |
#      (2,2) h      |         c (8,2)   
# ------------------a (5,3)--------------
#      (2,4) g      |         d (8,4)
#                   |
#       (3,6)  f    |    e (6,6)
#                   |
#                           Clockwise the slope is
# a b = -3   = (0-3)/(6-5)  
# a c = -1/3 = (2-3)/(8-5)  Ascending
# a d =  1/3 = (4-3)/(8-5)
# a e =  3   = (6-3)/(6-5)  Ascending
# a f = -3/2 = (6-3)/(3-5)
# a g = -1/3 = (4-3)/(2-5)  Ascending
# a h =  1/3 = (2-3)/(2-5)
# a i =  3/2 = (0-3)/(3-5)  Ascending
#

import math
from operator import itemgetter
from itertools import groupby
from pprint import pprint

def get_input():
    with open("data.txt", "r") as f:
        data = f.read().split("\n")
    return data

class Galaxy():

    def __init__(self):
        self.asteroids = []
        self.highvis_asteroid = None

    def add_asteroid(self, asteroid):
        self.asteroids.append(asteroid)

    def load_galaxy(self, data):
        y = 0
        for row in data:
            x = 0
            for cell in row:
                if cell == "#":
                    self.add_asteroid(Asteroid(x, y, self))
                x += 1
            y += 1

    def asteroids_detect_each_other(self):
        for asteroid in self.asteroids:
            asteroid.detect_asteroids()

    def find_best_loc_for_monitoring_station(self):
        self.asteroids_detect_each_other()
        most = 0
        ast_w_most = None
        for asteroid in self.asteroids:
            if len(asteroid.visibility) > most:
                most = len(asteroid.visibility)
                ast_w_most = asteroid
        self.highvis_asteroid = ast_w_most
        return f'Asteroid at {ast_w_most.x}, {ast_w_most.y} detects {most} other asteroids'
        # return f'{max([(len(i.visibility)) for i in self.asteroids])}' \
        #     f' are the most asteroids visible from one place.'


class Asteroid():

    def __init__(self, x, y, galaxy):
        self.x = x
        self.y = y
        self.visibility = set()
        self.map = []
        self.galaxy = galaxy

    def check_zero_division(self, other_ast):
        if other_ast.x == self.x:
            if other_ast.y < self.y:
                return "up"
            else:
                return "down"

    def find_direction(self, other_ast):
        if other_ast.y < self.y:
            return "above"
        else:
            return "below"

    def get_slope(self, other_ast):
        if other_ast.y == self.y:
            if other_ast.x > self.x:
                slope = 0
                direction = "right"
            else:
                slope = 0
                direction = "left"
        else:
            try:
                slope = (other_ast.y - self.y) / (other_ast.x - self.x)
                direction = self.find_direction(other_ast)
            except ZeroDivisionError:
                slope = None
                direction = self.check_zero_division(other_ast)

        return (slope, direction)

    def get_distance(self, other_ast):
        y_delta = abs(other_ast.y - self.y)
        x_delta = abs(other_ast.x - self.x)
        distance = math.sqrt((y_delta**2) + (x_delta**2))
        return distance

    def detect_asteroids(self):
        for other_ast in self.galaxy.asteroids:
            if other_ast == self:
                continue
            slope, direction = self.get_slope(other_ast)
            distance = self.get_distance(other_ast)
            self.visibility.add((slope, direction))
            self.map.append((other_ast, slope, direction, distance))
        return len(self.visibility)

    def filter_N(self, map_item):
        return map_item[2] == "up"

    def filter_NE(self, map_item):
        return map_item[2] == "above" and map_item[1] < 0

    def filter_E(self, map_item):
        return map_item[2] == "left"

    def filter_SE(self, map_item):
        return map_item[2] == "below" and map_item[1] > 0

    def filter_S(self, map_item):
        return map_item[2] == "down"

    def filter_SW(self, map_item):
        return map_item[2] == "below" and map_item[1] < 0

    def filter_W(self, map_item):
        return map_item[2] == "left"

    def filter_NW(self, map_item):
        return map_item[2] == "above" and map_item[1] > 0

    def sort_groupby_and_dictify(self, iter):
        a = sorted(iter, key=itemgetter(1,3))
        b = groupby(a, key=itemgetter(1))
        result = dict()
        for key, group in b:
            result[key] = list(group)
        return result

    def find_200th(self):
        N = self.sort_groupby_and_dictify(filter(self.filter_N, self.map))
        NE = self.sort_groupby_and_dictify(filter(self.filter_NE, self.map))
        E = self.sort_groupby_and_dictify(filter(self.filter_E, self.map))
        SE = self.sort_groupby_and_dictify(filter(self.filter_SE, self.map))
        S = self.sort_groupby_and_dictify(filter(self.filter_S, self.map))
        SW = self.sort_groupby_and_dictify(filter(self.filter_SW, self.map))
        W = self.sort_groupby_and_dictify(filter(self.filter_W, self.map))
        NW = self.sort_groupby_and_dictify(filter(self.filter_NW, self.map))

        vaporized_count = 0
        while True:
            for quadrant in [N, NE, E, SE, S, SW, W, NW]:
                for line_of_sight in quadrant:
                    if len(quadrant[line_of_sight]) > 0:
                        vaporized = quadrant[line_of_sight].pop(0)
                        vaporized_count += 1
                    else:
                        continue
                    
                    if vaporized_count == 200:
                        return vaporized[0].x * 100 + vaporized[0].y
        
galaxy = Galaxy()
galaxy.load_galaxy(get_input())
print(galaxy.find_best_loc_for_monitoring_station())

# PART TWO
# The Elves are placing bets on which will be the 200th asteroid to be 
# vaporized. Win the bet by determining which asteroid that will be; what do
#  you get if you multiply its X coordinate by 100 and then add its Y
#  coordinate?

print(galaxy.highvis_asteroid.find_200th())