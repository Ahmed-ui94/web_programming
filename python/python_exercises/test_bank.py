from bank import value

def test_with_hello():
    assert value("hello") == "$0"

def test_with_h():
    assert value("hala;") == "$20"

def test_with_other():
    assert value("Ahmed") == "$100"