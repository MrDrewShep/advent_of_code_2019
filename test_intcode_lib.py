import intcode_lib

def get_software():
    with open("05/data.txt") as f:
        program = f.read().split(',')
        program = [int(i) for i in program]
    return program

def initialize_intcode():
    program = get_software()
    intcode = intcode_lib.Intcode(program)
    return intcode

def test_init():
    intcode = intcode_lib.Intcode(get_software())
    assert intcode.phase_setting == None
    assert intcode.user_input == None
    intcode = intcode_lib.Intcode(get_software(), 1)
    assert intcode.phase_setting == None
    assert intcode.user_input == 1
    intcode = intcode_lib.Intcode(get_software(), 1, 2)
    assert intcode.phase_setting == 2
    assert intcode.user_input == 1
    intcode = intcode_lib.Intcode(get_software(), 0, 0)
    assert intcode.phase_setting == 0
    assert intcode.user_input == 0

def test_advance_ptr():
    intcode = initialize_intcode()
    assert intcode.ptr == 0
    assert intcode.advance_ptr() == 1

def test_get_instruction():
    intcode = initialize_intcode()
    assert intcode.get_instruction() == "00003"
    intcode.ptr = 6
    assert intcode.get_instruction() == "01100"
    intcode.ptr = 12
    assert intcode.get_instruction() == "01101"

def test_get_opcode():
    intcode = initialize_intcode()
    result = intcode.get_opcode("01101")
    assert result == 1
    assert type(result) == int
    assert result not in ["1", "01"]

def test_get_parameter_mode():
    intcode = initialize_intcode()
    result = intcode.get_parameter_mode("01001", "first")
    assert result == 0
    assert type(result) == int
    result = intcode.get_parameter_mode("01001", "second")
    assert result == 1
    assert type(result) == int

def test_get_next_parameter():
    intcode = initialize_intcode()
    intcode.advance_ptr()
    assert intcode.ptr == 1
    result = intcode.get_next_parameter()
    assert intcode.ptr == 2
    assert result == 225
    assert type(result) == int

def test_get_input():
    intcode = initialize_intcode()
    result = intcode.get_input(6, 0)
    assert result == 1100
    assert type(result) == int
    result = intcode.get_input(6, 1)
    assert result == 6
    assert type(result) == int

def test_opcode_1():
    intcode = initialize_intcode()
    assert intcode.opcode_1(5, 12, 30) == 17
    assert intcode.memory[30] == 17
    assert intcode.opcode_1(11, 3, 30) == 14
    assert intcode.memory[30] == 14

def test_opcode_2():
    intcode = initialize_intcode()
    assert intcode.opcode_2(5, 12, 30) == 60
    assert intcode.memory[30] == 60
    assert intcode.opcode_2(11, 3, 30) == 33
    assert intcode.memory[30] == 33

def test_opcode_3():
    intcode = initialize_intcode()
    assert intcode.user_input == None
    assert intcode.phase_setting == None
    intcode.user_input = 141
    assert intcode.user_input == 141
    assert intcode.opcode_3(20) == 141
    intcode.phase_setting = 3
    assert intcode.phase_setting == 3
    assert intcode.opcode_3(20) == 3
    assert intcode.opcode_3(20) == 141
    assert intcode.opcode_3(20) == 141

def test_store():
    intcode = initialize_intcode()
    assert intcode.store(5, 12) == 5
    assert intcode.memory[12] == 5
    assert intcode.store(91, 12) == 91
    assert intcode.memory[12] == 91

def test_opcode_5():
    intcode = initialize_intcode()
    intcode.ptr = 0
    assert intcode.opcode_5(1, 14) == 14
    assert intcode.ptr == 14
    intcode.ptr = 2
    assert intcode.opcode_5(0, 14) == 2
    assert intcode.ptr == 2

def test_opcode_6():
    intcode = initialize_intcode()
    intcode.ptr = 0
    assert intcode.opcode_6(1, 14) == 0
    assert intcode.ptr == 0
    intcode.ptr = 2
    assert intcode.opcode_6(0, 14) == 14
    assert intcode.ptr == 14

def test_opcode_7():
    intcode = initialize_intcode()
    intcode.memory[10] = 999
    assert intcode.opcode_7(5, 6, 10) == 1
    assert intcode.memory[10] == 1
    intcode.memory[10] = 999
    assert intcode.opcode_7(5, 4, 10) == 0
    assert intcode.memory[10] == 0

def test_opcode_8():
    intcode = initialize_intcode()
    intcode.memory[10] = 999
    assert intcode.opcode_8(5, 5, 10) == 1
    assert intcode.memory[10] == 1
    intcode.memory[10] = 999
    assert intcode.opcode_8(5, 4, 10) == 0
    assert intcode.memory[10] == 0