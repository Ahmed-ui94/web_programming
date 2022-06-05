class Vehicle:
    def __init__(self,speed):
        if speed>200:
            raise Exception("not allowed")
        self.speed = speed

    def __del__(self):
        print("release resources")
    

#creating objects
car = Vehicle(350)
#delete object
del car