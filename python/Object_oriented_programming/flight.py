class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passanger = []
   
   
    # add passanger to the flight
    def add_passanger(self,name):
        self.name = name
        if len(self.passanger) < self.capacity:
            self.passanger.append(name)
        else:
            print(f"Not available seat for {name}")


flight = Flight(3)
peoples = ["Ahmed","Abde","ali","farah"]
for people in peoples:
    flight.add_passanger(people)

print(flight.passanger)