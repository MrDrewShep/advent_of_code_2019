import puzzle

def test_check_increasing_false_1():
    assert puzzle.check_increasing("123452") == False

def test_check_increasing_false_2():
    assert puzzle.check_increasing("444452") == False

def test_check_increasing_true_1():
    assert puzzle.check_increasing("444457") == True

def test_check_increasing_true_2():
    assert puzzle.check_increasing("444444") == True
    

# PART TWO

def test_check_adjacent_part_2_true_1():
    assert puzzle.check_adjacent_part_2("123344") == True

def test_check_adjacent_part_2_true_2():
    assert puzzle.check_adjacent_part_2("124478") == True

def test_check_adjacent_part_2_true_3():
    assert puzzle.check_adjacent_part_2("111122") == True

def test_check_adjacent_part_2_false_1():
    assert puzzle.check_adjacent_part_2("123444") == False

def test_check_adjacent_part_2_false_2():
    assert puzzle.check_adjacent_part_2("123456") == False
