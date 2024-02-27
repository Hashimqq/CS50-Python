from twttr import shorten

def test_twttr():
    assert shorten("hello") == "hll"
    assert shorten("hello, WORLD") == "hll, WRLD"
    assert shorten("123") == "123"
    assert shorten("__..__") == "__..__"
