from numb3rs import validate


def test_true():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True


def test_false():
    assert validate("256.255.255.255") == False
    assert validate("64.128.256.512") == False
    assert validate("465:iugiu:556:sfgs") == False
    assert validate("cat") == False



