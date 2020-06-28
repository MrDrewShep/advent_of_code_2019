import intcode_lib

def initialize_program():
    with open("05/data.txt") as f:
        program = f.read().split(',')
        program = [int(i) for i in program]

    intcode = intcode_lib.Intcode(program)
    return intcode

def test_advance_ptr():
    intcode = initialize_program()
    assert intcode.ptr == 0
    assert intcode.advance_ptr() == 1

def test_get_instruction():
    intcode = initialize_program()
    assert intcode.get_instruction() == "00003"
    intcode.ptr = 6
    assert intcode.get_instruction() == "01100"
    intcode.ptr = 12
    assert intcode.get_instruction() == "01101"

def test_get_opcode():
    intcode = initialize_program()
    result = intcode.get_opcode("01101")
    assert result == 1
    assert type(result) == int
    assert result not in ["1", "01"]

def test_get_parameter_mode():
    intcode = initialize_program()
    result = intcode.get_parameter_mode("01001", "first")
    assert result == 0
    assert type(result) == int
    result = intcode.get_parameter_mode("01001", "second")
    assert result == 1
    assert type(result) == int

def test_get_next_parameter():
    intcode = initialize_program()
    intcode.advance_ptr()
    assert intcode.ptr == 1
    result = intcode.get_next_parameter()
    assert intcode.ptr == 2
    assert result == 225
    assert type(result) == int

def test_get_input():
    intcode = initialize_program()
    result = intcode.get_input(6, 0)
    assert result == 1100
    assert type(result) == int
    result = intcode.get_input(6, 1)
    assert result == 6
    assert type(result) == int

def test_opcode_1():
    intcode = initialize_program()
    assert intcode.opcode_1(5, 12, 30) == 17
    assert intcode.memory[30] == 17
    assert intcode.opcode_1(11, 3, 30) == 14
    assert intcode.memory[30] == 14

def test_opcode_2():
    intcode = initialize_program()
    assert intcode.opcode_2(5, 12, 30) == 60
    assert intcode.memory[30] == 60
    assert intcode.opcode_2(11, 3, 30) == 33
    assert intcode.memory[30] == 33

def test_store():
    intcode = initialize_program()
    assert intcode.store(5, 12) == 5
    assert intcode.memory[12] == 5
    assert intcode.store(91, 12) == 91
    assert intcode.memory[12] == 91

def test_opcode_5():
    intcode = initialize_program()
    intcode.ptr = 0
    assert intcode.opcode_5(1, 14) == 14
    assert intcode.ptr == 14
    intcode.ptr = 2
    assert intcode.opcode_5(0, 14) == 2
    assert intcode.ptr == 2

def test_opcode_6():
    intcode = initialize_program()
    intcode.ptr = 0
    assert intcode.opcode_6(1, 14) == 0
    assert intcode.ptr == 0
    intcode.ptr = 2
    assert intcode.opcode_6(0, 14) == 14
    assert intcode.ptr == 14

def test_opcode_7():
    intcode = initialize_program()
    intcode.memory[10] = 999
    assert intcode.opcode_7(5, 6, 10) == 1
    assert intcode.memory[10] == 1
    intcode.memory[10] = 999
    assert intcode.opcode_7(5, 4, 10) == 0
    assert intcode.memory[10] == 0

def test_opcode_8():
    intcode = initialize_program()
    intcode.memory[10] = 999
    assert intcode.opcode_8(5, 5, 10) == 1
    assert intcode.memory[10] == 1
    intcode.memory[10] = 999
    assert intcode.opcode_8(5, 4, 10) == 0
    assert intcode.memory[10] == 0