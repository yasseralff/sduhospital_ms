# Define the Patient class
class Patient:
    def __init__(self, name, doctor_specialist, day, time):
        self.name = name
        self.doctor_specialist = doctor_specialist
        self.time = time
        self.day = day

    # Method to display patient details
    def display(self):
        print("PATIENT NAME : ", self.name)
        print("TO           : ", self.doctor_specialist)
        print("DAY          : ", self.day)
        print("TIME         : ", self.time)
