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

def test_get_parameter():
    intcode = initialize_program()
    intcode.advance_ptr()
    assert intcode.ptr == 1
    result = intcode.get_parameter()
    assert intcode.ptr == 2
    assert result == 225

def test_get_input():
    intcode = initialize_program()
    assert intcode.get_input(6) == 1100

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