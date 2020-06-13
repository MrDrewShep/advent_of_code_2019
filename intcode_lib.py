
class Intcode:

    def __init__(self, program):
        self.ptr = 0
        self.memory = program

    def advance(self, steps):
        """Advances the pointer"""
        self.ptr += steps

    def get_opcode(self):
        """Returns the opcode, where the pointer is currently pointing"""
        return self.memory[self.ptr]

    def get_address(self, increment=0):
        return self.memory[self.ptr + increment]

    def get_value(self, address, increment=0):
        return self.memory[address + increment]

    def add(self, param_1, param_2):
        """Opcode 1 returns the addition of two values"""
        return param_1 + param_2

    def multiply(self, param_1, param_2):
        """Opcode 2 returns the multiplication of two values"""
        return param_1 * param_2

    def store(self, value, address):
        """Stores a value at the address given"""
        self.memory[address] = value

    def run(self):
        while True:
            opcode = self.get_opcode()

            param_1 = self.get_value(self.get_address(1))
            param_2 = self.get_value(self.get_address(2))
            
            if opcode == 1:
                output = self.add(param_1, param_2)
                advance = 4
            elif opcode == 2:
                output = self.multiply(param_1, param_2)
                advance = 4
            elif opcode == 99:
                return self.get_value(0)
        
            self.store(output, self.get_address(3))
            self.advance(advance)
