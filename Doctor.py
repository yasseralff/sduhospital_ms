# Define the Doctor class
class Doctor:
    def __init__(self, id_num, name, schedule):
        self.id_num = id_num
        self.name = name
        self.schedule = schedule

    # Method to display doctor details
    def display(self):
        print("ID NUMBER      : ", self.id_num)
        print("NAME           : ", self.name)
        print("SCHEDULE       : ", self.schedule)

# Define the Cardiologist class, inheriting from Doctor
class Cardiologist(Doctor):
    def working(self):
        print("A cardiologist is a physician who is an expert in the care of your heart and blood vessels")

    specialization = "HEART specialist"

    # Method to display cardiologist details
    def display(self):
        print("         CARDIOLOGIST DOCTOR           ")
        super().display()
        print("SPECIALIZATION : ", self.specialization)

# Define the Pediatrician class, inheriting from Doctor
class Pediatrician(Doctor):
    def working(self):
        print("A doctor who has special training in preventing, diagnosing, and treating diseases and injuries in children.")

    specialization = "DISEASE AND INJURIES IN CHILDREN"

    # Method to display pediatrician details
    def display(self):
        print("         PEDIATRICIAN DOCTOR           ")
        super().display()
        print("SPECIALIZATION : ", self.specialization)

# Define the Neurologist class, inheriting from Doctor
class Neurologist(Doctor):
    def working(self):
        print("Neurologists are specialists who treat diseases of the brain and spinal cord, peripheral nerves, and muscles")

    specialization = "specialization in NEUROLOGY"

    # Method to display neurologist details
    def display(self):
        print("         NEUROLOGIST DOCTOR           ")
        super().display()
        print("SPECIALIZATION : ", self.specialization)
