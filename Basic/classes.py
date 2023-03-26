class Point():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []
    
    def add_passenger(self, name):
        if len(self.passenger) < self.capacity:
            self.passenger.append(name)


flight_use = Point(3)
flight_use.add_passenger("Tanvir")
flight_use.add_passenger("Mahmud")
flight_use.add_passenger("Fahim")
flight_use.add_passenger("Rahim")

print(flight_use.passenger)
