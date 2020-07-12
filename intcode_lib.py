# Day 2
# Day 5
# Day 7
# Day 9

class Intcode:

    def __init__(self, program, user_input=None, phase_setting=None, day_7=False):
        self.ptr = 0
        self.memory = program
        self.user_input = int(user_input) if user_input != None else None
        self.phase_setting = int(phase_setting) if phase_setting != None else None
        self.day_7 = day_7 # Special exit instructions for opcode 4 + 99
        self.relative_base = 0

    # DEFINITIONS:
    # Program = my puzzle input
    # Memory = list of integers, initialized from my puzzle input
    # Instruction pointer = address of the current instruction
    # Position = 0/1/2/3 relative to the pointer, aka relative index
    # Address = a position in memory, aka index
    # Instruction = an opcode followed by respective no. of parameters
    # Opcode = first integer of an instruction
    # Parameters = subsequent integers of an instruction

    # PARAMETER MODES:
    # 0 = position = causes the parameter to be interpreted as a position
    # 1 = immediate = causes the parameter to be interpreted as the input
    # 2 = relative = the parameter is interpreted as a position.
    #  The address a relative mode parameter refers to is itself plus the 
    #  current relative base.

    def advance_ptr(self):
        """Advances the pointer."""
        self.ptr += 1
        return self.ptr

    def get_instruction(self):
        """Returns the instruction, at the current location of the pointer."""
        instruction = str(self.memory[self.ptr]).zfill(5)
        return instruction

    def get_opcode(self, instruction):
        """Returns the opcode of an instruction, in int type."""
        return int(instruction[-2:])

    def get_parameter_mode(self, instruction, order):
        """Returns the mode of the specified parameter."""
        if order == "first":
            return int(instruction[-3:-2])
        elif order == "second":
            return int(instruction[-4:-3])
        elif order == "third":
            return int(instruction[-5:-4])

    def get_next_parameter(self):
        """Uses the current pointer to return the integer at that index as a\
             parameter."""
        parameter = self.memory[self.ptr]
        self.advance_ptr()
        return parameter

    def validate_address(self, address):
        """Returns the value at the address, expanding the memory to include \
            that address if it does not yet exist."""
        try:
            # print(f'attempting to validate address at {address}')
            # print(f'current length {len(self.memory)}')
            self.memory[address]
        except IndexError:
            # print(f'expanding memory by {address + 1 - len(self.memory)}...')
            for _ in range(len(self.memory), address + 1):
                self.memory.append(0)
        return address

    def get_input(self, parameter, parameter_mode):
        """Returns an integer based on that parameter's mode."""
        if parameter_mode == 0:
            return self.memory[self.validate_address(parameter)]
        elif parameter_mode == 1:
            return parameter
        elif parameter_mode == 2:
            return self.memory[self.validate_address(self.relative_base + parameter)]

    def opcode_1(self, input_1, input_2, dest_address):
        """Opcode 1 returns the addition of two values"""
        return self.store(input_1 + input_2, dest_address)

    def opcode_2(self, input_1, input_2, dest_address):
        """Opcode 2 returns the multiplication of two values"""
        return self.store(input_1 * input_2, dest_address)

    def opcode_3(self, dest_address, parameter_mode):
        """Stores an input value at the given address. The input value \
            upon the first call will default to the phase_setting, if \
                a phase_setting is given. Then, the input value will \
                    be whatever actual input value was provided by the user."""
        # From the problem's instructions: Parameters that an instruction 
        # writes to will never be in immediate mode.
        if self.phase_setting != None:
            to_store = self.phase_setting
            self.phase_setting = None
        else:
            to_store = self.user_input

        # print(f'found... attempting {to_store} at {dest_address}')
        # print(f'len of memory is {len(self.memory)}')
        if parameter_mode == 0:
            dest_address = dest_address
        elif parameter_mode == 2:
            dest_address += self.relative_base
        # print(f'found... attempting {to_store} at {dest_address}')
        # print(f'len of memory is {len(self.memory)}')
        return self.store(to_store, dest_address)

    def store(self, to_store, dest_address):
        """Stores a value at a given address."""
        self.memory[self.validate_address(dest_address)] = to_store
        return to_store

    def output(self, source_address, parameter_mode):
        """Returns the value at a given address in memory."""
        if parameter_mode == 0:
            output = self.memory[self.validate_address(source_address)]
        elif parameter_mode == 1:
            output = source_address
        elif parameter_mode == 2:
            print(f'source address {source_address}')
            print(self.relative_base)
            output = self.memory[self.validate_address(self.relative_base + source_address)]
        return f'Output is {output}'

    def opcode_5(self, input_1, input_2):
        """Jump if true. If the first parameter is non-zero, it sets the \
            instruction pointer to the value from the second parameter. \
                Otherwise, it does nothing."""
        if input_1 != 0:
            self.ptr = input_2
        return self.ptr

    def opcode_6(self, input_1, input_2):
        """Jump if false. If the first parameter is zero, it sets the \
            instruction pointer to the value from the second parameter. \
                Otherwise, it does nothing."""
        if input_1 == 0:
            self.ptr = input_2
        return self.ptr

    def opcode_7(self, input_1, input_2, dest_address):
        """Less than. If the first parameter is less than the second \
            parameter, it stores 1 in the position given by the third \
                parameter. Otherwise, it stores 0."""
        self.memory[self.validate_address(dest_address)] = 1 if input_1 < input_2 else 0
        return self.memory[dest_address]

    def opcode_8(self, input_1, input_2, dest_address):
        """Equals. If the first parameter is equal to the second \
            parameter, it stores 1 in the position given by the third \
                parameter. Otherwise, it stores 0."""
        self.memory[self.validate_address(dest_address)] = 1 if input_1 == input_2 else 0
        return self.memory[dest_address]
    
    def opcode_9(self, input_1, parameter_mode):
        """Adjusts the relative base by the input given."""
        if parameter_mode == 0:
            increment = self.memory[input_1]
        elif parameter_mode == 1:
            increment = input_1
        elif parameter_mode == 2:
            increment = self.memory[self.relative_base + input_1]

        self.relative_base += increment
        return self.relative_base

    def run(self):
        while True:
            instruction = self.get_instruction()
            opcode = self.get_opcode(instruction)
            first_parameter_mode = self.get_parameter_mode(instruction, "first")
            second_parameter_mode = self.get_parameter_mode(instruction, "second")
            third_parameter_mode = self.get_parameter_mode(instruction, "third")


            # print(f'relative base is {self.relative_base}')
            # if instruction == "00203":
            #     print('found me')
            #     print(f'rel base {self.relative_base}')
            #     print(f'ptr {self.ptr}')
            #     print(f'next in list: {self.memory[self.ptr + 1]}')

            if opcode == 99:
                if self.day_7:
                    return "HALT"
                else:
                    return self.memory[0]
            else:
                self.advance_ptr()
        
            # Get the inputs
            if opcode in [1, 2, 5, 6, 7, 8]:
                input_1 = self.get_input(self.get_next_parameter(), \
                    first_parameter_mode)
                input_2 = self.get_input(self.get_next_parameter(), \
                    second_parameter_mode)
            if opcode in [3]:
                dest_address = self.get_next_parameter()
                # print(f'first param mode {first_parameter_mode}')
                # print(f'rel base {self.relative_base}')
                # print(f'dest {dest_address}')
            if opcode in [1, 2, 7, 8]:
                dest_address = self.get_next_parameter()
                if third_parameter_mode == 0:
                    dest_address = dest_address
                elif third_parameter_mode == 2:
                    dest_address += self.relative_base
                # dest_address = self.get_input(self.get_next_parameter(), \
                #     third_parameter_mode)
            if opcode in [4]:
                source_address = self.get_next_parameter()
            if opcode in [9]:
                input_1 = self.get_next_parameter()

            # Feed the inputs to the opcode executor
            if opcode == 1:
                self.opcode_1(input_1, input_2, dest_address)
            elif opcode == 2:
                self.opcode_2(input_1, input_2, dest_address)
            elif opcode == 3:
                self.opcode_3(dest_address, first_parameter_mode)
                # print(f'at address 2009 is {self.memory[2009]}')
            elif opcode == 4:
                if self.day_7:
                    return self.memory[source_address]
                else:
                    print(self.output(source_address, first_parameter_mode))
            elif opcode == 5:
                self.opcode_5(input_1, input_2)
            elif opcode == 6:
                self.opcode_6(input_1, input_2)
            elif opcode == 7:
                self.opcode_7(input_1, input_2, dest_address)
            elif opcode == 8:
                self.opcode_8(input_1, input_2, dest_address)
            elif opcode == 9:
                self.opcode_9(input_1, first_parameter_mode)
        
