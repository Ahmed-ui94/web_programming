from um import count

def test_correct():
    assert count("Um") == '1'
    assert count("um?") == '1'

def test_possible_wrong():
    assert count("Um, thanks for the album.") == '1'
    assert count("yum ") == None
    assert count(" um ") == '1'