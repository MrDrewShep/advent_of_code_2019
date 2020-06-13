# PART ONE
# What is the Manhattan distance from the central port to the closest 
# intersection?

# Bring in both datasets
# Assign a set to each wire, of unique x,y coords that wire travels
# Iterate through datasets, filling in the sets
# Find common x,y coords between sets
# Find common coord with the least manhattan distance

class Panel:

    def __init__(self):
        self.wires = []
        self.intersections = set()

    def add_wire(self, wire):
        self.wires.append(wire)

    def trace_wires(self):
        for wire in self.wires:
            wire.trace_wire()

    def find_intersections(self):
        self.trace_wires()

        self.intersections = set(i for i in self.wires[0].coords \
             if i in self.wires[1].coords)

    def find_closest_intersection(self):
        self.find_intersections()

        closest = min(abs(x) + abs(y) for x, y in self.intersections)
        total = len(self.intersections)
        return f'Closest intersection to the central port is {closest} '\
            f'manhattan steps. {total} total intersections.'

    def find_intersection_with_fewest_combined_steps(self):
        self.trace_wires()

        combined_intersections = {}
        for k, v in self.wires[0].intersections.items():
            combined_intersections[k] = v + self.wires[1].intersections[k]
        return min(combined_intersections.values())


class Wire:

    def __init__(self, wire_path, panel):
        self.x = 0
        self.y = 0
        self.coords = set()
        self.wire_path = wire_path
        self.total_steps = 0
        self.panel = panel
        self.intersections = {}
        panel.add_wire(self)

    def move_u(self):
        self.y += 1
        self.coords.add((self.x, self.y))

    def move_d(self):
        self.y -= 1
        self.coords.add((self.x, self.y))

    def move_r(self):
        self.x += 1
        self.coords.add((self.x, self.y))

    def move_l(self):
        self.x -= 1
        self.coords.add((self.x, self.y))

    def trace_wire(self):
        self.x = 0
        self.y = 0
        self.total_steps = 0

        for segment in self.wire_path:
            direction = segment[:1]
            steps = int(segment[1:])

            for _ in range(steps):
                self.total_steps += 1
                if direction == 'U':
                    self.move_u()
                elif direction == 'D':
                    self.move_d()
                elif direction == 'R':
                    self.move_r()
                elif direction == 'L':
                    self.move_l()
                
                if (self.x, self.y) in self.panel.intersections and \
                    (self.x, self.y) not in self.intersections:
                    self.intersections[(self.x, self.y)] = self.total_steps

with open("data.txt") as f:
    wire_1_path = list(f.read().split(','))

with open("data2.txt") as f:
    wire_2_path = list(f.read().split(','))

panel_1 = Panel()
wire_1 = Wire(wire_1_path, panel_1)
wire_2 = Wire(wire_2_path, panel_1)
print(panel_1.find_closest_intersection())

print(panel_1.find_intersection_with_fewest_combined_steps())

# PART TWO
# What is the fewest combined steps the wires must take to reach an 
# intersection?

# Added to Panel(), find_intersection_with_fewest_combined_steps()