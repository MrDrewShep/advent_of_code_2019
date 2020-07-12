import sys
sys.path.append('C:\\Users\\Drew\'s Laptop\\OneDrive\\workspace\\advent_of_code\\2019_2')
from intcode_lib import Intcode

def get_software():
    with open('data.txt', 'r') as f:
        data = f.read().split(',')
    data = [int(i) for i in data]
    return data

selection = input("Input value > ")
intcode = Intcode(get_software(), selection)

print(intcode.run())