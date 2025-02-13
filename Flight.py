import random
class Flight():
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination
        self.id = random.random() 