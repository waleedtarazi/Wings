from .Flight import Flight
import random
class Booking():
    def __init__(self, flight, user_name):
        self.flight = flight
        self.user_name = user_name
        self.id = random.random()
        pass
    
    def get_booking_detiels(self):
        return self.flight.departure + self.user_name