class vehicle:
    def __init__(self, engine):
        print("inside vehicle constructor")
        self.engine = engine
class car(vehicle):
    def __init__(self, engine,max_speed):
        super().__init__(engine)
        print('inside car constructor')
        self.max_speed = max_speed
class Electric_car(car):
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print("inside Electric_car constructor")
        self.km_range = km_range
#object of electric car 
ev = Electric_car("1500cc",2200, 750)
print(f"engine={ev.engine}, max speed={ev.max_speed}, km range={ev.km_range}")