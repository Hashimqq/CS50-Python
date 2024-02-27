from bank import value


def main():
    test_bank()


def test_bank():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0


if __name__ == '__main__':
    main()
