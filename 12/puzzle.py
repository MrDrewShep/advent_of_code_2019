# PART ONE
# What is the total energy in the system after simulating the moons given 
# in your scan for 1000 steps?

from pprint import pprint

def get_data():
    with open("test_data2.txt", "r") as f:
        data = f.readlines()
        data = [i.strip("\n") for i in data]
        return data

class Jupiter():

    def __init__(self, moons):
        self.moons = moons
        self.states = set()

    def __repr__(self):
        return f'{moon.pos for moon in self.moons}'

    def moons_apply_gravity(self):
        for moon in self.moons:
            moon.apply_gravity(self.moons)

    def moons_apply_velocity(self):
        for moon in self.moons:
            moon.apply_velocity()

    def steps(self, steps):
        for _ in range(steps):
            self.moons_apply_gravity()
            self.moons_apply_velocity()

    def get_total_energy(self):
        return sum([i.calc_total_energy() for i in self.moons])

    def part_one(self):
        self.steps(1000)
        print(self.get_total_energy())

    def part_two(self): #TODO figure out how to make this efficient
        counter = 0
        while True:
        # while state not in self.states:
            self.moons_apply_gravity()
            self.moons_apply_velocity()
            state = (
                self.moons[0].pos["x"],
                self.moons[0].pos["y"],
                self.moons[0].pos["z"],
                self.moons[0].vel["x"],
                self.moons[0].vel["y"],
                self.moons[0].vel["z"],
                self.moons[1].pos["x"],
                self.moons[1].pos["y"],
                self.moons[1].pos["z"],
                self.moons[1].vel["x"],
                self.moons[1].vel["y"],
                self.moons[1].vel["z"],
                self.moons[2].pos["x"],
                self.moons[2].pos["y"],
                self.moons[2].pos["z"],
                self.moons[2].vel["x"],
                self.moons[2].vel["y"],
                self.moons[2].vel["z"],
                self.moons[3].pos["x"],
                self.moons[3].pos["y"],
                self.moons[3].pos["z"],
                self.moons[3].vel["x"],
                self.moons[3].vel["y"],
                self.moons[3].vel["z"],
            )
            if state in self.states:
                print('breaking')
                break
            self.states.add(state)
            counter += 1
            if counter % 100000 == 0:
                print(counter)
        print(f'{counter} states until a duplicate')

class Moon():

    def __init__(self, x, y, z):
        self.pos = {
            "x" : x,
            "y" : y,
            "z" : z
        }

        self.vel = {
            "x" : 0,
            "y" : 0,
            "z" : 0
        }

    def __repr__(self):
        return f'{self.pos.items()} {self.vel.items()}'

    def apply_gravity(self, moons):
        for k, v in self.pos.items():
            delta = 0
            for moon in moons:
                if moon == self:
                    continue
                
                if v > moon.pos[k]:
                    delta -= 1
                elif v < moon.pos[k]:
                    delta += 1

            self.vel[k] += delta

    def apply_velocity(self):
        for k, v in self.vel.items():
            self.pos[k] += v

    def calc_pot_energy(self):
        return sum([abs(i) for i in self.pos.values()])

    def calc_kin_energy(self):
        return sum([abs(i) for i in self.vel.values()])

    def calc_total_energy(self):
        return self.calc_pot_energy() * self.calc_kin_energy()


moons = []
for coords in get_data():
    x_start = coords.find("x=") + 2
    x_stop = coords.find(", y")
    x = int(coords[x_start:x_stop])

    y_start = coords.find("y=") + 2
    y_stop = coords.find(", z")
    y = int(coords[y_start:y_stop])

    z_start = coords.find("z=") + 2
    z_stop = coords.find(">")
    z = int(coords[z_start:z_stop])

    moons.append(Moon(x, y, z))

jupiter = Jupiter(moons)

jupiter.part_one()
jupiter.part_two()