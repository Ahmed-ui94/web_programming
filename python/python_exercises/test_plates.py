from plates import is_valid
#testing whether it starts with two letters
def test_2_letters():
    assert is_valid("cs") == True

def test_maximum_letters():
    assert is_valid("saa300") == True

def test_0_char():
    assert is_valid("als000") == False

def test_numbers_middle():
    assert is_valid("ala303sl") == False
