# PART ONE
# What is the sum of the fuel requirements for all of the modules on your 
# spacecraft?

with open("data.txt") as f:
    data = f.readlines()
    data = [i.strip("\n") for i in data]

def calc_fuel(module_mass):
    """Takes in mass of a module and returns the amount of fuel required 
    to launch it"""
    return (int(module_mass) // 3) -2

total_fuel = 0
for module in data:
    total_fuel += calc_fuel(module)

print(total_fuel)

#PART TWO
# What is the sum of the fuel requirements for all of the modules on your 
# spacecraft when also taking into account the mass of the added fuel?

def calc_fuel_2(module_mass):
    """Takes in the mass of a module and returns a recursively derrived 
    amount of fuel required to launch it, and launch the fuel itself"""
    fuel_req = (int(module_mass) // 3) - 2
    if fuel_req < 0:
        return 0
    return fuel_req + calc_fuel_2(fuel_req)

total_fuel = 0
for module in data:
    total_fuel += calc_fuel_2(module)

print(total_fuel)
