import pytest
from project import get_difficulty, generate_question, check_answer


def test_get_difficulty():
    assert get_difficulty(1) == 1
    assert get_difficulty(2) == 2
    assert get_difficulty(3) == 3
    assert get_difficulty(4) == 4
    with pytest.raises(SystemExit):
        get_difficulty(5)


def test_generate_question():
    x, y, operation = generate_question(1)
    assert operation == "+"
    assert 1 <= x <= 10
    assert 1 <= y < x

    x, y, operation = generate_question(2)
    assert operation in ["+", "-"]
    assert 1 <= x <= 50
    assert 1 <= y < x


def test_check_answer():
    assert check_answer(3, 2, "+", 5)
    assert not check_answer(3, 2, "+", 6)
    assert check_answer(3, 2, "-", 1)
