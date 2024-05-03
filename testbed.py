import time
import tkinter as tk
from tkinter import messagebox

class HospitalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="****** HOSPITAL MANAGEMENT *********")
        self.label.grid(row=0, columnspan=2)

        self.btn_hospital_details = tk.Button(self.frame, text="Hospital details", command=self.display_hospital_details)
        self.btn_hospital_details.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.btn_doctor_details = tk.Button(self.frame, text="Doctor details", command=self.display_doctor_details)
        self.btn_doctor_details.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        self.btn_patient_entry = tk.Button(self.frame, text="Patient Entry", command=self.patient_entry)
        self.btn_patient_entry.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

        self.btn_patient_details = tk.Button(self.frame, text="Patient details", command=self.display_patient_details)
        self.btn_patient_details.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

        self.btn_exit = tk.Button(self.frame, text="Exit", command=self.master.quit)
        self.btn_exit.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

    def display_hospital_details(self):
        messagebox.showinfo("Hospital Details", "Hospital Name: SDU\nLocation: Kaskelen\nOpening Time: 7:00am\nClosing Time: 11:00pm")

    def display_doctor_details(self):
        messagebox.showinfo("Doctor Details", "Cardiologist:\nID Number: 01\nName: Dr.Daniyal\nSpecialization: HEART specialist\nSchedule: Monday - Friday, 8AM - 5PM\n\nPediatrician:\nID Number: 02\nName: Dr.Mubeen\nSpecialization: DISEASE AND INJURIES IN CHILDREN\nSchedule: Tuesday - Sunday, 9AM - 7PM\n\nNeurologist:\nID Number: 03\nName: Dr.Sufyan\nSpecialization: specialization in NEUROLOGY\nSchedule: Friday - Sunday, 6AM - 9PM")

    def patient_entry(self):
        # Code for patient entry
        pass

    def display_patient_details(self):
        # Code for displaying patient details
        pass

def main():
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

class Hospital:
    def __init__(self, name, location, opening_time, closing_time):
        self.name = name
        self.location = location
        self.opening_time = opening_time
        self.closing_time = closing_time

    def display(self):
        print("HOSPITAL NAME            : ", self.name)
        print("HOSPITAL LOCATION        : ", self.location)
        print("HOSPITAL OPENING TIME    : ", self.opening_time)
        print("HOSPITAL CLOSING TIME    : ", self.closing_time)


class Patient:
    def __init__(self, name, doctor_specialist, day, time):
        self.name = name
        self.doctor_specialist = doctor_specialist
        self.time = time
        self.day = day

    def display(self):
        print("PATIENT NAME : ", self.name)
        print("TO           : ", self.doctor_specialist)
        print("DAY          : ", self.day)
        print("TIME         : ", self.time)


class Doctor:
    def __init__(self, id_num, name, schedule):
        self.id_num = id_num
        self.name = name
        self.schedule = schedule

class Cardiologist(Doctor):
    def working(self):
        print("A cardiologist is a physician who is an expert in the care of your heart and blood vessels")

    specialization = "HEART specialist"

    def display(self):
        print("         CARDIOLOGIST DOCTOR           ")
        print("ID NUMBER      : ", self.id_num)
        print("NAME           : ", self.name)
        print("SPECIALIZATION : ", self.specialization)
        print("SCHEDULE       : ", self.schedule)


class Pediatrician(Doctor):
    def working(self):
        print(
            "A doctor who has special training in preventing, diagnosing, and treating diseases and injuries in children.")

    specialization = "DISEASE AND INJURIES IN CHILDREN"

    def display(self):
        print("         PEDIATRICIAN DOCTOR           ")
        print("ID NUMBER      : ", self.id_num)
        print("NAME           : ", self.name)
        print("SPECIALIZATION : ", self.specialization)
        print("SCHEDULE       : ", self.schedule)


class Neurologist(Doctor):
    def working(self):
        print(
            "Neurologists are specialists who treat diseases of the brain and spinal cord, peripheral nerves, and muscles")

    specialization = "specialization in NEUROLOGY"

    def display(self):
        print("         NEUROLOGIST DOCTOR           ")
        print("ID NUMBER      : ", self.id_num)
        print("NAME           : ", self.name)
        print("SPECIALIZATION : ", self.specialization)
        print("SCHEDULE       : ", self.schedule)


# MAIN CODE
patients = []
a = 1

