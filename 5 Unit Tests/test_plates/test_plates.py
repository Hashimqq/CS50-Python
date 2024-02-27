from Py5.test_plates.plates import is_valid

def test_plates():
    assert is_valid("c") == False
    assert is_valid("hello, world") == False
    assert is_valid("CS50") == True

def test_plates1():
    assert is_valid("CS") == False
    assert is_valid("23") == False


def test_plates2():
    assert is_valid("CS32") == False
    assert is_valid("cs.,32") == False

def test_plates3():
    assert is_valid("CS50") == True
    assert is_valid("cs05") == False
