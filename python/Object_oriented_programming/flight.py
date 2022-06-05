class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passanger = []
    # add passanger to the flight
    def add_passanger(self,name):
        self.name = name
        if len(self.passanger) > self.capacity:
            self.passanger.append(name)
        else:
            print("No available seat")

flight = Flight(3)
peoples = ["Ahmed","Abde","ali","farah"]
for people in peoples:
    flight.name = people
    flight.add_passanger(flight.passanger)

print(flight.passanger)