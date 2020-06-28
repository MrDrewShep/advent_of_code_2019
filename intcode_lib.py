class Intcode:

    def __init__(self, program, user_input=None):
        self.ptr = 0
        self.memory = program
        if user_input:
            self.user_input = int(user_input)

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

    def get_parameter_mode(self, instruction, order):
        """Returns the mode of an instruction's given parameter"""
        if order == "first":
            return int(instruction[-3:-2])
        elif order == "second":
            return int(instruction[-4:-3])

    def get_next_parameter(self):
        """Uses the current pointer to return the integer at that index as a\
             parameter."""
        parameter = self.memory[self.ptr]
        self.advance_ptr()
        return parameter

    def get_input(self, parameter, parameter_mode):
        """Returns an integer based on that parameter's mode"""
        if parameter_mode == 0:
            return self.memory[parameter]
        elif parameter_mode == 1:
            return parameter

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

    def output(self, source_address):
        """Returns the value at a given address in memory."""
        return f'The integer at address {source_address} is' \
            f' {self.memory[source_address]}'

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
        self.memory[dest_address] = 1 if input_1 < input_2 else 0
        return self.memory[dest_address]

    def opcode_8(self, input_1, input_2, dest_address):
        """Equals. If the first parameter is equal to the second \
            parameter, it stores 1 in the position given by the third \
                parameter. Otherwise, it stores 0."""
        self.memory[dest_address] = 1 if input_1 == input_2 else 0
        return self.memory[dest_address]

    def run(self):
        while True:
            instruction = self.get_instruction()
            opcode = self.get_opcode(instruction)
            first_parameter_mode = self.get_parameter_mode(instruction, "first")
            second_parameter_mode = self.get_parameter_mode(instruction, "second")

            if opcode == 99:
                return self.memory[0]
            else:
                self.advance_ptr()
        
            if opcode in [1, 2, 5, 6, 7, 8]:
                input_1 = self.get_input(self.get_next_parameter(), \
                    first_parameter_mode)
                input_2 = self.get_input(self.get_next_parameter(), \
                    second_parameter_mode)
            if opcode in [1, 2, 3, 7, 8]:
                dest_address = self.get_next_parameter()
            if opcode in [4]:
                source_address = self.get_next_parameter()

            if opcode == 1:
                self.opcode_1(input_1, input_2, dest_address)
            elif opcode == 2:
                self.opcode_2(input_1, input_2, dest_address)
            elif opcode == 3:
                self.store(self.user_input, dest_address)
            elif opcode == 4:
                print(self.output(source_address))
            elif opcode == 5:
                self.opcode_5(input_1, input_2)
            elif opcode == 6:
                self.opcode_6(input_1, input_2)
            elif opcode == 7:
                self.opcode_7(input_1, input_2, dest_address)
            elif opcode == 8:
                self.opcode_8(input_1, input_2, dest_address)
        
