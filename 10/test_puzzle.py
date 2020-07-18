from puzzle import Asteroid, Galaxy
import math

galaxy = Galaxy()
ast_0 = Asteroid(2, 2, galaxy)
ast_1 = Asteroid(2, 0, galaxy)
ast_2 = Asteroid(4, 0, galaxy)
ast_3 = Asteroid(4, 2, galaxy)
ast_4 = Asteroid(4, 4, galaxy)
ast_5 = Asteroid(2, 4, galaxy)
ast_6 = Asteroid(0, 4, galaxy)
ast_7 = Asteroid(0, 2, galaxy)
ast_8 = Asteroid(0, 0, galaxy)

def test_get_slope():
    assert ast_0.get_slope(ast_1) == (None, "up")
    assert ast_0.get_slope(ast_2) == (-1, "above")
    assert ast_0.get_slope(ast_3) == (0, "right")
    assert ast_0.get_slope(ast_4) == (1, "below")
    assert ast_0.get_slope(ast_5) == (None, "down")
    assert ast_0.get_slope(ast_6) == (-1, "below")
    assert ast_0.get_slope(ast_7) == (0, "left")
    assert ast_0.get_slope(ast_8) == (1, "above")

def test_get_distance():
    assert ast_0.get_distance(ast_1) == 2
    assert ast_0.get_distance(ast_2).__round__(3) == 2.828

def test_filter_n():
    galaxy.asteroids_detect_each_other()
    