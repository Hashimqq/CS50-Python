from um import count


def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um") == 1
    assert count("um, thanks,um") == 2
    assert count("yum") == 0
    assert count("album") == 0
    assert count("cat") == 0



