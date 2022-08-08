from twitter import shorten

def test_consonats():
    assert shorten("abcd") == "bcd"

def test_vowels():
    assert shorten("aaeiou") == ""

def test_alphabets():
    assert shorten("twitter") == "twttr"