while a == 1:
    print("****** HOSPITAL MANAGEMENT *********")
    print("Press '1' for Hospital details")
    print("Press '2' for Doctor details")
    print("Press '3' for Patient Entry")
    print("Press '4' for patient details")
    print("Press '5' to Exit")

    try:
        num = int(input("Enter your number: "))

        if num == 1:
            print("*** Please Wait ***")
            time.sleep(1)
            print("___******____")
            obj = Hospital('SDU', 'Kaskelen', '7:00am', '11:00pm')
            obj.display()
            time.sleep(1)

        elif num == 2:
            print("*** Please Wait ***")
            time.sleep(1)
            print(" **There are three types of Doctors here**")
            print("1: Cardiologist")
            print("2: Pediatrician")
            print("3: Neurologist")
            num_doc = int(input("Enter your number for any doctor details: "))

            if num_doc == 1:
                print("*** Please Wait ***")
                time.sleep(1)
                print("_*******_")
                obj = Cardiologist("01", "Dr.Daniyal", "Monday - Friday, 8AM - 5PM")
                obj.display()
                obj.working()
                time.sleep(1)

            elif num_doc == 2:
                print("*** Please Wait ***")
                time.sleep(1)
                print("_*******_")
                obj = Pediatrician("02", "Dr.Mubeen", "Tuesday - Sunday, 9AM - 7PM")
                obj.display()
                obj.working()
                time.sleep(1)

            elif num_doc == 3:
                print("*** Please Wait ***")
                time.sleep(1)
                print("_*******_")
                obj = Neurologist("03", "Dr.Sufyan", "Friday - Sunday, 6AM - 9PM")
                obj.display()
                obj.working()
                time.sleep(1)

        elif num == 3:
            print(" **There are three types of Doctors here**")
            print("1: Cardiologist")
            print("2: Pediatrician")
            print("3: Neurologist")
            doctor_specialist = int(input("Enter your number for any doctor details: "))
            print("____PATIENT ENTRY______")
            if doctor_specialist == 1:
                doctor_specialist = "Cardiologist"
                doctor_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
                doctor_time = ("8AM", "9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM")

                try:
                    name = input("Enter patient name: ")
                    day = input("Enter your Appointment day (e.g., Monday - Friday): ")

                    while day not in doctor_days:
                        print("Doctor not available on that day.")
                        day = input("Enter your Appointment day (e.g., Monday - Friday): ")

                    print("Doctor is available on", day)

                    time = input("Enter your Appointment time (e.g., 8AM - 5PM): ")

                    while time not in doctor_time:
                        print("Doctor not available at that time.")
                        time = input("Enter your Appointment time (e.g., 8AM - 5PM): ")

                    if any(patient.day == day and patient.time == time for patient in patients):
                        print("Sorry, there is already an appointment scheduled at that time.")
                    else:
                        obj = Patient(name, doctor_specialist, day, time)
                        patients.append(obj)
                        print("Patient details entered.")

                except Exception as e:
                    print("Error occurred:", e)

            elif doctor_specialist == 2:
                doctor_specialist = "Pediatrician"
                doctor_days = ("Tuesday", "Wednesday", "Thursday", "Friday", "Sunday")
                doctor_time = ("9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM")

                try:
                    name = input("Enter patient name: ")
                    day = input("Enter your Appointment day (e.g., Tuesday - Sunday): ")

                    while day not in doctor_days:
                        print("Doctor not available on that day.")
                        day = input("Enter your Appointment day (e.g., Tuesday - Sunday): ")

                    print("Doctor is available on", day)

                    time = input("Enter your Appointment time (e.g., 9AM - 7PM): ")

                    while time not in doctor_time:
                        print("Doctor not available at that time.")
                        time = input("Enter your Appointment time (e.g., 9AM - 7PM): ")

                    if any(patient.day == day and patient.time == time for patient in patients):
                        print("Sorry, there is already an appointment scheduled at that time.")
                    else:
                        obj = Patient(name, doctor_specialist, day, time)
                        patients.append(obj)
                        print("Patient details entered.")

                except Exception as e:
                    print("Error occurred:", e)

            elif doctor_specialist == 3:
                doctor_specialist = "Neurologist"
                doctor_days = ("Friday", "Saturday", "Sunday")
                doctor_time = ("6AM", "7AM", "8AM", "9AM", "10AM","11AM","12PM", "1PM", "2PM", "3PM", "4PM", "5PM",
                               "6PM","7PM", "8PM", "9PM")

                try:
                    name = input("Enter patient name: ")
                    day = input("Enter your Appointment day (e.g., Friday - Sunday): ")

                    while day not in doctor_days:
                        print("Doctor not available on that day.")
                        day = input("Enter your Appointment day (e.g., Friday - Sunday): ")

                    print("Doctor is available on", day)

                    time = input("Enter your Appointment time (e.g., 6AM - 9PM): ")

                    while time not in doctor_time:
                        print("Doctor not available at that time.")
                        time = input("Enter your Appointment time (e.g., 6AM - 9PM): ")

                    if any(patient.day == day and patient.time == time for patient in patients):
                        print("Sorry, there is already an appointment scheduled at that time.")
                    else:
                        obj = Patient(name, doctor_specialist, day, time)
                        patients.append(obj)
                        print("Patient details entered.")


                except Exception as e:
                    print("Error occurred:", e)
            # Similarly handle for Pediatrician and Neurologist

        elif num == 4:
            print("____PATIENT DETAILS______")
            for patient in patients:
                print("Patient name:      ", patient.name)
                print("To          :      ", patient.doctor_specialist)
                print("Day         :      ", patient.day)
                print("Time        :      ", patient.time)

        elif num == 5:
            print("___******____")
            print("Thanks for visiting.")
            a = 0
        else:
            print("Invalid Input. Try again")
    except:
        print("Invalid Input. Try again")