# Define the Hospital class
class Hospital:
    def __init__(self, name, location, opening_time, closing_time):
        self.name = name
        self.location = location
        self.opening_time = opening_time
        self.closing_time = closing_time

    # Method to display hospital details
    def display(self):
        print("HOSPITAL NAME            : ", self.name)
        print("HOSPITAL LOCATION        : ", self.location)
        print("HOSPITAL OPENING TIME    : ", self.opening_time)
        print("HOSPITAL CLOSING TIME    : ", self.closing_time)
