from jar import Jar
import pytest
 

def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(1)
    assert str(jar) == '🍪'
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    
    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdrew():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(5)
    assert jar.size == 1
    
    with pytest.raises(ValueError):
        jar.withdraw(2)
