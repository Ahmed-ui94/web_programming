
class Jar:

    def __init__(self, capacity = 12):
        self._cookie_jar = 0
        self._capacity = capacity
        if capacity < 0:
            raise ValueError("provide a positive integer")
    
    def __str__(self) -> str:
         
        return '🍪' * self._cookie_jar
    
    def deposit(self, n):
        self.n = n 
        if (self._cookie_jar + n) > self._capacity:
            raise ValueError("it exceeds capacity of cookie jar")
            return None
        self._cookie_jar += n
        return self._cookie_jar
    
    
    def withdraw(self, n):
        self.n = n
        if (self._cookie_jar - n) > 0 or n < self._cookie_jar:
            self._cookie_jar -= n
            return self._cookie_jar
        else:
            raise ValueError("the are'nt that many cookies in the cookie jar")
            return None
    
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookie_jar
    
    

jar = Jar()
print(jar)
jar.deposit(1)
jar.deposit(8)
jar.withdraw(1)
print(jar)
print(jar.size)