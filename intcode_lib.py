
class Intcode:

    def __init__(self, program, user_input=None):
        self.ptr = 0
        self.memory = program
        self.user_input = user_input

    # DEFINITIONS:
    # Program = my puzzle input
    # Memory = list of integers, initialized from my puzzle input
    # Instruction pointer = address of the current instruction
    # Position = 0/1/2/3 relative to the pointer, aka relative index
    # Address = a position in memory, aka index
    # Instruction = an opcode followed by respective no. of parameters
    # Opcode = first integer of an instruction
    # Parameters = subsequent integers of an instruction

    def advance_ptr(self):
        """Advances the pointer"""
        self.ptr += 1
        return self.ptr

    def get_instruction(self):
        """Returns the instruction, at the current location of the pointer"""
        instruction = str(self.memory[self.ptr]).zfill(5)
        return instruction

    def get_opcode(self, instruction):
        """Returns the opcode of an instruction, in int format"""
        return int(instruction[-2:])

    def get_parameter(self):
        """Returns the parameter which is 'position' integers after the 
        opcode"""
        parameter = self.memory[self.ptr]
        self.advance_ptr()
        return parameter

    def get_input(self, parameter):
        """Returns the integer at a given position/address"""
        return self.memory[parameter]

    def opcode_1(self, input_1, input_2, dest_address):
        """Opcode 1 returns the addition of two values"""
        return self.store(input_1 + input_2, dest_address)

    def opcode_2(self, input_1, input_2, dest_address):
        """Opcode 2 returns the multiplication of two values"""
        return self.store(input_1 * input_2, dest_address)

    def store(self, to_store, dest_address):
        """Stores a value at a given address. Also used for opcode 3."""
        self.memory[dest_address] = to_store
        return to_store

    # def output(self):
    #     address = self.get_input(self.get_parameter())
    #     return f'The integer at address {address} is {self.memory[address]}'

    # PARAMETER MODES:
    # 0 = position = causes the parameter to be interpreted as a position
    # 1 = immediate = causes the parameter to be interpreted as the input

    def run(self):
        while True:
            instruction = self.get_instruction()
            opcode = self.get_opcode(instruction)

            if opcode == 99:
                return self.get_input(0)
            else:
                self.advance_ptr()
        
            if opcode in [1, 2]:
                input_1 = self.get_input(self.get_parameter())
                input_2 = self.get_input(self.get_parameter())
                dest_address = self.get_parameter()

            if opcode == 1:
                self.opcode_1(input_1, input_2, dest_address)
            elif opcode == 2:
                self.opcode_2(input_1, input_2, dest_address)
            # elif opcode == 3:
            #     self.store(self.user_input)
            # elif opcode == 4:
            #     print(self.output())
        
