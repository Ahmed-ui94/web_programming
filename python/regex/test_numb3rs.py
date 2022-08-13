from numb3rs import validate

def test_ip():
    assert validate("1.2.3.4") == True

def test_3_digits():
    assert validate("127.0.0.1") == True

def test_255():
    assert validate("255.255.255.255") == True

def test_above_range():
    assert validate("512.512.512.512") == False

