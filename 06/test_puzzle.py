from puzzle import Galaxy, Planet

def load_data():
    with open("data.txt", "r") as f:
        data = f.readlines()
        data = [i.strip("\n") for i in data]
    return data

def test_find_com_index():
    galaxy = Galaxy(load_data())
    galaxy.data = load_data()
    assert galaxy.find_com_index(3) == 518
    assert galaxy.data[518][:3] == "COM"

def test_load_galaxy():
    galaxy = Galaxy(load_data())
    assert galaxy.com != None
    assert galaxy.com.name == "COM"
    assert len(galaxy.planets) == 1654 #includes com

def test_get_parent_name():
    galaxy = Galaxy(load_data())
    assert galaxy.get_parent_name("AAA)BBB", 3) == "AAA"

def test_get_new_planet_name():
    galaxy = Galaxy(load_data())
    assert galaxy.get_new_planet_name("AAA)BBB", 3) == "BBB"

def test_remove_pair_from_data():
    galaxy = Galaxy(load_data())
    assert len(galaxy.data) == 0
    galaxy.data = load_data()
    assert len(galaxy.data) == 1653
    assert galaxy.remove_pair_from_data("HCP)993") == "HCP)993"
    assert len(galaxy.data) == 1652
