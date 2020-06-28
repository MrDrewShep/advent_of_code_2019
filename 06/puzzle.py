# PART ONE
# What is the total number of direct and indirect orbits in your map data?

# PART TWO
# What is the minimum number of orbital transfers required to move from the
#  object YOU are orbiting to the object SAN is orbiting?

# TODO add docstrings

class Planet():

    def __init__(self, name, parent):
        self.name = name
        self.orbiting = parent

    def map_transfers_to(self, destination):
        my_map = []
        planet = self
        while planet.name != destination.name:
            my_map.append(planet.orbiting)
            planet = planet.orbiting
        return my_map

class Galaxy():

    def __init__(self, data):
        self.com = None
        self.data = data
        self.planets = []
        self.load_galaxy(3)

    def remove_pair_from_data(self, pair):
        self.data.remove(pair)
        return pair            

    def add_planet(self, planet):
        self.planets.append(planet)
        return planet

    def get_planet(self, planet_name):
        if self.com.name == planet_name:
            return self.com

        for planet in self.planets:
            if planet.name == planet_name:
                return planet
        return False

    def get_parent_name(self, pair, delimeter):
        return pair[:delimeter]

    def get_new_planet_name(self, pair, delimiter):
        return pair[delimiter + 1:]

    def add_new_pair(self, new_pair):
        delimeter = 3
        parent_name = self.get_parent_name(new_pair, delimeter)
        parent = self.get_planet(parent_name)
        new_planet_name = self.get_new_planet_name(new_pair, delimeter)
        new_planet = Planet(new_planet_name, parent)
        return self.add_planet(new_planet)

    def find_com_index(self, delimeter):
        all_children = [self.get_new_planet_name(i, delimeter) for i in self.data]
        index = 0
        for pair in self.data:
            parent_name = self.get_parent_name(pair, delimeter)
            if parent_name not in all_children:
                return index
            index += 1

    def load_com(self, com_index, delimeter):
        first_pair = self.data[com_index]
        com_name = self.get_parent_name(first_pair, delimeter)
        com = Planet(com_name, None)
        self.com = com
        self.add_planet(com)
        return com

    def load_galaxy(self, delimeter):
        self.load_com(self.find_com_index(delimeter), delimeter)

        while len(self.data) > 0:
            for pair in self.data:
                if self.get_planet(self.get_parent_name(pair, delimeter)):
                    self.add_new_pair(pair)
                    self.remove_pair_from_data(pair)
        return len(self.planets)

    def calc_total_orbits(self):
        counter = 0
        for planet in self.planets:
            counter += len(planet.map_transfers_to(self.com))
        return counter

    def find_transfers_btwn(self, origin_str, destination_str):
        origin = self.get_planet(origin_str)
        destination = self.get_planet(destination_str)

        origin_map = origin.map_transfers_to(self.com)
        destination_map = destination.map_transfers_to(self.com)

        for i in origin_map:
            if i in destination_map:
                return len(origin.map_transfers_to(i)) + \
                    len(destination.map_transfers_to(i)) - 2

with open("data.txt", "r") as f:
    data = f.readlines()
    data = [i.strip("\n") for i in data]

galaxy = Galaxy(data)
print(galaxy.calc_total_orbits())
print(galaxy.find_transfers_btwn("YOU", "SAN"))
